from controller.AbstractControlador import AbstractControlador
from model.Funcionario import Funcionario
from view.TelaFuncionario import TelaFuncionario
from view.TelaEndereco import TelaEndereco
from messages.Funcionarios import mensagens
from messages.Sistema import mensagens as mensagens_sistema
from utils.faker.Funcionario import fakeFuncionario
import time


class ControladorFuncionarios(AbstractControlador):
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema, TelaFuncionario(self))
        self.__funcionarios = [
            fakeFuncionario
        ]
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
            self.__funcionarios.append(instancia_funcionario)
        else:
            super()._sistema.mensagem_sistema.warning(mensagens.get('ja_cadastrado'))
            self.adicionar()

        dados_endereco = self.__tela_endereco.adicionar()
        instancia_funcionario.definir_endereco(*dados_endereco.values())

    def excluir(self):
        if self.__verifica_tem_dados():
            try:
                funcionario = self.buscar()
                self.__funcionarios.remove(funcionario)
            except Exception:
                super()._sistema.mensagem_sistema.error(mensagens.get('erro_excluir'))

    def editar(self):
        if self.__verifica_tem_dados():
            funcionario = self.buscar()
            dados_funcionarios = super()._tela.editar(funcionario)

            email = dados_funcionarios['email']
            telefone = dados_funcionarios['telefone']
            salario = dados_funcionarios['salario']

            funcionario.email = email if email != '--' else funcionario.email
            funcionario.telefone = telefone if telefone != '--' else funcionario.telefone
            funcionario.salario = salario if salario != '--' else funcionario.salario

    def listar(self):
        super()._tela.listar(self.__funcionarios)

    def buscar(self) -> Funcionario:
        return super()._tela.buscar(self.__funcionarios)

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
