import utils.Log as Log
from abc import ABC, abstractmethod


class AbstractControlador(ABC):
    @abstractmethod
    def __init__(self, controlador_sistema, tela):
        self.__controlador_sistema = controlador_sistema
        self.__tela = tela

    @abstractmethod
    def abre_tela(self, titulo, opcoes, acoes):
        if len(opcoes) != len(acoes):
            Log.error(
                'ERRO: O tamanho da lista de opções e de ações na tela é diferente!')
            exit(0)

        opcoes.append('<-- Voltar')

        tela_aberta = True
        while tela_aberta:
            opcao_selecionada = self.__tela.mostrar_opcoes(titulo, opcoes)

            if opcao_selecionada == len(opcoes) - 1:
                tela_aberta = False
            else:
                try:
                    acoes[opcao_selecionada]()
                except KeyError:
                    Log.error('ERRO: A opção selecionada não foi implementada!')
                    time.sleep(2)

    @property
    def _tela(self):
        return self.__tela
