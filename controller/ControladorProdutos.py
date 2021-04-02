import time
from controller.AbstractControlador import AbstractControlador
from model.Produto import Produto
from messages.Sistema import mensagens as mensagens_sistema
from messages.Produto import mensagens
from view.TelaProduto import TelaProduto
from datetime import date


class ControladorProdutos(AbstractControlador):
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema, TelaProduto(self))
        self.__produtos = []

    def abre_tela(self):
        super().abre_tela(mensagens_sistema.get('titulo_opcoes'), [
            mensagens.get('adicionar'),
            mensagens.get('listar'),
            mensagens.get('editar')
        ], [
            self.adicionar,
            self.listar,
            self.editar,
        ])

    def adicionar(self):
        dados_produto = super()._tela.adicionar()

        # Obtem os dados da categoria deste produto
        # Verifica se existe categorias de produto para cadastrar, se não possuir, abre a tela para o cadastro.
        if len(super()._sistema.controlador_cat_produto.categorias) == 0:
            # Cadastra categoria
            super()._sistema.mensagem_sistema.clear()
            dados_produto['categoria'] = \
                super()._sistema.controlador_cat_produto.adicionar()
        else:
            # Seleciona categoria
            try:
                dados_produto['categoria'] = \
                    super()._sistema.controlador_cat_produto.buscar(
                        mensagens.get('selecionar_categoria_adicionar_produtos'))
            except NenhumaOpcaoParaSelecionar:
                super()._sistema.mensagem_sistema.error(mensagens.get('erro_cadastrar'))
                return

        # Verifica se o produto já está cadastrado, caso não esteja, cadastra
        if len([x for x in self.__produtos if x.nome == dados_produto['nome'] and x.categoria.nome == dados_produto['categoria'].nome and x.marca == dados_produto['marca']]) == 0:
            instancia_marca = Produto(*dados_produto.values())
            dados_produto['categoria'].adicionar_produto(instancia_marca)
            self.__produtos.append(instancia_marca)
        else:
            super()._sistema.mensagem_sistema.warning(mensagens.get('ja_cadastrado'))
            time.sleep(1)

    def listar(self):
        super()._tela.listar(self.__produtos)

    def editar(self):
        pass
