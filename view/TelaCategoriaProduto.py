import utils.Log as Log
from view.AbstractTela import AbstractTela
from model.CategoriaProduto import CategoriaProduto
from utils.exceptions.NenhumaOpcaoSelecionada import NenhumaOpcaoSelecionada
import time


class TelaCategoriaProduto(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)

    def adicionar(self):
        Log.log('Digite o nome da nova categoria de produto a ser cadastrada:')
        return super().ler_string()

    def listar(self, categorias_produto):
        Log.clear()
        Log.info('Mostrando as categorias de produto cadastradas')

        if len(categorias_produto) == 0:
            Log.log('Não há nada cadastrado para ser listado...')
        else:
            for categoria_produto in categorias_produto:
                Log.log(
                    f'- Código: {categoria_produto.codigo}    |    Categoria: {categoria_produto.nome}')

        Log.warning('Pressione enter para continuar')
        input()

    def buscar(self, categorias_produto) -> CategoriaProduto:
        if len(categorias_produto) == 0:
            Log.error(
                'AVISO: Não existe categorias de produto para buscar, cadastre uma primeiro...')
            Log.warning('Pressione enter para continuar')
            input()
            raise NenhumaOpcaoSelecionada

        return super().encontrar_opcao(categorias_produto)
