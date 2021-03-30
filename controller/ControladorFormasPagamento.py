from controller.AbstractControlador import AbstractControlador
from view.TelaFormaPagamento import TelaFormaPagamento
from model.FormaPagamento import FormaPagamento
from messages.FormaPagamento import mensagens
from messages.Sistema import mensagens as mensagens_sistema


class ControladorFormasPagamento(AbstractControlador):
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema, TelaFormaPagamento(self))
        self.__formas_pagamentos = []

    def abre_tela(self):
        super().abre_tela(mensagens_sistema.get('titulo_tela_opcoes'), [
            mensagens.get('cadastrar'),
            mensagens.get('listar')
        ], [
            self.adicionar,
            self.listar
        ])

    def adicionar(self):
        forma_pagamento = super()._tela.adicionar()
        if len([x for x in self.__formas_pagamentos if x.metodo == forma_pagamento]) == 0:
            self.__formas_pagamentos.append(FormaPagamento(forma_pagamento))
        else:
            super()._sistema.mensagem_sistema.warning(mensagens.get('ja_cadastrado'))
            self.adicionar()

    def listar(self):
        super()._tela.listar(self.__formas_pagamentos)
