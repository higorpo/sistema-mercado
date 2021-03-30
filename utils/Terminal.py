import os


class Terminal:
    def warning(self, message: str) -> str:
        # Printa uma mensagem de aviso
        return f'\033[93m{message}\033[0m'

    def sucess(self, message: str) -> str:
        # Printa uma mensagem de sucesso
        return f'\033[92m{message}\033[0m'

    def error(self, message: str) -> str:
        # Printa uma mensagem de erro
        return f'\033[91m{message}\033[0m'

    def info(self, message: str) -> str:
        # Printa uma mensagem de informação
        return f'\033[96m{message}\033[0m'

    def clear_all(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')
