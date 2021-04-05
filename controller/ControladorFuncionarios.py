from controller.AbstractControlador import AbstractControlador
from model.Funcionario import Funcionario
from view.TelaFuncionario import TelaFuncionario
from view.TelaEndereco import TelaEndereco
from messages.Funcionarios import mensagens
from messages.Sistema import mensagens as mensagens_sistema
from utils.faker.Funcionario import fakeFuncionario
from utils.exceptions.NenhumaOpcaoSelecionada import NenhumaOpcaoSelecionada
from configs.settings import Settings
import time


class ControladorFuncionarios(AbstractControlador):
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema, TelaFuncionario(self))
        self.__funcionarios = \
            [fakeFuncionario] if Settings.INICIAR_SISTEMA_COM_DADOS_FAKES else []
        self.__tela_endereco = TelaEndereco(self)

    def abre_tela(self):
        super().abre_tela(mensagens_sistema.get('titulo_tela_opcoes'), [
            mensagens.get('cadastrar'),
            mensagens.get('excluir'),
            mensagens.get('editar'),
            mensagens.get('listar')
        ], [
            self.adicionar,
            self.excluir,
            self.editar,
            self.listar
        ])

    def adicionar(self):
        dados_funcionario = super()._tela.adicionar()

        if len([x for x in self.__funcionarios if x.cpf == dados_funcionario['cpf']]) == 0:
            instancia_funcionario = Funcionario(*dados_funcionario.values())
            dados_endereco = self.__tela_endereco.adicionar()
            instancia_funcionario.definir_endereco(*dados_endereco.values())
            self.__funcionarios.append(instancia_funcionario)
        else:
            super()._sistema.mensagem_sistema.warning(mensagens.get('ja_cadastrado'))
            self.adicionar()

    def excluir(self):
        if self.__verifica_tem_dados():
            try:
                funcionario = self.buscar(mensagens.get('titulo_tela_excluir'))
                self.__funcionarios.remove(funcionario)
            except Exception:
                super()._sistema.mensagem_sistema.error(mensagens.get('erro_excluir'))

    def editar(self):
        if self.__verifica_tem_dados():
            try:
                funcionario = self.buscar(mensagens.get('titulo_tela_editar'))

                dados_funcionarios = super()._tela.editar(funcionario)

                salario, email, telefone = dados_funcionarios.values()

                funcionario.salario = salario if salario != '--' else funcionario.salario
                funcionario.email = email if email != '--' else funcionario.email
                funcionario.telefone = telefone if telefone != '--' else funcionario.telefone
            except NenhumaOpcaoSelecionada:
                super()._sistema.mensagem_sistema.warning(
                    mensagens_sistema.get('nenhuma_opcao_selecionada'))
                self.editar()

    def listar(self):
        super()._tela.listar(self.__funcionarios)

    def buscar(self, titulo_tela: str = mensagens.get('titulo_tela_buscar')) -> Funcionario:
        return super()._tela.buscar(self.__funcionarios, titulo_tela)

    def pesquisar_opcoes(self, buscar_por: str):
        return list(filter(lambda x: buscar_por.lower() in x.nome.lower(), self.__funcionarios))

    def __verifica_tem_dados(self) -> bool:
        if len(self.__funcionarios) == 0:
            super()._sistema.mensagem_sistema.log(
                mensagens.get('nada_cadastrado_busca')
            )
            super()._sistema.mensagem_sistema.warning(
                mensagens_sistema.get('enter_continuar')
            )
            input()
            return False
        else:
            return True

    @property
    def funcionarios(self):
        return self.__funcionarios
