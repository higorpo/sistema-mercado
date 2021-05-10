import time
from model.Produto import Produto
from messages.Sistema import mensagens as mensagens_sistema
from messages.Produto import mensagens
from view.TelaProduto import TelaProduto
from view.TelaProdutoCadastro import TelaProdutoCadastro
from view.TelaProdutoSelecao import TelaProdutoSelecao
from view.TelaProdutoDefinirQuantidade import TelaProdutoDefinirQuantidade
from view.TelaProdutosPorCategoria import TelaProdutosPorCategoria
from datetime import date
from configs.settings import Settings
from utils.exceptions.TelaFechada import TelaFechada
from dao.ProdutoDAO import ProdutoDAO
from dao.CategoriaProdutoDAO import CategoriaProdutoDAO


class ControladorProdutos:
    __instance = None

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela = TelaProduto(self)
        self.__tela_cadastro = TelaProdutoCadastro(self)
        self.__tela_selecao = TelaProdutoSelecao(self)
        self.__tela_produtos_categoria = TelaProdutosPorCategoria(self)
        self.__tela_definir_quantidade = TelaProdutoDefinirQuantidade(self)
        self.__dao = ProdutoDAO()
        self.__dao_cat_produto = CategoriaProdutoDAO()

    def __new__(cls, _):
        if ControladorProdutos.__instance is None:
            ControladorProdutos.__instance = object.__new__(cls)
        return ControladorProdutos.__instance

    @property
    def dao(self) -> ProdutoDAO:
        return self.__dao

    def abre_tela(self):
        while True:
            event, values = self.__tela.abrir_tela(
                self.map_object_to_array(self.__dao.get_all())
            )
            if event == 'exited':
                break
            elif event == 'btn_cadastrar':
                self.__tela.fechar_tela()
                try:
                    self.adicionar()
                except Exception:
                    continue
            elif event == 'btn_deletar':
                self.excluir(values)
                self.__tela.fechar_tela()
            elif event == 'btn_editar':
                self.__tela.fechar_tela()
                self.editar(values)

    def map_object_to_array(self, data):
        return list(map(lambda item: [item.codigo, item.nome, item.qtd_estoque, item.marca, item.preco, item.categoria.nome], data))

    def adicionar(self):
        event, dados_produto = self.__tela_cadastro.abrir_tela(False, None)

        if event == 'criar':
            if len(self.__controlador_sistema.controlador_cat_produto.categorias) == 0:
                dados_produto['categoria'] = \
                    self.__controlador_sistema.controlador_cat_produto.adicionar()
            else:
                try:
                    dados_produto['categoria'] = \
                        self.__controlador_sistema.controlador_cat_produto.buscar(
                            mensagens.get('selecionar_categoria_adicionar_produtos'))
                except TelaFechada:
                    return

            produtos = self.__dao.get_all()
            if len([x for x in produtos if x.nome == dados_produto['nome'] and x.categoria.nome == dados_produto['categoria'].nome and x.marca == dados_produto['marca']]) == 0:
                instancia_produto = Produto(*dados_produto.values())
                dados_produto['categoria'].adicionar_produto(instancia_produto)
                self.__dao_cat_produto.add(dados_produto['categoria'])

                self.__dao.add(instancia_produto)
            else:
                self.__controlador_sistema.mensagem_sistema.warning(
                    mensagens.get('ja_cadastrado'))
        else:
            raise TelaFechada

    def excluir(self, codigo_produto):
        try:
            produto = self.__dao.get(codigo_produto)
            self.__dao.remove(produto)
        except Exception:
            self.__controlador_sistema\
                .mensagem_sistema.error(mensagens.get('erro_excluir'))

    def editar(self, codigo_produto):
        produto = self.__dao.get(codigo_produto)
        print(produto)

        event, dados_produtos = self.__tela_cadastro.abrir_tela(
            True, produto)

        if event == 'exited':
            return
        elif event == 'criar':
            _, qtd_estoque, _, preco, _ = dados_produtos.values()

            produto.qtd_estoque = qtd_estoque
            produto.preco = preco

            self.__dao.add(produto)

    def buscar(self):
        event, index_dos_produtos = self.__tela_selecao.abrir_tela(
            self.map_object_to_array(self.__dao.get_all())
        )

        produtos = self.__dao.get_all()
        if event == 'exited':
            raise TelaFechada
        elif event == 'selecionado':
            return [x for x in produtos if list(produtos).index(x) in index_dos_produtos]

    def definir_quantidade_comprada(self, produtos_selecionados: list):
        return self.__tela_definir_quantidade.abrir_tela(produtos_selecionados)

    def tem_produtos_estoque(self) -> bool:
        tem_produtos_estoque = False
        produtos = self.__dao.get_all()
        for produto in produtos:
            if int(produto.qtd_estoque) > 0:
                tem_produtos_estoque = True
                break
        return tem_produtos_estoque

    def exibir_produtos_por_categoria(self, data):
        while True:
            event, values = self.__tela_produtos_categoria.abrir_tela(
                self.map_object_to_array(data)
            )
            if event == 'exited':
                break
