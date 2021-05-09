from view.TelaCategoriaProduto import TelaCategoriaProduto
from view.TelaCategoriaProdutoCadastro import TelaCategoriaProdutoCadastro
from view.TelaCategoriaProdutoSelecao import TelaCategoriaProdutoSelecao
from model.CategoriaProduto import CategoriaProduto
from messages.CategoriaProduto import mensagens
from messages.Sistema import mensagens as mensagens_sistema
from utils.exceptions.TelaFechada import TelaFechada
from dao.CategoriaProdutoDAO import CategoriaProdutoDAO

# TODO: Adicionar lista de fornecedores para cada categoria se der tempo..


class ControladorCategoriasProduto:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela = TelaCategoriaProduto(self)
        self.__tela_cadastro = TelaCategoriaProdutoCadastro(self)
        self.__tela_selecao = TelaCategoriaProdutoSelecao(self)
        self.__dao = CategoriaProdutoDAO()

    @property
    def dao(self) -> CategoriaProdutoDAO:
        return self.__dao

    def abre_tela(self):
        while True:
            event, values = self.__tela.abrir_tela(self.map_object_to_array())
            if event == 'exited':
                break
            elif event == 'btn_cadastrar':
                self.__tela.fechar_tela()
                try:
                    self.adicionar()
                except Exception:
                    continue

    def map_object_to_array(self):
        return list(map(lambda item: [item.codigo, item.nome, len(item.produtos)], self.__dao.get_all()))

    def adicionar(self) -> CategoriaProduto:
        event, dados_categoria = self.__tela_cadastro.abrir_tela()

        if event == 'criar':
            categorias = self.__dao.get_all()
            if len([x for x in categorias if x.nome == dados_categoria['nome']]) == 0:
                nova_categoria = CategoriaProduto(dados_categoria['nome'])
                self.__dao.add(nova_categoria)
                return nova_categoria
            else:
                self.__controlador_sistema.mensagem_sistema.warning(
                    mensagens.get('ja_cadastrado')
                )
                raise Exception
        else:
            raise TelaFechada

    def buscar(self, titulo_tela: str) -> CategoriaProduto:
        event, codigoCategoria = self.__tela_selecao.abrir_tela(
            self.map_object_to_array()
        )

        if event == 'exited':
            raise TelaFechada
        elif event == 'selecionado':
            return self.__dao.get(codigoCategoria)

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
        return self.__dao.get_all()
