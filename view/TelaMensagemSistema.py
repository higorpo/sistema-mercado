import os


class TelaMensagemSistema:
    def __init__(self, controlador):
        self.__controlador_sistema = controlador

    def warning(self, message: str) -> None:
        # Printa uma mensagem de aviso
        print(f'\033[93m{message}\033[0m')

    def sucess(self, message: str) -> None:
        # Printa uma mensagem de sucesso
        print(f'\033[92m{message}\033[0m')

    def error(self, message: str) -> None:
        # Printa uma mensagem de erro
        print(f'\033[91m{message}\033[0m')

    def info(self, message: str) -> None:
        # Printa uma mensagem de informação
        print(f'\033[96m{message}\033[0m')

    def log(self, message: str) -> None:
        # Print um log normal
        print(message)

    def clear(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')
