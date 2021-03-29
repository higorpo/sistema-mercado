import utils.Log as Log
from view.AbstractTela import AbstractTela
from datetime import date


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

        Log.log('Digite o cpf do funcionário a ser cadastrado:')
        dados_funcionario['cpf'] = super().ler_cpf()

        Log.log('Digite o nome do funcionário a ser cadastrado:')
        dados_funcionario['nome'] = super().ler_string()

        Log.log('Digite o email do funcionário a ser cadastrado:')
        dados_funcionario['email'] = super().ler_email()

        Log.log('Digite o telefone (com DDD) do funcionário a ser cadastrado:')
        dados_funcionario['telefone'] = super().ler_telefone()

        Log.log('Digite o salario do funcionário a ser cadastrado:')
        dados_funcionario['salario'] = super().ler_float()

        return dados_funcionario

    def excluir_funcionario(self):
        # Esperar código do Higor
        pass

    def editar_funcionario(self):
        # Esperar código do Higor
        pass

    # Vamos mudar o modo como é listado dps, fiz assim só pra testar, sei q tá feio
    def listar_funcionarios(self, funcionarios):
        Log.clear()
        Log.info('Mostrando funcionários cadastrados:')
        for funcionario in funcionarios:
            Log.log(f'Nome: {funcionario.nome}')
            Log.log(f'CPF: {funcionario.cpf}')
            Log.log(f'Telefone: {funcionario.telefone}')
            Log.log(f'Email: {funcionario.email}')
            Log.log(f'Salário: {funcionario.salario}')
            Log.log(
                f'Data de contratação: {funcionario.data_contratacao}\n ---')
        Log.warning('Pressione enter para continuar')
        input()

    def buscar_funcionario(self):
        # Esperar código do Higor
        pass
