from controller.AbstractControlador import AbstractControlador
from model.Funcionario import Funcionario
from view.TelaFuncionario import TelaFuncionario
from view.TelaFuncionarioCadastro import TelaFuncionarioCadastro
from view.TelaEndereco import TelaEndereco
from messages.Funcionarios import mensagens
from messages.Sistema import mensagens as mensagens_sistema
from utils.faker.Funcionario import fakeFuncionario
from utils.exceptions.NenhumaOpcaoSelecionada import NenhumaOpcaoSelecionada
from configs.settings import Settings
import time


class ControladorFuncionarios(AbstractControlador):
    def __init__(self, controlador_sistema):
        super().__init__(
            controlador_sistema,
            TelaFuncionario(self),
            TelaFuncionarioCadastro(self)
        )
        self.__funcionarios = \
            [fakeFuncionario] if Settings.INICIAR_SISTEMA_COM_DADOS_FAKES else []
        self.__tela_endereco = TelaEndereco(self)

    def abre_tela(self):
        while True:
            event, values = super()._tela.abrir_tela(self.map_object_to_array())
            if event == 'exited':
                break
            elif event == 'btn_cadastrar':
                super()._tela.fechar_tela()
                self.adicionar()
            elif event == 'btn_deletar':
                self.excluir(values)
                super()._tela.fechar_tela()
            elif event == 'btn_editar':
                super()._tela.fechar_tela()
                self.editar(values)

    def map_object_to_array(self):
        return list(map(lambda item: [item.codigo, item.nome, item.email, item.telefone, item.cpf, item.endereco], self.__funcionarios))

    def adicionar(self):
        event, dados_funcionario = super()._tela_cadastro.abrir_tela(False, None)

        if event == 'criar':
            if len([x for x in self.__funcionarios if x.cpf == dados_funcionario['cpf']]) == 0:
                instancia_funcionario = Funcionario(
                    *dados_funcionario.values())
                event, dados_endereco = self.__tela_endereco.abrir_tela()

                if event == 'exited':
                    return
                elif event == 'criar':
                    instancia_funcionario.definir_endereco(
                        *dados_endereco.values()
                    )
                    self.__funcionarios.append(instancia_funcionario)
            else:
                super()._sistema.mensagem_sistema.warning(mensagens.get('ja_cadastrado'))

    def excluir(self, funcionarioIndex):
        try:
            self.__funcionarios.remove(self.__funcionarios[funcionarioIndex])
        except Exception:
            super()._sistema.mensagem_sistema.error(mensagens.get('erro_excluir'))

    def editar(self, funcionarioIndex):
        try:
            funcionario = self.__funcionarios[funcionarioIndex]

            event, dados_funcionarios = super()._tela_cadastro.abrir_tela(True, funcionario)

            if event == 'exited':
                return
            elif event == 'criar':
                _, salario, _, email, telefone, _ = dados_funcionarios.values()

                funcionario.salario = salario
                funcionario.email = email
                funcionario.telefone = telefone

        except NenhumaOpcaoSelecionada:
            super()._sistema.mensagem_sistema.warning(
                mensagens_sistema.get('nenhuma_opcao_selecionada')
            )

    # TODO: Remover no futuro
    def listar(self):
        super()._tela.listar(self.__funcionarios, mensagens)

    # TODO: Remover no futuro

    def buscar(self, titulo_tela: str = mensagens.get('titulo_tela_buscar')) -> Funcionario:
        return super()._tela.buscar(self.__funcionarios, titulo_tela, mensagens)

    # TODO: Remover no futuro

    def pesquisar_opcoes(self, buscar_por: str):
        return list(filter(lambda x: buscar_por.lower() in x.nome.lower(), self.__funcionarios))

    @property
    def funcionarios(self):
        return self.__funcionarios
