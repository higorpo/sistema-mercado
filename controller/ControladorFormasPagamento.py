import utils.Log as Log
from controller.AbstractControlador import AbstractControlador
from view.TelaFormaPagamento import TelaFormaPagamento
from model.FormaPagamento import FormaPagamento


class ControladorFormasPagamento(AbstractControlador):
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema, TelaFormaPagamento(self))
        self.__formas_pagamentos = []

    def abre_tela(self):
        super().abre_tela('O que você deseja fazer?', [
            'Cadastrar nova forma de pagamento',
            'Listar todas as formas de pagamento'
        ], [
            self.adicionar,
            self.listar
        ])

    def adicionar(self):
        forma_pagamento = super()._tela.adicionar()
        if len([x for x in self.__formas_pagamentos if x.metodo == forma_pagamento]) == 0:
            self.__formas_pagamentos.append(FormaPagamento(forma_pagamento))
        else:
            # TODO: Remover os prints da tela
            Log.warning('AVISO: Essa forma de pagamento já foi cadastrada!')
            self.adicionar()

    def listar(self):
        super()._tela.listar(self.__formas_pagamentos)
