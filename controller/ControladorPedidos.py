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
        # Funcionario
        # Forma pagamento
        forma_pagamento = super()._sistema.controlador_formas_pagamento.buscar()

        pedido = Pedido(observacao, data_atual, cliente, forma_pagamento)

        # Produtos
        produtos = ...

        for produto in produtos:
            # Chamar no controlador de produto uma tela para pedir a quantidade de produtos em cada um dos produtos
            quantidade_comprada = ...

            # Verifica se tem no estoque
            if ...:
                produto.qtd_estoque -= 1  # diminuir do estoque
                pedido.adicionar_item_pedido(
                    ItemPedido(self, produto, quantidade_comprada))
                cliente.adicionar_pedidos(pedido)
            else:
                # ...

        self.__pedidos.append(pedido)

    def listar_pedido(self):
        super()._tela.listar(self.__pedidos)
