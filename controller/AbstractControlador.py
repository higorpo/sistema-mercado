from abc import ABC, abstractmethod
from controller.ControladorSistema import ControladorSistema


class AbstractControlador(ABC):
    @abstractmethod
    def __init__(self, controlador_sistema: ControladorSistema, tela):
        self.__controlador_sistema = controlador_sistema
        self.__tela = tela

    def adicionar(self):
        self.novo_registro(self.__tela.adicionar())

    @abstractmethod
    def novo_registro(self, opcoes: list):
        pass
