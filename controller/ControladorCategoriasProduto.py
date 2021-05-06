from controller.AbstractControlador import AbstractControlador
from view.TelaCategoriaProduto import TelaCategoriaProduto
from view.TelaCategoriaProdutoCadastro import TelaCategoriaProdutoCadastro
from model.CategoriaProduto import CategoriaProduto
from messages.CategoriaProduto import mensagens
from messages.Sistema import mensagens as mensagens_sistema
from utils.exceptions.NenhumaOpcaoParaSelecionar import NenhumaOpcaoParaSelecionar


class ControladorCategoriasProduto:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela = TelaCategoriaProduto(self)
        self.__tela_cadastro = TelaCategoriaProdutoCadastro(self)

        self.__list_cat_produto = []

    def abre_tela(self):
        while True:
            event, values = self.__tela.abrir_tela(self.map_object_to_array())
            if event == 'exited':
                break
            elif event == 'btn_cadastrar':
                self.__tela.fechar_tela()
                self.adicionar()

    def map_object_to_array(self):
        return list(map(lambda item: [item.codigo, item.nome, len(item.produtos)], self.__list_cat_produto))

    def adicionar(self) -> CategoriaProduto:
        event, dados_categoria = self.__tela_cadastro.abrir_tela()

        if event == 'criar':
            if len([x for x in self.__list_cat_produto if x.nome == dados_categoria['nome']]) == 0:
                nova_categoria = CategoriaProduto(dados_categoria['nome'])
                self.__list_cat_produto.append(nova_categoria)
                return nova_categoria
            else:
                self.__controlador_sistema.mensagem_sistema.warning(
                    mensagens.get('ja_cadastrado')
                )
                return None
        else:
            return None

    def listar(self):
        self.__tela.listar(self.__list_cat_produto, mensagens)

    def buscar(self, titulo_tela: str) -> CategoriaProduto:
        try:
            return self.__tela.buscar(self.__list_cat_produto, titulo_tela, mensagens)
        except NenhumaOpcaoParaSelecionar:
            self.abre_tela()

    def pesquisar_opcoes(self, buscar_por: str):
        return list(filter(lambda x: buscar_por.lower() in x.nome.lower(), self.__list_cat_produto))

    # TODO: Criar listagem de produtos por categoria...
    def listar_produtos_por_categoria(self):
        categoria_selecionada = \
            self.buscar(mensagens.get('mostrando_cadastros_para_selecionar'))
        try:
            return self.__tela.listar_produtos_por_categoria(categoria_selecionada)
        except AttributeError:
            self._sistema.abre_tela()

    @property
    def categorias(self):
        return self.__list_cat_produto
