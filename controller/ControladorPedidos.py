from controller.AbstractControlador import AbstractControlador
from model.Pedido import Pedido
from messages.Sistema import mensagens as mensagens_sistema
from messages.Pedido import mensagens
from view.TelaPedido import TelaPedido
from model.ItemPedido import ItemPedido
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
        # Funcionario #(é pra ter funcionário no pedido também?)
        forma_pagamento = super()._sistema.controlador_formas_pagamento.buscar()

        pedido = Pedido(observacao, data_atual, cliente, forma_pagamento)

        produtos = super()._sistema.controlador_produtos.selecionar_produtos()

        for produto in produtos:
            flag = True
            while flag:
                quantidade_comprada = super(
                )._sistema.controlador_produtos.definir_quantidade_comprada(produto)
                # Verifica se tem no estoque
                if (produto.qtd_estoque - quantidade_comprada) >= 0:
                    produto.qtd_estoque -= quantidade_comprada
                    pedido.adicionar_item_pedido(
                        ItemPedido(pedido, produto, quantidade_comprada))
                    cliente.adicionar_novo_pedido(pedido)
                    flag = False
                else:
                    super()._sistema.mensagem_sistema.warning(
                        mensagens_sistema.get('nao_tem_estoque'))

        self.__pedidos.append(pedido)

    def listar_pedido(self):
        super()._tela.listar(self.__pedidos)
