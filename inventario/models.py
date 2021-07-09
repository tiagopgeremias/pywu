import re
from django.db import models
from django.db.models.deletion import PROTECT
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from django.core.exceptions import ValidationError
from django.utils.text import slugify


class GrupoEstacoes(models.Model):
    titulo = models.CharField(max_length=150, null=False, blank=False)
    slug = models.CharField(max_length=150, null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)


    def __str__(self) -> str:
        return self.titulo

    class Meta:
        verbose_name = 'Grupos Estações'
        verbose_name_plural = "Grupos estações"

@receiver(pre_save, sender=GrupoEstacoes)
def geral_slugfy(sender, instance, **kwargs):
    instance.slug = slugify(instance.titulo)


class FiltroEstacoes(models.Model):
    choice_campo_filtro = [
        ('hostname', 'Hostname'),
        ('endereco_ip', 'Endereço IP'),
        ('filial', 'Filial'),
        ('tipo_estacao', 'Tipo de Estação'),
        ('tipo_pdv','Tipo de PDV')
    ]

    
    campo = models.CharField(choices=choice_campo_filtro, max_length=100)
    valor_pesquisa = CharField(max_length=500, null=False, blank=False)
    grupo_estacoes = ForeignKey(GrupoEstacoes, on_delete=models.CASCADE)

    def __str__(self):
        return self.grupo_estacoes.titulo


@receiver(pre_save,sender=FiltroEstacoes)
def valida_regex(sender,instance,**kwargs):
    try:
        re.compile(instance.valor_pesquisa)
    except Exception as error:
        raise ValidationError({'valor_pesquisa': ["Regex inválido"]})

class Estacoes(models.Model):

    tipo_estacao_choice = [
        ('servidor', 'servidor'),
        ('pdv', 'pdv'),
        ('retaguarda','retaguarda'),
        ('farmaceutica','farmaceutica')
    ]
    tipo_pdv_choice = [
        ('omni_caixa','omni_caixa'),
        ('omni_balcao','omni_balcao'),
        ('pharmax','pharmax')
    ]

    hostname = models.CharField(max_length=100, null=False, blank=False,unique=True)
    endereco_ip = models.CharField(max_length=100, null=False, blank=False,unique=True)
    filial = models.CharField(max_length=3, null=False, blank=False)
    tipo_estacao = models.CharField(max_length=50, choices=tipo_estacao_choice)
    tipo_pdv = models.CharField(max_length=50,choices=tipo_pdv_choice,blank=True,null=True)
    descricao = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Estação'
        verbose_name_plural = "Estações"

    def __str__(self):
        return self.hostname

@receiver(pre_save,sender=Estacoes)
def signals_receiver(sender, instance, **kwargs):
    if instance.tipo_estacao == 'pdv':
        if instance.tipo_pdv not in ['omni_caixa','omni_balcao','pharmax']:
            raise ValidationError({'tipo_pdv': ["Escolha um tipo de PDV"]})
    else:
        if instance.tipo_pdv in ['omni_caixa','omni_balcao','pharmax']:
            raise ValidationError({'tipo_pdv': ["Estação não é PDV, deixe em branco"]})