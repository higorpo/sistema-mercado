import os
from utils.Terminal import Terminal


class TelaMensagemSistema:
    def __init__(self, controlador):
        self.__controlador_sistema = controlador

    def warning(self, message: str) -> None:
        # Printa uma mensagem de aviso
        print(Terminal.warning(self, message))

    def success(self, message: str) -> None:
        # Printa uma mensagem de sucesso
        print(Terminal.success(self, message))

    def error(self, message: str) -> None:
        # Printa uma mensagem de erro
        print(Terminal.error(self, message))

    def info(self, message: str) -> None:
        # Printa uma mensagem de informação
        print(Terminal.info(self, message))

    def log(self, message: str) -> None:
        # Print um log normal
        print(message)

    def clear(self) -> None:
        Terminal.clear_all(self)
