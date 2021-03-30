from datetime import date
from utils.Terminal import Terminal
from utils.exceptions import NenhumaOpcaoSelecionada
from view.AbstractTela import AbstractTela


class TelaFuncionario(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)

    def adicionar_funcionarios(self):

        dados_funcionario = {
            'data_atual': date.today().strftime("%d/%m/%Y"),
            'salario': None,
            'nome': None,
            'email': None,
            'telefone': None,
            'cpf': None
        }

        print('Digite o cpf do funcionário a ser cadastrado:')
        dados_funcionario['cpf'] = super().ler_cpf()

        print('Digite o nome do funcionário a ser cadastrado:')
        dados_funcionario['nome'] = super().ler_string()

        print('Digite o email do funcionário a ser cadastrado:')
        dados_funcionario['email'] = super().ler_email()

        print('Digite o telefone (com DDD) do funcionário a ser cadastrado:')
        dados_funcionario['telefone'] = super().ler_telefone()

        print('Digite o salario do funcionário a ser cadastrado:')
        dados_funcionario['salario'] = super().ler_float()

        return dados_funcionario

    def excluir_funcionario(self, funcionarios):
        if len(funcionarios) == 0:
            print(Terminal.error(
                self,
                'AVISO: Não há nenhum funcionário para excluir, cadastre um primeiro...'
            ))
            print(Terminal.warning(self, 'Pressione enter para continuar'))
            input()

        return super().encontrar_opcao(funcionarios)

    def editar_funcionario(self):
        # Esperar código do Higor
        pass

    # Vamos mudar o modo como é listado dps, fiz assim só pra testar, sei q tá feio
    def listar_funcionarios(self, funcionarios):
        Terminal.clear_all(self)
        print(Terminal.info(self, 'Mostrando funcionários cadastrados:'))
        for funcionario in funcionarios:
            print(f'Nome: {funcionario.nome}')
            print(f'CPF: {funcionario.cpf}')
            print(f'Telefone: {funcionario.telefone}')
            print(f'Email: {funcionario.email}')
            print(f'Salário: {funcionario.salario}')
            print(
                f'Data de contratação: {funcionario.data_contratacao}\n ---')
        print(Terminal.warning(self, 'Pressione enter para continuar'))
        input()

    def buscar_funcionario(self):
        # Esperar código do Higor
        pass
