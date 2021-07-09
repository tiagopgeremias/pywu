from inventario.models import Estacoes


def run():
    for filial in range(1,491):
        tmp_f = str(filial)
        ip = '10.'

        if len(tmp_f) == 1:
            numero_filial = f'00{tmp_f}'
            ip += f'0.{tmp_f}.'
        elif len(tmp_f) == 2:
            numero_filial = f'0{tmp_f}'
            ip += f'0.{tmp_f}.'
        else:
            numero_filial = tmp_f
            ip += f'{numero_filial[0]}.{int(numero_filial[-2:])}.'
        
        Estacoes.objects.bulk_create([
            Estacoes(
                filial=numero_filial,
                hostname='phw'+numero_filial+'001',
                endereco_ip=ip+"40",
                tipo_estacao='servidor'
            ),
            Estacoes(
                filial=numero_filial,
                hostname='phw'+numero_filial+'002',
                endereco_ip=ip+"41",
                tipo_estacao='retaguarda'
            ),
            Estacoes(
                filial=numero_filial,
                hostname='farmaceutica'+numero_filial,
                endereco_ip=ip+"50",
                tipo_estacao='farmaceutica'
            )
        ])

        for estacao in range(42,46):
            try:
                hostname = 'phw'+numero_filial+'0'+str(estacao-30)
                endereco_ip = ip+str(estacao)
                e = Estacoes()
                e.filial = numero_filial
                e.hostname = hostname
                e.endereco_ip = endereco_ip
                e.tipo_estacao = 'pdv'
                if estacao in [42,44]:
                    e.tipo_pdv = 'omni_caixa'
                elif estacao == 43:
                    e.tipo_pdv = 'pharmax'
                else:
                    e.tipo_pdv = 'omni_balcao'
                e.save()
            except Exception as error:
                print('Ocorreu um erro ao inserir a estação')
                print(error)
        
            
            