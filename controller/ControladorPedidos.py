from model.Pedido import Pedido
from messages.Sistema import mensagens as mensagens_sistema
from messages.Pedido import mensagens
from view.TelaPedido import TelaPedido
from view.TelaPedidoCadastro import TelaPedidoCadastro
from model.ItemPedido import ItemPedido
from datetime import date
from utils.exceptions.NenhumaOpcaoParaSelecionar import NenhumaOpcaoParaSelecionar
from dao.PedidoDAO import PedidoDAO


class ControladorPedidos:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela = TelaPedido(self)
        self.__tela_cadastro = TelaPedidoCadastro(self)
        self.__dao = PedidoDAO()

    # TODO: Colocar alguma exceção ali
    def abre_tela(self):
        while True:
            event, values = self.__tela.abrir_tela(self.map_object_to_array())
            if event == 'exited':
                break
            elif event == 'btn_cadastrar':
                self.__tela.fechar_tela()
            # try:
                self.adicionar()
            # except Exception:
            #    print('alguma exceção')

    def map_object_to_array(self):
        return list(map(lambda item: [item.codigo, item.observacao, item.data_pedido, item.cliente.nome, item.funcionario.nome, item.forma_pagamento.metodo, item.obter_itens_pedido()], self.__dao.get_all()))

    def adicionar(self):
        # Verifica se existem produtos cadastrados em estoque antes de realizar o cadastro de um pedido
        if not self.__controlador_sistema.controlador_produtos.tem_produtos_estoque():
            self.__tela_cadastro.sem_estoque()
            return

        event, dados_pedido = self.__tela_cadastro.abrir_tela()

        if event == 'criar':
            # Verifica se existe clientes para cadastrar, se não possuir, abre a tela para o cadastro.
            if len(self.__controlador_sistema.controlador_clientes.clientes) == 0:
                dados_pedido['cliente'] = \
                    self.__controlador_sistema.controlador_clientes.adicionar()
            else:
                try:
                    dados_pedido['cliente'] = \
                        self.__controlador_sistema.controlador_clientes.buscar(
                            mensagens.get(
                                'selecionar_cliente_adicionar_pedido'
                            )
                    )
                except NenhumaOpcaoParaSelecionar:
                    self.__controlador_sistema.mensagem_sistema.error(
                        mensagens.get('erro_cadastrar'))
                    return

            # Verifica se existe funcionário para cadastrar, se não possuir, abre a tela para o cadastro.
            if len(self.__controlador_sistema.controlador_funcionarios.funcionarios) == 0:
                dados_pedido['funcionario'] = \
                    self.__controlador_sistema.controlador_funcionarios.adicionar()
            else:
                try:
                    dados_pedido['funcionario'] = \
                        self.__controlador_sistema.controlador_funcionarios.buscar(
                            mensagens.get(
                                'selecionar_funcionario_adicionar_pedido'
                            )
                    )
                except NenhumaOpcaoParaSelecionar:
                    self.__controlador_sistema.mensagem_sistema.error(
                        mensagens.get('erro_cadastrar'))
                    return

            # Verifica se existe formas de pagamento para cadastrar, se não possuir, abre a tela para o cadastro.
            if len(self.__controlador_sistema.controlador_formas_pagamento.formas_pagamento) == 0:
                dados_pedido['forma_pagamento'] = \
                    self.__controlador_sistema.controlador_formas_pagamento.adicionar()
            else:
                try:
                    dados_pedido['forma_pagamento'] = \
                        self.__controlador_sistema.controlador_formas_pagamento.buscar(
                            mensagens.get(
                                'selecionar_forma_pagamento_adicionar_pedido'
                            )
                    )
                except NenhumaOpcaoParaSelecionar:
                    self.__controlador_sistema.mensagem_sistema.error(
                        mensagens.get('erro_cadastrar'))
                    return

            pedido = Pedido(*dados_pedido.values())

            produtos_selecionados = self.__controlador_sistema.controlador_produtos.buscar(
                mensagens.get('selecionar_produtos_adicionar_pedido'))

            dict_quantidade_comprada = \
                self.__controlador_sistema.controlador_produtos.definir_quantidade_comprada(
                    produtos_selecionados)

            for produto in produtos_selecionados:
                pedido.adicionar_item_pedido(ItemPedido(
                    pedido, produto, dict_quantidade_comprada[produto.codigo]))
                produto.qtd_estoque = int(
                    produto.qtd_estoque) - dict_quantidade_comprada[produto.codigo]

            dados_pedido['cliente'].adicionar_novo_pedido(pedido)
            self.__dao.add(pedido)

            # Entrega o faturamento do pedido
            total_preco = pedido.obter_dados_faturamento()
            self.__tela.exibir_preco_final(total_preco)
        else:
            raise TelaFechada

    # TODO: Remover no futuro
    def listar_pedidos(self):
        super()._tela.listar(self.__dao.get_all(), mensagens)
