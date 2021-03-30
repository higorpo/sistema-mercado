from controller.AbstractControlador import AbstractControlador
from model.Funcionario import Funcionario
from view.TelaFuncionario import TelaFuncionario
from messages.Funcionarios import mensagens
from messages.Sistema import mensagens as mensagens_sistema


class ControladorFuncionarios(AbstractControlador):
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema, TelaFuncionario(self))
        self.__funcionarios = []

    def abre_tela(self):
        super().abre_tela(mensagens_sistema.get('titulo_tela_opcoes'), [
            mensagens.get('cadastrar'),
            mensagens.get('excluir'),
            mensagens.get('editar'),
            mensagens.get('listar'),
            mensagens.get('buscar')
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
            super()._sistema.mensagem_sistema.warning(mensagens.get('ja_cadastrado'))
            self.adicionar_funcionarios()

    def excluir_funcionario(self):
        funcionario_para_excluir = super()._tela.excluir_funcionario(self.__funcionarios)
        self.__funcionarios.remove(funcionario_para_excluir)

    def editar_funcionario(self):
        # Esperar código do HIgor
        pass

    def listar_funcionarios(self):
        super()._tela.listar_funcionarios(self.__funcionarios)

    def buscar_funcionario(self):
        # Esperar código do Higor
        pass

    def pesquisar_opcoes(self, buscar_por: str):
        return list(filter(lambda x: buscar_por.lower() in x.nome.lower(), self.__funcionarios))
