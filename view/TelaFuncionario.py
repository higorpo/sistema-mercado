from datetime import date
from model.Funcionario import Funcionario
from utils.Terminal import Terminal
from utils.exceptions import NenhumaOpcaoSelecionada
from view.AbstractTela import AbstractTela
from messages.Funcionarios import mensagens
from messages.Sistema import mensagens as mensagens_sistema


class TelaFuncionario(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)

    def adicionar(self):

        dados_funcionario = {
            'data_atual': date.today().strftime('%d/%m/%Y'),
            'salario': None,
            'nome': None,
            'email': None,
            'telefone': None,
            'cpf': None
        }

        print(mensagens.get('label_cpf'))
        dados_funcionario['cpf'] = super().ler_cpf()

        print(mensagens.get('label_nome'))
        dados_funcionario['nome'] = super().ler_string()

        print(mensagens.get('label_email'))
        dados_funcionario['email'] = super().ler_email()

        print(mensagens.get('label_telefone'))
        dados_funcionario['telefone'] = super().ler_telefone()

        print(mensagens.get('label_salario'))
        dados_funcionario['salario'] = super().ler_float()

        return dados_funcionario

    def editar(self, funcionario: Funcionario):
        dados_funcionario = {
            'salario': funcionario.salario,
            'email': funcionario.email,
            'telefone': funcionario.telefone
        }

        print(mensagens.get('label_email'))
        print(
            Terminal.warning(
                self,
                mensagens.get('label_atualmente')
                (
                    'E-mail', dados_funcionario['email']
                )
            )
        )
        dados_funcionario['email'] = super().ler_email(modo_edicao=True)

        print(mensagens.get('label_telefone'))
        print(
            Terminal.warning(
                self,
                mensagens.get('label_atualmente')
                (
                    'Telefone', dados_funcionario['telefone']
                )
            )
        )
        dados_funcionario['telefone'] = super().ler_telefone(modo_edicao=True)

        print(mensagens.get('label_salario'))
        print(
            Terminal.warning(
                self,
                mensagens.get('label_atualmente')
                (
                    'Salário', dados_funcionario['salario']
                )
            )
        )
        dados_funcionario['salario'] = super().ler_float(modo_edicao=True)

        return dados_funcionario

    def listar(self, funcionarios):
        Terminal.clear_all(self)
        print(Terminal.info(self, mensagens.get('mostrando_cadastros')))
        for funcionario in funcionarios:
            print(mensagens.get('lista_valores')(funcionario))
        print(Terminal.warning(self, mensagens_sistema.get('enter_continuar')))
        input()

    def buscar(self, funcionarios) -> Funcionario:
        if len(funcionarios) == 0:
            print(Terminal.error(
                self,
                mensagens.get('nada_cadastrado_busca')
            ))
            print(Terminal.warning(self, mensagens_sistema.get('enter_continuar')))
            input()
            raise NenhumaOpcaoSelecionada

        return super().encontrar_opcao(funcionarios)
