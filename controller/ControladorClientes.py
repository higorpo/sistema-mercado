from model.Cliente import Cliente
from view.TelaCliente import TelaCliente
from view.TelaClienteCadastro import TelaClienteCadastro
from view.TelaClienteSelecao import TelaClienteSelecao
from messages.Sistema import mensagens as mensagens_sistema
from messages.Cliente import mensagens
from view.TelaEndereco import TelaEndereco
from view.TelaPedidosPorCliente import TelaPedidosPorCliente
from configs.settings import Settings
from utils.exceptions.TelaFechada import TelaFechada
from dao.ClienteDAO import ClienteDAO


class ControladorClientes:
    __instance = None

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela = TelaCliente(self)
        self.__tela_cadastro = TelaClienteCadastro(self)
        self.__tela_selecao = TelaClienteSelecao(self)
        self.__tela_pedidos_por_cliente = TelaPedidosPorCliente(self)
        self.__dao = ClienteDAO()

        self.__tela_endereco = TelaEndereco(self)

    def __new__(cls, _):
        if ControladorClientes.__instance is None:
            ControladorClientes.__instance = object.__new__(cls)
        return ControladorClientes.__instance

    @property
    def dao(self) -> ClienteDAO:
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
            elif event == 'btn_visualizar':
                self.__tela.fechar_tela()
                self.listar_pedidos_por_cliente(values)

    def map_object_to_array(self):
        return list(map(lambda item: [item.codigo, item.nome, item.email, item.telefone, item.cpf, item.endereco, item.vip], self.__dao.get_all()))

    def adicionar(self):
        event, dados_cliente = self.__tela_cadastro.abrir_tela(False, None)

        if event == 'criar':
            clientes = self.__dao.get_all()
            if len([x for x in clientes if x.cpf == dados_cliente['cpf']]) == 0:
                instancia_cliente = Cliente(*dados_cliente.values())
                event, dados_endereco = self.__tela_endereco.abrir_tela()

                if event == 'exited':
                    return
                elif event == 'criar':
                    instancia_cliente.definir_endereco(
                        *dados_endereco.values())
                    self.__dao.add(instancia_cliente)
            else:
                self.__controlador_sistema\
                    .mensagem_sistema.warning(mensagens.get('ja_cadastrado'))

    def excluir(self, codigo_cliente):
        try:
            cliente = self.__dao.get(codigo_cliente)
            self.__dao.remove(cliente)
        except Exception:
            self.__controlador_sistema\
                .mensagem_sistema.error(mensagens.get('erro_excluir'))

    def editar(self, codigo_cliente):
        cliente = self.__dao.get(codigo_cliente)

        event, dados_clientes = self.__tela_cadastro.abrir_tela(
            True, cliente)

        if event == 'exited':
            return
        elif event == 'criar':
            vip, _, email, telefone, _ = dados_clientes.values()

            cliente.email = email
            cliente.telefone = telefone
            cliente.vip = vip

            self.__dao.add(cliente)

    def listar_pedidos_por_cliente(self, codigo_cliente):
        print(codigo_cliente)

        cliente = self.__dao.get(codigo_cliente)
        data = list(map(lambda item: [item.codigo, item.observacao, item.data_pedido,
                                      item.forma_pagamento.metodo, item.obter_itens_pedido()], cliente.pedidos))
        while True:
            event, values = self.__tela_pedidos_por_cliente.abrir_tela(data)
            if event == 'exited':
                break

    def buscar(self, titulo_tela: str) -> Cliente:
        event, key = self.__tela_selecao.abrir_tela(
            self.map_object_to_array()
        )

        if event == 'exited':
            raise TelaFechada
        elif event == 'selecionado':
            return self.__dao.get(key)

    @ property
    def clientes(self):
        return self.__dao.get_all()
