from model.Cliente import Cliente
from view.TelaCliente import TelaCliente
from view.TelaClienteCadastro import TelaClienteCadastro
from messages.Sistema import mensagens as mensagens_sistema
from messages.Cliente import mensagens
from view.TelaEndereco import TelaEndereco
from utils.faker.Cliente import fakeClientes
from configs.settings import Settings
from utils.exceptions.NenhumaOpcaoParaSelecionar import NenhumaOpcaoParaSelecionar


class ControladorClientes:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela = TelaCliente(self)
        self.__tela_cadastro = TelaClienteCadastro(self)

        self.__clientes = \
            [*fakeClientes] if Settings.INICIAR_SISTEMA_COM_DADOS_FAKES else []
        self.__tela_endereco = TelaEndereco(self)

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
        return list(map(lambda item: [item.nome, item.email, item.telefone, item.cpf, item.endereco, item.vip], self.__clientes))

    def adicionar(self):
        event, dados_cliente = self.__tela_cadastro.abrir_tela(False, None)

        if event == 'criar':
            if len([x for x in self.__clientes if x.cpf == dados_cliente['cpf']]) == 0:
                instancia_cliente = Cliente(*dados_cliente.values())
                event, dados_endereco = self.__tela_endereco.abrir_tela()

                if event == 'exited':
                    return
                elif event == 'criar':
                    instancia_cliente.definir_endereco(
                        *dados_endereco.values())
                    self.__clientes.append(instancia_cliente)
            else:
                self.__controlador_sistema\
                    .mensagem_sistema.warning(mensagens.get('ja_cadastrado'))

    def excluir(self, clienteIndex):
        try:
            self.__clientes.remove(self.__clientes[clienteIndex])
        except Exception:
            self.__controlador_sistema\
                .mensagem_sistema.error(mensagens.get('erro_excluir'))

    def editar(self, clienteIndex):
        try:
            cliente = self.__clientes[clienteIndex]

            event, dados_clientes = self.__tela_cadastro.abrir_tela(
                True, cliente)

            if event == 'exited':
                return
            elif event == 'criar':
                vip, _, email, telefone, _ = dados_clientes.values()

                cliente.email = email
                cliente.telefone = telefone
                cliente.vip = vip

        except NenhumaOpcaoSelecionada:
            self.__controlador_sistema\
                .mensagem_sistema.warning(mensagens_sistema.get('nenhuma_opcao_selecionada'))

    # TODO: Remover no futuro
    def listar(self):
        super()._tela.listar(self.__clientes, mensagens)

    # TODO: Remover no futuro
    def buscar(self, titulo_tela: str = mensagens.get('titulo_tela_buscar')):
        try:
            return super()._tela.buscar(self.__clientes, titulo_tela, mensagens)
        except NenhumaOpcaoParaSelecionar:
            self.abre_tela()

    # TODO: Remover no futuro
    def pesquisar_opcoes(self, buscar_por: str):
        return list(filter(lambda x: buscar_por.lower() in x.nome.lower(), self.__clientes))

    # TODO: Remover no futuro
    def __verifica_tem_dados(self) -> bool:
        if len(self.__clientes) == 0:
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

    # TODO: Implementar no futuro
    def listar_compras(self):
        if self.__verifica_tem_dados():
            cliente = self.buscar()
            return super()._tela.listar_compras(cliente.pedidos)

    @ property
    def clientes(self):
        return self.__clientes
