from utils.exceptions.TelaFechada import TelaFechada
from model.Funcionario import Funcionario
from messages.Funcionarios import mensagens
from view.TelaFuncionario import TelaFuncionario
from view.TelaFuncionarioCadastro import TelaFuncionarioCadastro
from view.TelaFuncionarioSelecao import TelaFuncionarioSelecao
from view.TelaEndereco import TelaEndereco
from dao.FuncionarioDAO import FuncionarioDAO


class ControladorFuncionarios:
    __instance = None

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela = TelaFuncionario(self)
        self.__tela_cadastro = TelaFuncionarioCadastro(self)
        self.__tela_selecao = TelaFuncionarioSelecao(self)
        self.__dao = FuncionarioDAO()

        self.__tela_endereco = TelaEndereco(self)

    def __new__(cls, _):
        if ControladorFuncionarios.__instance is None:
            ControladorFuncionarios.__instance = object.__new__(cls)
        return ControladorFuncionarios.__instance

    @property
    def dao(self) -> FuncionarioDAO:
        return self.__dao

    def abre_tela(self):
        while True:
            event, values = self.__tela.abrir_tela(self.map_object_to_array())
            if event == 'exited':
                break
            elif event == 'btn_cadastrar':
                self.__tela.fechar_tela()
                self.adicionar()
            elif event == 'btn_deletar':
                self.excluir(values)
                self.__tela.fechar_tela()
            elif event == 'btn_editar':
                self.__tela.fechar_tela()
                self.editar(values)

    def map_object_to_array(self):
        return list(map(lambda item: [item.codigo, item.nome, item.email, item.telefone, item.cpf, item.endereco], self.__dao.get_all()))

    def adicionar(self):
        event, dados_funcionario = self.__tela_cadastro.abrir_tela(False, None)

        if event == 'criar':
            funcionarios = self.__dao.get_all()
            if len([x for x in funcionarios if x.cpf == dados_funcionario['cpf']]) == 0:
                instancia_funcionario = Funcionario(
                    *dados_funcionario.values())
                event, dados_endereco = self.__tela_endereco.abrir_tela()

                if event == 'exited':
                    return
                elif event == 'criar':
                    instancia_funcionario.definir_endereco(
                        *dados_endereco.values()
                    )
                    self.__dao.add(instancia_funcionario)
                    return instancia_funcionario
            else:
                self.__controlador_sistema\
                    .mensagem_sistema.warning(mensagens.get('ja_cadastrado'))

    def excluir(self, codigo_funcionario):
        try:
            funcionario = self.__dao.get(codigo_funcionario)
            self.__dao.remove(funcionario)
        except Exception:
            self.__controlador_sistema\
                .mensagem_sistema.error(mensagens.get('erro_excluir'))

    def editar(self, codigo_funcionario):
        funcionario = self.__dao.get(codigo_funcionario)

        event, dados_funcionarios = self.__tela_cadastro.abrir_tela(
            True, funcionario
        )

        if event == 'exited':
            return
        elif event == 'criar':
            _, salario, _, email, telefone, _ = dados_funcionarios.values()

            funcionario.salario = salario
            funcionario.email = email
            funcionario.telefone = telefone

            self.__dao.add(funcionario)

    def buscar(self) -> Funcionario:
        event, key = self.__tela_selecao.abrir_tela(
            self.map_object_to_array()
        )

        if event == 'exited':
            raise TelaFechada
        elif event == 'selecionado':
            return self.__dao.get(key)

    @property
    def funcionarios(self):
        return self.__dao.get_all()
