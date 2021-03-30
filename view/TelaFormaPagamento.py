from utils.Terminal import Terminal
from view.AbstractTela import AbstractTela


class TelaFormaPagamento(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)

    def adicionar(self):
        print('Digite o nome da nova forma de pagamento a ser cadastrada:')
        return super().ler_string()

    def listar(self, formas_pagamento):
        Terminal.clear_all(self)
        print(Terminal.info(self, 'Mostrando formas de pagamento cadastradas'))

        if len(formas_pagamento) == 0:
            print('Não há nada cadastrado para ser listado...')
        else:
            for forma_pagamento in formas_pagamento:
                print(
                    f'- Código: {forma_pagamento.codigo}    |    Método: {forma_pagamento.metodo}')

        print(Terminal.warning(self, 'Pressione enter para continuar'))
        input()
