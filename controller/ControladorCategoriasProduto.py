from controller.AbstractControlador import AbstractControlador
from view.TelaCategoriaProduto import TelaCategoriaProduto
from model.CategoriaProduto import CategoriaProduto
from messages.CategoriaProduto import mensagens
from messages.Sistema import mensagens as mensagens_sistema


class ControladorCategoriasProduto(AbstractControlador):
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema, TelaCategoriaProduto(self))
        self.__list_cat_produto = []

    def abre_tela(self):
        super().abre_tela(mensagens_sistema.get('titulo_tela_opcoes'), [
            mensagens.get('adicionar'),
            mensagens.get('listar')
        ], [
            self.adicionar,
            self.listar
        ])

    def adicionar(self):
        categoria_produto = super()._tela.adicionar()
        if len([x for x in self.__list_cat_produto if x.nome == categoria_produto]) == 0:
            self.__list_cat_produto.append(CategoriaProduto(categoria_produto))
        else:
            super()._sistema.mensagem_sistema.warning(
                mensagens.get('ja_cadastrado')
            )
            self.adicionar()

    def listar(self):
        super()._tela.listar(self.__list_cat_produto)

    def buscar(self) -> CategoriaProduto:
        return super()._tela.buscar(self.__list_cat_produto)

    def pesquisar_opcoes(self, buscar_por: str):
        return list(filter(lambda x: buscar_por.lower() in x.nome.lower(), self.__list_cat_produto))
