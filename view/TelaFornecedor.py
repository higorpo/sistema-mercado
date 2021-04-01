from view.AbstractTela import AbstractTela
from utils.exceptions import NenhumaOpcaoSelecionada
from utils.Terminal import Terminal
from messages.Sistema import mensagens as mensagens_sistema
from messages.Fornecedor import mensagens


class TelaFornecedor(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)

    def adicionar(self):

        dados_fornecedor = {
            'nome': None,
            'cnpj': None,
            'email': None,
            'telefone': None,
            'fornece': None
        }

        print(mensagens.get('label_cnpj'))
        dados_fornecedor['cnpj'] = super().ler_cnpj()

        print(mensagens.get('label_nome'))
        dados_fornecedor['nome'] = super().ler_string()

        print(mensagens.get('label_email'))
        dados_fornecedor['email'] = super().ler_email()

        return dados_fornecedor

    def editar(self, fornecedor):
        dados_fornecedor = {
            'email': fornecedor.email,
            'telefone': fornecedor.telefone
        }

        print(mensagens.get('label_email'))
        print(Terminal.warning(self, mensagens.get(
            'label_atualmente')('Email', dados_fornecedor['email'])))

        dados_fornecedor['email'] = super().ler_email(modo_edicao=True)

        print(mensagens.get('label_telefone'))
        print(Terminal.warning(self, mensagens.get('label_atualmente')
                               ('Telefone', dados_fornecedor['telefone'])))

        dados_fornecedor['telefone'] = super().ler_telefone(modo_edicao=True)

        return dados_fornecedor

    def listar(self, fornecedores):
        Terminal.clear_all(self)
        print(Terminal.info(self, mensagens.get('mostrando_cadastros')))
        for fornecedor in fornecedores:
            print(mensagens.get('lista_valores')(fornecedor))
        print(Terminal.warning(self, mensagens_sistema.get('enter_continuar')))
        input()

    def buscar(self, fornecedores):
        if len(fornecedores) == 0:
            print(Terminal.error(self, mensagens.get('nada_cadastrado_busca')))
            print(Terminal.warning(self, mensagens_sistema.get('enter_continuar')))
            input()
            raise NenhumaOpcaoSelecionada

        return super().encontrar_opcao(fornecedores)
