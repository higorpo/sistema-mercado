from view.AbstractTela import AbstractTela
from messages.Cliente import mensagens
from utils.Terminal import Terminal
from messages.Cliente import mensagens
from messages.Sistema import mensagens as mensagens_sistema
from utils.exceptions.NenhumaOpcaoParaSelecionar import NenhumaOpcaoParaSelecionar


class TelaCliente(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)

    def cadastar(self):
        dados_cliente = {
            'vip': None,
            'nome': None,
            'email': None,
            'telefone': None,
            'cpf': None
        }

        print(mensagens.get('label_cpf'))
        dados_cliente['cpf'] = super().ler_cpf()

        print(mensagens.get('label_nome'))
        dados_cliente['nome'] = super().ler_string()

        print(mensagens.get('label_email'))
        dados_cliente['email'] = super().ler_email()

        print(mensagens.get('label_telefone'))
        dados_cliente['telefone'] = super().ler_telefone()

        print(mensagens.get('label_vip'))
        dados_cliente['vip'] = super().ler_vip()

        return dados_cliente

    def editar(self, cliente):
        dados_cliente = {
            'vip': cliente.vip,
            'email': cliente.email,
            'telefone': cliente.telefone
        }

        print(mensagens.get('label_vip'))
        print(
            Terminal.warning(
                self,
                mensagens_sistema.get('label_atualmente')
                (
                    'VIP', dados_cliente['vip']
                )
            )
        )

        dados_cliente['vip'] = super().ler_vip(modo_edicao=True)

        print(mensagens.get('label_email'))
        print(
            Terminal.warning(
                self,
                mensagens_sistema.get('label_atualmente')
                (
                    'E-mail', dados_cliente['email']
                )
            )
        )

        dados_cliente['email'] = super().ler_email(modo_edicao=True)

        print(mensagens.get('label_telefone'))
        print(
            Terminal.warning(
                self,
                mensagens_sistema.get('label_atualmente')
                (
                    'Telefone', dados_cliente['telefone']
                )
            )
        )

        dados_cliente['telefone'] = super().ler_telefone(modo_edicao=True)

        return dados_cliente
