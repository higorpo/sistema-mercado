import utils.Log as Log
from abc import ABC, abstractmethod


class AbstractControlador(ABC):
    @abstractmethod
    def __init__(self, controlador_sistema, tela):
        self.__controlador_sistema = controlador_sistema
        self.__tela = tela

    # def adicionar(self):
    #     self.novo_registro(self.__tela.adicionar())

    # @abstractmethod
    # def novo_registro(self, opcoes: list):
    #     pass

    @abstractmethod
    def abre_tela(self, titulo, opcoes, acoes):
        if len(opcoes) != len(acoes):
            Log.error(
                'ERRO: O tamanho da lista de opções e de ações na tela é diferente!')
            exit(0)

        opcao_selecionada = self.__tela.mostrar_opcoes(titulo, opcoes)
        acoes[opcao_selecionada]

    @property
    def _tela(self):
        return self.__tela
