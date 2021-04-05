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
        # Verifica se existem produtos cadastrados em estoque antes de realizar o cadastro de um pedido
        if not super()._sistema.controlador_produtos.tem_produtos_estoque:
            super()._sistema.mensagem_sistema.error(
                mensagens.get('sem_produtos_estoque')
            )
            super()._sistema.mensagem_sistema.warning(
                mensagens_sistema.get('enter_continuar')
            )
            input()
            return

        observacao = super()._tela.adicionar()
        data_atual = date.today().strftime('%d/%m/%Y')

        # Verifica se existe clientes para cadastrar, se não possuir, abre a tela para o cadastro.
        if len(super()._sistema.controlador_clientes.clientes) == 0:
            super()._sistema.mensagem_sistema.clear()
            super()._sistema.mensagem_sistema.info(
                mensagens.get('cadastro_cliente_adicionar_pedido'))
            cliente = \
                super()._sistema.controlador_clientes.cadastrar()
        else:
            try:
                cliente = \
                    super()._sistema.controlador_clientes.buscar(
                        mensagens.get(
                            'selecionar_cliente_adicionar_pedido'
                        )
                    )
            except NenhumaOpcaoParaSelecionar:
                super()._sistema.mensagem_sistema.error(mensagens.get('erro_cadastrar'))
                return

        # Verifica se existe funcionário para cadastrar, se não possuir, abre a tela para o cadastro.
        if len(super()._sistema.controlador_funcionarios.funcionarios) == 0:
            super()._sistema.mensagem_sistema.clear()
            super()._sistema.mensagem_sistema.info(
                mensagens.get('cadastro_funcionario_adicionar_pedido'))
            funcionario = \
                super()._sistema.controlador_funcionarios.adicionar()
        else:
            try:
                funcionario = \
                    super()._sistema.controlador_funcionarios.buscar(
                        mensagens.get(
                            'selecionar_funcionario_adicionar_pedido'
                        )
                    )
            except NenhumaOpcaoParaSelecionar:
                super()._sistema.mensagem_sistema.error(mensagens.get('erro_cadastrar'))
                return

        # Verifica se existe formas de pagamento para cadastrar, se não possuir, abre a tela para o cadastro.
        if len(super()._sistema.controlador_formas_pagamento.formas_pagamento) == 0:
            super()._sistema.mensagem_sistema.clear()
            super()._sistema.mensagem_sistema.info(
                mensagens.get('cadastro_forma_pagamento_adicionar_pedido'))
            forma_pagamento = \
                super()._sistema.controlador_formas_pagamento.adicionar()
        else:
            try:
                forma_pagamento = \
                    super()._sistema.controlador_formas_pagamento.buscar(
                        mensagens.get(
                            'selecionar_forma_pagamento_adicionar_pedido'
                        )
                    )
            except NenhumaOpcaoParaSelecionar:
                super()._sistema.mensagem_sistema.error(mensagens.get('erro_cadastrar'))
                return

        pedido = Pedido(observacao, data_atual,
                        cliente, funcionario, forma_pagamento)

        produtos = super()._sistema.controlador_produtos.selecionar_produtos()

        for produto in produtos:
            flag = True
            while flag:
                quantidade_comprada = \
                    super()._sistema.controlador_produtos.definir_quantidade_comprada(produto)
                # Verifica se tem no estoque
                if (produto.qtd_estoque - quantidade_comprada) >= 0:
                    produto.qtd_estoque -= quantidade_comprada
                    pedido.adicionar_item_pedido(
                        ItemPedido(pedido, produto, quantidade_comprada)
                    )
                    cliente.adicionar_novo_pedido(pedido)
                    flag = False
                else:
                    super()._sistema.mensagem_sistema \
                        .warning(mensagens.get('nao_tem_estoque'))

        self.__pedidos.append(pedido)

        # Entrega o faturamento do pedido
        total_preco = pedido.obter_dados_faturamento()

        super()._sistema.mensagem_sistema \
            .info(mensagens.get('preco_compra')(total_preco))

        super()._sistema.mensagem_sistema.warning(
            mensagens_sistema.get('enter_continuar')
        )
        input()

    def listar_pedido(self):
        super()._tela.listar(self.__pedidos, mensagens)
