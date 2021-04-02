from controller.AbstractControlador import AbstractControlador
from model.Pedido import Pedido
from messages.Sistema import mensagens as mensagens_sistema
from messages.Pedido import mensagens
from view.TelaPedido import TelaPedido
from datetime import date


class ControladorPedidos(AbstractControlador):
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema, TelaPedido(self))
        self.__pedidos = []

    def abre_tela(self):
        super().abre_tela(mensagens_sistema.get('titulo_opcoes'), [
            mensagens.get('adicionar'),
            mensagens.get('listar'),
        ], [
            self.adicionar_pedido,
            self.listar_pedido
        ])

    def adicionar_pedido(self):
        observacao = super()._tela.adicionar()
        data_atual = date.today().strftime('%d/%m/%Y')
        cliente = super()._sistema.controlador_clientes.buscar()
        forma_pagamento = super()._sistema.controlador_formas_pagamento.buscar()
        self.__pedidos.append(
            Pedido(observacao, data_atual, cliente, forma_pagamento))

    def listar_pedido(self):
        super()._tela.listar(self.__pedidos)
