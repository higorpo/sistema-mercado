from utils.Terminal import Terminal
from view.AbstractTela import AbstractTela
from messages.FormaPagamento import mensagens
from messages.Sistema import mensagens as mensagens_sistema
from utils.exceptions import NenhumaOpcaoSelecionada


class TelaFormaPagamento(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)

    def adicionar(self):
        print(mensagens.get('label_metodo_pagamento'))
        return super().ler_string()

    def listar(self, formas_pagamento):
        Terminal.clear_all(self)
        print(Terminal.info(self, mensagens.get('mostrando_cadastros')))

        if len(formas_pagamento) == 0:
            print(mensagens.get('nada_cadastrado'))
        else:
            for forma_pagamento in formas_pagamento:
                print(mensagens.get('lista_valores')(forma_pagamento))

        print(Terminal.warning(self, mensagens_sistema.get('enter_continuar')))
        input()

    def buscar(self, formas_pagamento):
        if len(formas_pagamento) == 0:
            print(Terminal.error(
                self,
                mensagens.get('nada_cadastrado_busca')
            ))
            print(Terminal.warning(self, mensagens_sistema.get('enter_continuar')))
            input()
            raise NenhumaOpcaoSelecionada

        return super().encontrar_opcao(formas_pagamento)
