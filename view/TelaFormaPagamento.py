import utils.Log as Log
from view.AbstractTela import AbstractTela


class TelaFormaPagamento(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)

    def adicionar(self):
        Log.log('Digite o nome da nova forma de pagamento a ser cadastrada:')
        return super().ler_string()

    def listar(self, formas_pagamento):
        Log.clear()
        Log.info('Mostrando formas de pagamento cadastradas')

        if len(formas_pagamento) == 0:
            Log.log('Não há nada cadastrado para ser listado...')
        else:
            for forma_pagamento in formas_pagamento:
                Log.log(
                    f'- Código: {forma_pagamento.codigo}    |    Método: {forma_pagamento.metodo}')

        Log.warning('Pressione enter para continuar')
        input()
