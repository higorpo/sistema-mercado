from controller.AbstractControlador import AbstractControlador
from model.Cliente import Cliente
from view.TelaCliente import TelaCliente
from messages.Sistema import mensagens as mensagens_sistema
from messages.Cliente import mensagens
from view.TelaEndereco import TelaEndereco
from utils.faker.Cliente import fakeClientes
from configs.settings import Settings
from utils.exceptions.NenhumaOpcaoParaSelecionar import NenhumaOpcaoParaSelecionar
from utils.exceptions.NadaParaListar import NadaParaListar


class ControladorClientes(AbstractControlador):
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema, TelaCliente(self))
        self.__clientes = \
            [*fakeClientes] if Settings.INICIAR_SISTEMA_COM_DADOS_FAKES else []
        self.__tela_endereco = TelaEndereco(self)

    def abre_tela(self):
        super().abre_tela(mensagens_sistema.get('titulo_opcoes'), [
            mensagens.get('cadastrar'),
            mensagens.get('excluir'),
            mensagens.get('editar'),
            mensagens.get('listar'),
            mensagens.get('listar_compras')
        ], [
            self.cadastrar,
            self.excluir,
            self.editar,
            self.listar,
            self.listar_compras
        ])

    def cadastrar(self):
        dados_cliente = super()._tela.cadastar()

        if len([x for x in self.__clientes if x.cpf == dados_cliente['cpf']]) == 0:
            instancia_cliente = Cliente(*dados_cliente.values())
            dados_endereco = self.__tela_endereco.adicionar()
            instancia_cliente.definir_endereco(*dados_endereco.values())
            self.__clientes.append(instancia_cliente)
            return instancia_cliente
        else:
            super()._sistema.mensagem_sistema.warning(mensagens.get('ja_cadastrado'))
            self.cadastrar()

    def excluir(self):
        if self.__verifica_tem_dados():
            try:
                cliente = self.buscar(
                    mensagens.get('titulo_tela_excluir')
                )
                self.__clientes.remove(cliente)
            except Exception:
                super()._sistema.mensagem_sistema.error(mensagens.get('erro_excluir'))

    def editar(self):
        if self.__verifica_tem_dados():
            try:
                cliente = self.buscar(mensagens.get('titulo_tela_editar'))
                dados_cliente = self._tela.editar(cliente)

                vip, email, telefone = dados_cliente.values()

                cliente.vip = vip if vip != '--' else cliente.vip
                cliente.email = email if email != '--' else cliente.email
                cliente.telefone = telefone if telefone != '--' else cliente.telefone
            except Exception:
                super()._sistema.mensagem_sistema.warning(
                    mensagens_sistema.get('nenhuma_opcao_selecionada'))
                self.editar()

    def listar(self):
        super()._tela.listar(self.__clientes, mensagens)

    def buscar(self, titulo_tela: str = mensagens.get('titulo_tela_buscar')):
        try:
            return super()._tela.buscar(self.__clientes, titulo_tela, mensagens)
        except NenhumaOpcaoParaSelecionar:
            self.abre_tela()

    def pesquisar_opcoes(self, buscar_por: str):
        return list(filter(lambda x: buscar_por.lower() in x.nome.lower(), self.__clientes))

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

    def listar_compras(self):
        if self.__verifica_tem_dados():
            try:
                cliente = self.buscar()
                return super()._tela.listar_compras(cliente.pedidos)
            except NadaParaListar:
                super()._sistema.mensagem_sistema.warning(
                    mensagens_sistema.get('enter_continuar')
                )
                input()

    @property
    def clientes(self):
        return self.__clientes
