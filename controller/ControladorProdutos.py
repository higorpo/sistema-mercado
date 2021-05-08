import time
from controller.AbstractControlador import AbstractControlador
from model.Produto import Produto
from messages.Sistema import mensagens as mensagens_sistema
from messages.Produto import mensagens
from view.TelaProduto import TelaProduto
from view.TelaProdutoCadastro import TelaProdutoCadastro
from view.TelaProdutoSelecao import TelaProdutoSelecao
from view.TelaProdutoDefinirQuantidade import TelaProdutoDefinirQuantidade
from utils.faker.Produto import fakeProdutos
from datetime import date
from configs.settings import Settings
from utils.exceptions import NenhumaOpcaoParaSelecionar
from utils.exceptions.TelaFechada import TelaFechada


class ControladorProdutos:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela = TelaProduto(self)
        self.__tela_cadastro = TelaProdutoCadastro(self)
        self.__tela_selecao = TelaProdutoSelecao(self)
        self.__tela_definir_quantidade = TelaProdutoDefinirQuantidade(self)
        self.__produtos = \
            [*fakeProdutos] if Settings.INICIAR_SISTEMA_COM_DADOS_FAKES else []

    def abre_tela(self):
        while True:
            event, values = self.__tela.abrir_tela(self.map_object_to_array())
            if event == 'exited':
                break
            elif event == 'btn_cadastrar':
                self.__tela.fechar_tela()
                self.adicionar()
            elif event == 'btn_deletar':
                self.excluir(values)
                self.__tela.fechar_tela()
            elif event == 'btn_editar':
                self.__tela.fechar_tela()
                self.editar(values)

    def map_object_to_array(self):
        return list(map(lambda item: [item.nome, item.qtd_estoque, item.marca, item.preco, item.categoria.nome], self.__produtos))

    def adicionar(self):
        event, dados_produto = self.__tela_cadastro.abrir_tela(False, None)

        if event == 'criar':
            # Cadastra categoria se não houver nenhuma
            if len(self.__controlador_sistema.controlador_cat_produto.categorias) == 0:
                dados_produto['categoria'] = \
                    self.__controlador_sistema.controlador_cat_produto.adicionar()
            else:
                # Seleciona categoria
                try:
                    dados_produto['categoria'] = \
                        self.__controlador_sistema.controlador_cat_produto.buscar(
                            mensagens.get('selecionar_categoria_adicionar_produtos'))
                except NenhumaOpcaoParaSelecionar:
                    self.__controlador_sistema.mensagem_sistema.error(
                        mensagens.get('erro_cadastrar'))
                    return

            # Verifica se o produto já está cadastrado, caso não esteja, cadastra
            if len([x for x in self.__produtos if x.nome == dados_produto['nome'] and x.categoria.nome == dados_produto['categoria'].nome and x.marca == dados_produto['marca']]) == 0:
                instancia_produto = Produto(*dados_produto.values())
                dados_produto['categoria'].adicionar_produto(instancia_produto)
                self.__produtos.append(instancia_produto)
            else:
                self.__controlador_sistema.mensagem_sistema.warning(
                    mensagens.get('ja_cadastrado'))
        else:
            raise TelaFechada

    def listar(self):
        super()._tela.listar(self.__produtos, mensagens)

    def excluir(self, produtoIndex):
        try:
            self.__produtos.remove(self.__produtos[produtoIndex])
        except Exception:
            self.__controlador_sistema\
                .mensagem_sistema.error(mensagens.get('erro_excluir'))

    def editar(self, produtoIndex):
        try:
            produto = self.__produtos[produtoIndex]

            event, dados_produtos = self.__tela_cadastro.abrir_tela(
                True, produto)

            if event == 'exited':
                return
            elif event == 'criar':
                _, qtd_estoque, _, preco, _ = dados_produtos.values()

                produto.qtd_estoque = qtd_estoque
                produto.preco = preco

        except NenhumaOpcaoSelecionada:
            self.__controlador_sistema\
                .mensagem_sistema.warning(mensagens_sistema.get('nenhuma_opcao_selecionada'))

    def buscar(self, titulo_tela: str):
        event, index_dos_produtos = self.__tela_selecao.abrir_tela(
            self.map_object_to_array()
        )

        if event == 'exited':
            raise TelaFechada
        elif event == 'selecionado':
            print([x for x in self.__produtos if self.__produtos.index(
                x) in index_dos_produtos])
            return [x for x in self.__produtos if self.__produtos.index(x) in index_dos_produtos]

    def pesquisar_opcoes(self, buscar_por: str):
        return list(filter(lambda x: buscar_por.lower() in x.nome.lower(), self.__produtos))

    # TODO: Implementar depois (seleção múltipla de produtos)
    def selecionar_produtos(self, titulo_tela: str):
        produtos_em_estoque = [x for x in self.__produtos if x.qtd_estoque > 0]
        try:
            return self.__tela.selecionar_produtos(produtos_em_estoque, mensagens.get('titulo_tela_selecionar'))
        except ValueError:
            super()._sistema.abre_tela()

    # TODO: Implementar depois, quando mover o método da TelaProduto pra uma nova tela separada
    def definir_quantidade_comprada(self, produtos_selecionados: list):
        return self.__tela_definir_quantidade.abrir_tela(produtos_selecionados)

    def tem_produtos_estoque(self) -> bool:
        tem_produtos_estoque = False

        for produto in self.__produtos:
            if produto.qtd_estoque > 0:
                tem_produtos_estoque = True
                break
        return tem_produtos_estoque
