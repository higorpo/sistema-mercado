from view.AbstractTela import AbstractTela
from utils.Terminal import Terminal
from messages.Endereco import mensagens


class TelaEndereco(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)

    def adicionar(self):
        Terminal.clear_all(self)
        dados_endereco = {
            'rua': None,
            'cidade': None,
            'estado': None,
            'cep': None,
            'complemento': None
        }

        print(Terminal.info(self, mensagens.get('titulo_cadastro')))
        print(mensagens.get('label_rua'))
        dados_endereco['rua'] = super().ler_string()

        print(mensagens.get('label_cidade'))
        dados_endereco['cidade'] = super().ler_string()

        print(mensagens.get('label_estado'))
        dados_endereco['estado'] = super().ler_string()

        print(mensagens.get('label_cep'))
        dados_endereco['cep'] = super().ler_cep()

        print(mensagens.get('label_complemento'))
        dados_endereco['complemento'] = super().ler_string()

        return dados_endereco
