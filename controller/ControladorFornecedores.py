from controller.AbstractControlador import AbstractControlador
from model.Fornecedor import Fornecedor
from view.TelaFornecedor import TelaFornecedor
from view.TelaEndereco import TelaEndereco
from messages.Sistema import mensagens as mensagens_sistema
from messages.Fornecedor import mensagens
from utils.faker.Fornecedor import fakeFornecedor
from utils.exceptions.NenhumaOpcaoSelecionada import NenhumaOpcaoSelecionada
from utils.exceptions.NenhumaOpcaoParaSelecionar import NenhumaOpcaoParaSelecionar
from configs.settings import Settings


class ControladorFornecedores(AbstractControlador):
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema, TelaFornecedor(self))
        self.__fornecedores = \
            [fakeFornecedor] if Settings.INICIAR_SISTEMA_COM_DADOS_FAKES else []
        self.__tela_endereco = TelaEndereco(self)

    def abre_tela(self):
        super().abre_tela(mensagens_sistema.get('titulo_tela_opcoes'), [
            mensagens.get('cadastrar'),
            mensagens.get('excluir'),
            mensagens.get('editar'),
            mensagens.get('listar')
        ],
            [
            self.adicionar,
            self.excluir,
            self.editar,
            self.listar
        ])

    def adicionar(self):
        dados_fornecedor = super()._tela.adicionar()

        # Verifica se existe categorias de produto para cadastrar, se não possuir, abre a tela para o cadastro.
        if len(super()._sistema.controlador_cat_produto.categorias) == 0:
            # Cadastra categoria
            super()._sistema.mensagem_sistema.clear()
            dados_fornecedor['fornece'] = \
                super()._sistema.controlador_cat_produto.adicionar()
        else:
            # Seleciona categoria
            try:
                dados_fornecedor['fornece'] = \
                    super()._sistema.controlador_cat_produto.buscar(
                        mensagens.get('selecionar_categoria_adicionar_fornecedor'))
            except NenhumaOpcaoParaSelecionar:
                super()._sistema.mensagem_sistema.error(mensagens.get('erro_cadastrar'))
                return

        if len([x for x in self.__fornecedores if x.cnpj == dados_fornecedor['cnpj']]) == 0:
            instancia_fornecedor = Fornecedor(*dados_fornecedor.values())
            dados_endereco = self.__tela_endereco.adicionar()
            instancia_fornecedor.definir_endereco(*dados_endereco.values())
            self.__fornecedores.append(instancia_fornecedor)
        else:
            super()._sistema.mensagem_sistema.warning(mensagens.get('ja_cadastrado'))
            self.adicionar()

    def excluir(self):
        if self.__verifica_tem_dados():
            try:
                fornecedor = self.buscar(mensagens.get('titulo_tela_excluir'))
                self.__fornecedores.remove(fornecedor)
            except Exception:
                super()._sistema.mensagem_sistema.error(mensagens.get('erro_excluir'))

    def editar(self):
        if self.__verifica_tem_dados():
            try:
                fornecedor = self.buscar(mensagens.get('titulo_tela_editar'))
                dados_fornecedor = super()._tela.editar(fornecedor)

                email, telefone = dados_fornecedor.values()

                fornecedor.email = email if email != '--' else fornecedor.email
                fornecedor.telefone = telefone if telefone != '--' else fornecedor.telefone
            except Exception:
                super()._sistema.mensagem_sistema.warning(
                    mensagens_sistema.get('nenhuma_opcao_selecionada'))
                self.editar()

    def listar(self):
        super()._tela.listar(self.__fornecedores, mensagens)

    def buscar(self, titulo_tela: str = mensagens.get('titulo_tela_buscar')):
        return super()._tela.buscar(self.__fornecedores, titulo_tela, mensagens)

    def pesquisar_opcoes(self, buscar_por: str):
        return list(filter(lambda x: buscar_por.lower() in x.nome.lower(), self.__fornecedores))

    def __verifica_tem_dados(self) -> bool:
        if len(self.__fornecedores) == 0:
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
