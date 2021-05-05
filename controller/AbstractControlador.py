from abc import ABC, abstractmethod
from messages.Sistema import mensagens as mensagens_sistema


class AbstractControlador(ABC):
    @abstractmethod
    def __init__(self, controlador_sistema, tela, tela_cadastro=None):
        self.__controlador_sistema = controlador_sistema
        self.__tela = tela
        self.__tela_cadastro = tela_cadastro

    @abstractmethod
    def abre_tela(self, titulo, opcoes, acoes):
        if len(opcoes) != len(acoes):
            raise ValueError

        opcoes.append(mensagens_sistema.get('voltar'))

        tela_aberta = True
        while tela_aberta:
            opcao_selecionada = self.__tela.mostrar_opcoes(titulo, opcoes)

            if opcao_selecionada == len(opcoes) - 1:
                tela_aberta = False
            else:
                try:
                    acoes[opcao_selecionada]()
                except KeyError:
                    raise NotImplementedError

    def pesquisar_opcoes(self, buscar_por: str):
        raise NotImplementedError

    @property
    def _tela(self):
        return self.__tela

    @property
    def _tela_cadastro(self):
        return self.__tela_cadastro

    @property
    def _sistema(self):
        return self.__controlador_sistema
