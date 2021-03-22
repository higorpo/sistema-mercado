import utils.Log as Log
from view.AbstractTela import AbstractTela


class TelaFormaPagamento(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)

    def adicionar(self):
        Log.log('Digite o nome da nova forma de pagamento a ser cadastrada:')
        return super().ler_string()
