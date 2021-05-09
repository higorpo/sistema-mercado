from view.TelaFormaPagamento import TelaFormaPagamento
from view.TelaFormaPagamentoCadastro import TelaFormaPagamentoCadastro
from view.TelaFormaPagamentoSelecao import TelaFormaPagamentoSelecao
from view.TelaFormaPagamentoSelecao import TelaFormaPagamentoSelecao
from model.FormaPagamento import FormaPagamento
from messages.FormaPagamento import mensagens
from utils.exceptions.TelaFechada import TelaFechada
from messages.Sistema import mensagens as mensagens_sistema
from dao.FormaPagamentoDAO import FormaPagamentoDAO


class ControladorFormasPagamento:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela = TelaFormaPagamento(self)
        self.__tela_cadastro = TelaFormaPagamentoCadastro(self)
        self.__tela_selecao = TelaFormaPagamentoSelecao(self)
        self.__dao = FormaPagamentoDAO()

    def abre_tela(self):
        while True:
            event, values = self.__tela.abrir_tela(self.map_object_to_array())
            if event == 'exited':
                break
            elif event == 'btn_cadastrar':
                self.__tela.fechar_tela()
                try:
                    self.adicionar()
                except Exception:
                    continue

    def map_object_to_array(self):
        return list(map(lambda item: [item.codigo, item.metodo], self.__dao.get_all()))

    def adicionar(self):
        event, dados_forma_pagamento = self.__tela_cadastro.abrir_tela()

        formas_pagamento = self.__dao.get_all()
        if event == 'criar':
            if len([x for x in formas_pagamento if x.metodo == dados_forma_pagamento['metodo']]) == 0:
                forma_pagamento = FormaPagamento(
                    dados_forma_pagamento['metodo'])
                self.__dao.add(forma_pagamento)
                return forma_pagamento
            else:
                self.__controlador_sistema.mensagem_sistema.warning(
                    mensagens.get('ja_cadastrado')
                )
                raise Exception
        else:
            raise TelaFechada

    def listar(self):
        self.__tela.listar(self.__dao.get_all(), mensagens)

    def buscar(self, titulo_tela: str) -> FormaPagamento:
        event, key = self.__tela_selecao.abrir_tela(
            self.map_object_to_array()
        )

        if event == 'exited':
            raise TelaFechada
        elif event == 'selecionado':
            return self.__dao.get(key)

    def pesquisar_opcoes(self, buscar_por: str):
        return list(filter(lambda x: buscar_por.lower() in x.metodo.lower(), self.__dao.get_all()))

    @property
    def formas_pagamento(self):
        return self.__dao.get_all()
