import utils.Log as Log
from controller.AbstractControlador import AbstractControlador
from view.TelaCategoriaProduto import TelaCategoriaProduto
from model.CategoriaProduto import CategoriaProduto


class ControladorCategoriasProduto(AbstractControlador):
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema, TelaCategoriaProduto(self))
        self.__list_cat_produto = []

    def abre_tela(self):
        super().abre_tela('O que você deseja fazer?', [
            'Adicionar nova categoria de produto',
            'Listar categorias de produto',
            'Buscar categorias de produto'
        ], [
            self.adicionar,
            self.listar,
            self.buscar,
        ])

    def adicionar(self):
        categoria_produto = super()._tela.adicionar()
        if len([x for x in self.__list_cat_produto if x.nome == categoria_produto]) == 0:
            self.__list_cat_produto.append(CategoriaProduto(categoria_produto))
        else:
            Log.warning('AVISO: Essa categoria de produto já foi cadastrada!')
            self.adicionar()

    def listar(self):
        super()._tela.listar(self.__list_cat_produto)

    def buscar(self) -> CategoriaProduto:
        super()._tela.buscar(self.__list_cat_produto)

    def pesquisar_opcoes(self, buscar_por: str):
        return list(filter(lambda x: buscar_por in x.nome, self.__list_cat_produto))
