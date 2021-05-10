from model.Fornecedor import Fornecedor
from view.TelaFornecedor import TelaFornecedor
from view.TelaFornecedorCadastro import TelaFornecedorCadastro
from view.TelaEndereco import TelaEndereco
from messages.Sistema import mensagens as mensagens_sistema
from messages.Fornecedor import mensagens
from utils.exceptions.TelaFechada import TelaFechada
from dao.FornecedoresDAO import FornecedoresDAO


class ControladorFornecedores:
    __instance = None

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela = TelaFornecedor(self)
        self.__tela_cadastro = TelaFornecedorCadastro(self)
        self.__tela_endereco = TelaEndereco(self)
        self.__dao = FornecedoresDAO()

    def __new__(cls, _):
        if ControladorFornecedores.__instance is None:
            ControladorFornecedores.__instance = object.__new__(cls)
        return ControladorFornecedores.__instance

    @property
    def dao(self) -> FornecedoresDAO:
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
        return list(map(lambda item: [item.codigo, item.nome, item.email, item.telefone, item.cnpj, item.fornece.nome, item.endereco], self.__dao.get_all()))

    def adicionar(self):
        event, dados_fornecedor = self.__tela_cadastro.abrir_tela(False, None)

        if event == 'criar':
            # Verifica se existe categorias de produto para cadastrar, se não possuir, abre a tela para o cadastro.
            if len(self.__controlador_sistema.controlador_cat_produto.categorias) == 0:
                # Cadastra categoria
                try:
                    dados_fornecedor['fornece'] = \
                        self.__controlador_sistema.controlador_cat_produto.adicionar()
                except TelaFechada:
                    return
                except Exception:
                    return
            else:
                # Seleciona categoria
                try:
                    dados_fornecedor['fornece'] = \
                        self.__controlador_sistema\
                            .controlador_cat_produto.buscar()
                except TelaFechada:
                    return

            fornecedores = self.__dao.get_all()
            if len([x for x in fornecedores if x.cnpj == dados_fornecedor['cnpj']]) == 0:
                instancia_fornecedor = Fornecedor(*dados_fornecedor.values())

                event, dados_endereco = self.__tela_endereco.abrir_tela()

                if event == 'exited':
                    return
                elif event == 'criar':
                    instancia_fornecedor.definir_endereco(
                        *dados_endereco.values()
                    )
                    self.__dao.add(instancia_fornecedor)
                    return instancia_fornecedor
            else:
                self.__controlador_sistema.mensagem_sistema.warning(
                    mensagens.get('ja_cadastrado'))

    def excluir(self, codigo_fornecedor):
        try:
            self.__dao.remove(self.__dao.get(codigo_fornecedor))
        except Exception:
            self.__controlador_sistema.mensagem_sistema\
                .error(mensagens.get('erro_excluir'))

    def editar(self, codigo_fornecedor):
        fornecedor = self.__dao.get(codigo_fornecedor)
        event, dados_fornecedor = self.__tela_cadastro.abrir_tela(
            True, fornecedor
        )

        if event == 'exited':
            return
        elif event == 'criar':
            _, _, email, telefone, _ = dados_fornecedor.values()

            fornecedor.email = email
            fornecedor.telefone = telefone

            self.__dao.add(fornecedor)
