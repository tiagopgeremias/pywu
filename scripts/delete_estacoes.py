from inventario.models import Estacoes

def run():
    estacoes = Estacoes.objects.all()
    for estacao in estacoes:
        estacao.delete()