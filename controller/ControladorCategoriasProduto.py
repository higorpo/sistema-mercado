from controller.AbstractControlador import AbstractControlador
from view.TelaCategoriaProduto import TelaCategoriaProduto
from model.CategoriaProduto import CategoriaProduto
from messages.CategoriaProduto import mensagens
from messages.Sistema import mensagens as mensagens_sistema
from utils.exceptions.NenhumaOpcaoParaSelecionar import NenhumaOpcaoParaSelecionar


class ControladorCategoriasProduto(AbstractControlador):
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema, TelaCategoriaProduto(self))
        self.__list_cat_produto = []

    def abre_tela(self):
        super().abre_tela(mensagens_sistema.get('titulo_tela_opcoes'), [
            mensagens.get('adicionar'),
            mensagens.get('listar'),
            mensagens.get('listar_produtos_por_categoria')
        ], [
            self.adicionar,
            self.listar,
            self.listar_produtos_por_categoria
        ])

    def adicionar(self) -> CategoriaProduto:
        categoria_produto = super()._tela.adicionar()
        if len([x for x in self.__list_cat_produto if x.nome == categoria_produto]) == 0:
            nova_categoria = CategoriaProduto(categoria_produto)
            self.__list_cat_produto.append(nova_categoria)
            return nova_categoria
        else:
            super()._sistema.mensagem_sistema.warning(
                mensagens.get('ja_cadastrado')
            )
            self.adicionar()

    def listar(self):
        super()._tela.listar(self.__list_cat_produto, mensagens)

    def buscar(self, titulo_tela: str) -> CategoriaProduto:
        try:
            return super()._tela.buscar(self.__list_cat_produto, titulo_tela, mensagens)
        except NenhumaOpcaoParaSelecionar:
            self.abre_tela()

    def pesquisar_opcoes(self, buscar_por: str):
        return list(filter(lambda x: buscar_por.lower() in x.nome.lower(), self.__list_cat_produto))

    # TODO coloquei um try/except aqui pq como eu tô passando um obj q pode n estar instanciado ele vai ser passado como None
    def listar_produtos_por_categoria(self):
        categoria_selecionada = \
            self.buscar(mensagens.get('mostrando_cadastros_para_selecionar'))
        try:
            return super()._tela.listar_produtos_por_categoria(categoria_selecionada)
        except AttributeError:
            self._sistema.abre_tela()

    @property
    def categorias(self):
        return self.__list_cat_produto
