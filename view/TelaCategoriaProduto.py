import time
from utils.Terminal import Terminal
from view.AbstractTela import AbstractTela
from model.CategoriaProduto import CategoriaProduto
from utils.exceptions.NenhumaOpcaoSelecionada import NenhumaOpcaoSelecionada


class TelaCategoriaProduto(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)

    def adicionar(self):
        print('Digite o nome da nova categoria de produto a ser cadastrada:')
        return super().ler_string()

    def listar(self, categorias_produto):
        Terminal.clear_all(self)
        print(Terminal.info(self, 'Mostrando as categorias de produto cadastradas'))

        if len(categorias_produto) == 0:
            print('Não há nada cadastrado para ser listado...')
        else:
            for categoria_produto in categorias_produto:
                print(
                    f'- Código: {categoria_produto.codigo}    |    Categoria: {categoria_produto.nome}')

        print(Terminal.warning(self, 'Pressione enter para continuar'))
        input()

    def buscar(self, categorias_produto) -> CategoriaProduto:
        if len(categorias_produto) == 0:
            print(Terminal.error(
                self,
                'AVISO: Não existe categorias de produto para buscar, cadastre uma primeiro...'
            ))
            print(Terminal.warning(self, 'Pressione enter para continuar'))
            input()
            raise NenhumaOpcaoSelecionada

        return super().encontrar_opcao(categorias_produto)
