import utils.Log as Log
from controller.AbstractControlador import AbstractControlador
from model.Funcionario import Funcionario
from view.TelaFuncionario import TelaFuncionario


class ControladorFuncionarios(AbstractControlador):
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema, TelaFuncionario(self))
        self.__funcionarios = []

    def abre_tela(self):
        super().abre_tela('O que você deseja fazer?', [
            'Cadastrar novo funcionário',
            'Excluir funcionário',
            'Editar funcionário',
            'Listar funcionários',
            'Buscar funcionário'
        ], [
            self.adicionar_funcionarios,
            self.excluir_funcionario,
            self.editar_funcionario,
            self.listar_funcionarios,
            self.buscar_funcionario
        ])

    def adicionar_funcionarios(self):
        dados_funcionario = super()._tela.adicionar_funcionarios()
        if len([x for x in self.__funcionarios if x.cpf == dados_funcionario['cpf']]) == 0:
            self.__funcionarios.append(
                Funcionario(*dados_funcionario.values()))
        else:
            # TODO: Remover os prints da tela
            Log.warning(
                'AVISO: Um funcionário com este CPF já foi cadastrado!')
            self.adicionar_funcionarios()

    def excluir_funcionario(self):
        # Esperar código do Higor
        pass

    def editar_funcionario(self):
        # Esperar código do HIgor
        pass

    def listar_funcionarios(self):
        super()._tela.listar_funcionarios(self.__funcionarios)

    def buscar_funcionario(self):
        # Esperar código do Higor
        pass
