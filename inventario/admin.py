from django.contrib import admin
from django.apps import apps
from django.utils.html import format_html
from django.urls import re_path
from .models import Estacoes, GrupoEstacoes, FiltroEstacoes
from .views import lista_estacoes_view, inventario_view
from django.core.paginator import Paginator
import collections
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.contrib import messages
import re

class GrupoEstacoesForm(ModelForm):
    def clean(self):
        super(GrupoEstacoesForm, self).clean()
        try:
            re.compile(self.cleaned_data.get('valor_pesquisa'))
        except Exception as error:
            raise ValidationError({'valor_pesquisa': ["Regex inválido"]})

class FiltroEstacoesInline(admin.TabularInline):
    form = GrupoEstacoesForm
    model = FiltroEstacoes
    extra = 0

@admin.register(GrupoEstacoes)
class GrupoEstacoesAdmin(admin.ModelAdmin):
    list_display = ['titulo','totalEstacoes','totalPdv','totalRetaguarda','totalFarmaceutica','totalServidor','totalFiliais','linkListaEstacoes', 'linkInventarioEstacoes']
    readonly_fields = ['slug','totalEstacoes']
    inlines = [FiltroEstacoesInline,]

    def getEstacoes(self, object_id):
        kwargs = {}
        filtros = FiltroEstacoes.objects.filter(grupo_estacoes__id=object_id)
        for filtro in filtros:
            kwargs['{}__regex'.format(filtro.campo)] = filtro.valor_pesquisa
        estacoes = Estacoes.objects.filter(**kwargs)
        return estacoes        

    def totalEstacoes(self, obj):
        estacoes = self.getEstacoes(obj.id).count()
        return estacoes
    totalEstacoes.short_description = 'Total'

    def totalFiliais(self,obj):
        filiais = self.getEstacoes(obj.id).distinct('filial').count()
        return filiais
    totalFiliais.short_description = 'Filiais'

    def totalPdv(self,obj):
        pdv = self.getEstacoes(obj.id).filter(tipo_estacao='pdv').count()
        return pdv
    totalPdv.short_description = 'PDV\'s'

    def totalServidor(self,obj):
        servidor = self.getEstacoes(obj.id).filter(tipo_estacao='servidor').count()
        return servidor
    totalServidor.short_description = 'Servidores'

    def totalFarmaceutica(self,obj):
        farmaceutica = self.getEstacoes(obj.id).filter(tipo_estacao='farmaceutica').count()
        return farmaceutica
    totalFarmaceutica.short_description = 'Farmaceuticas'

    def totalRetaguarda(self,obj):
        retaguarda = self.getEstacoes(obj.id).filter(tipo_estacao='retaguarda').count()
        return retaguarda
    totalRetaguarda.short_description = 'Retaguardas'

    def linkInventarioEstacoes(self, obj):
        link = f"/inventario/{obj.id}"
        return format_html(f'<a href="{link}" target="_blank">Detalhes</a>')
    linkInventarioEstacoes.short_description = 'Inventario'

    def linkListaEstacoes(self, obj):
        link = f"/admin/{obj._meta.app_label}/{obj._meta.model_name}/{obj.id}/lista_estacoes"
        return format_html(f'<a href="{link}">Detalhes</a>')
    linkListaEstacoes.short_description = 'Lista de estações'

    def get_urls(self):
        urls = super(GrupoEstacoesAdmin, self).get_urls()
        lista_estacoes_url = [
            re_path(
                r'^(?P<object_id>.*)/lista_estacoes/$',
                self.admin_site.admin_view(self.lista_estacoes),
                name='legacy_legacycollaborator_sync_ldap'
            ),
            re_path(
                r'^(?P<object_id>.*)/inventario$',
                self.admin_site.admin_view(self.get_inventario),
                name='inventario_ansible'
            ),
        ]
        return lista_estacoes_url + urls

    def lista_estacoes(self, request, object_id):
        page_number = request.GET.get('page') or 1
        estacoes = list(self.getEstacoes(object_id=object_id))
        
        e = Paginator(estacoes,50)
        gp_estacoes = GrupoEstacoes.objects.get(id=object_id)

        app__ = apps.get_app_configs()
        app_list = []

        for a in app__:
            if a.label in ['admin','contenttypes','sessions','messages','staticfiles','django_extensions']:
                pass
            else:
                md = a.get_models()
                modelsconfigs = {}

                app_list.append({
                    'name': a.verbose_name,
                    'app_label': a.label,
                    'app_url': f'/admin/{a.label}/',
                    'models':[]
                })

                for m in md:
                    if admin.site.is_registered(m):
                        modelsconfigs[m._meta.model_name] = {
                            'admin_url': f'/admin/{a.label}/{m._meta.model_name}/',
                            'name': m._meta.verbose_name_plural.title(),
                            'add_url': f'/admin/{a.label}/{m._meta.model_name}/add/',
                        }

                od = collections.OrderedDict(sorted(modelsconfigs.items()))
                
                for k, v in od.items():
                    app_list[-1]['models'].append(v)

        context = {
            'title': gp_estacoes.titulo,
            'available_apps':app_list,
            'is_nav_sidebar_enabled':True,
            'page_obj':e.get_page(page_number)
        }
        return lista_estacoes_view(request,context)
    
    def get_inventario(self, request, object_id):
        estacoes = self.getEstacoes(object_id=object_id)
        gp_estacoes = GrupoEstacoes.objects.get(id=object_id)

        filiais = estacoes.distinct('filial')

        context = {
            'filiais': filiais,
            'grupos': gp_estacoes,
            'estacoes': list(estacoes)
        }
        return inventario_view(request, context)

class EstacoeslForm(ModelForm):
    def clean(self):
        super(EstacoeslForm, self).clean()
        tipo_estacao = self.cleaned_data.get('tipo_estacao')
        tipo_pdv = self.cleaned_data.get('tipo_pdv')
        if tipo_estacao == 'pdv':
            if tipo_pdv not in ['omni_caixa','omni_balcao','pharmax']:
                raise ValidationError({'tipo_pdv': ["Escolha um tipo de PDV"]})
        else:
            if tipo_pdv in ['omni_caixa','omni_balcao','pharmax']:
                raise ValidationError({'tipo_pdv': ["Estação não é PDV, deixe em branco"]})

@admin.register(Estacoes)
class EstacoesAdmin(admin.ModelAdmin):
    list_display = ['hostname','tipo_estacao','tipo_pdv','filial','endereco_ip']
    search_fields = ['hostname','tipo_estacao','filial','endereco_ip']
    form = EstacoeslForm
    fieldsets = (
        ('Identificação',{
            'fields':(('hostname','endereco_ip'),),
            
        }),
        ('Caracteristicas',{
            'fields':(('filial','tipo_estacao','tipo_pdv'),)
        }),
        ('Observações',{
            'fields':('descricao',)
        }),
    )

