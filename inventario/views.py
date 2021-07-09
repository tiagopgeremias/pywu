from django.http.response import Http404
from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponseNotFound
from inventario.models import Estacoes, FiltroEstacoes, GrupoEstacoes

class Inventario(ListView):
    
    template_name = 'inventario.html'
    context_object_name = 'estacoes'
    content_type='text/plain'

    def get_queryset(self):
        kwargs = {}
        filtros = FiltroEstacoes.objects.filter(grupo_estacoes__id=self.kwargs['grupo'])
        for filtro in filtros:
            kwargs['{}__regex'.format(filtro.campo)] = filtro.valor_pesquisa
            
        return Estacoes.objects.filter(**kwargs)
            

    def get_context_data(self,**kwargs):
        context = super(Inventario,self).get_context_data(**kwargs)
        try:
            gpe = GrupoEstacoes.objects.get(id=self.kwargs['grupo'])
            context['inventario'] = gpe.slug
        except Exception as error:
            raise Http404("Erro 404: Inventário não encontrado")

        context['filiais'] = self.get_queryset().distinct('filial')

        return context

def lista_estacoes_view(request, context):
    return render(
        request,
        'lista_estacoes.html',
        context
    )

def inventario_view(request, context):
    return render(
        request,
        'inventario.html',
        context,
        content_type='text/plain'
    )