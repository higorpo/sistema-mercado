import time
from controller.AbstractControlador import AbstractControlador
from model.Produto import Produto
from messages.Sistema import mensagens as mensagens_sistema
from messages.Produto import mensagens
from view.TelaProduto import TelaProduto
from utils.faker.Produto import fakeProdutos
from datetime import date


class ControladorProdutos(AbstractControlador):
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema, TelaProduto(self))
        self.__produtos = [*fakeProdutos]

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
        if self.__verifica_tem_dados():
            try:
                produto = self.buscar(mensagens.get('titulo_tela_editar'))
                dados_produto = super()._tela.editar(produto)

                nome, qtd_estoque, preco = dados_produto.values()

                produto.nome = nome if nome != '--' else produto.nome
                produto.preco = preco if preco != '--' else produto.preco
                produto.qtd_estoque = qtd_estoque if qtd_estoque != '--' else produto.qtd_estoque
            except Exception:
                super()._sistema.mensagem_sistema.warning(
                    mensagens_sistema.get('nenhuma_opcao_selecionada'))

    def buscar(self, titulo_tela: str = mensagens.get('titulo_tela_buscar')):
        return super()._tela.buscar(self.__produtos, titulo_tela)

    def pesquisar_opcoes(self, buscar_por: str):
        return list(filter(lambda x: buscar_por.lower() in x.nome.lower(), self.__produtos))

    def __verifica_tem_dados(self) -> bool:
        if len(self.__produtos) == 0:
            super()._sistema.mensagem_sistema.log(
                mensagens.get('nada_cadastrado_busca')
            )
            super()._sistema.mensagem_sistema.warning(
                mensagens_sistema.get('enter_continuar')
            )
            input()
            return False
        else:
            return True
