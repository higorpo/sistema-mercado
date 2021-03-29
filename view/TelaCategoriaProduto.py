import utils.Log as Log
from view.AbstractTela import AbstractTela


class TelaCategoriaProduto(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)

    def adicionar(self):
        Log.log('Digite o nome da nova categoria de produto a ser cadastrada:')
        return super().ler_string()

    def listar(self, categorias_produto):
        Log.clear()
        Log.info('Mostrando as categorias de produto cadastradas')
        for categoria_produto in categorias_produto:
            Log.log(
                f'- Código: {categoria_produto.codigo}    |    Método: {categoria_produto.nome}')
        Log.warning('Pressione enter para continuar')
        input()
