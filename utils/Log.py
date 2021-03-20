import os


def warning(message: str) -> None:
    # Printa uma mensagem de aviso
    print(f'\033[93m{message}\033[0m')


def sucess(message: str) -> None:
    # Printa uma mensagem de sucesso
    print(f'\033[92m{message}\033[0m')


def error(message: str) -> None:
    # Printa uma mensagem de erro
    print(f'\033[91m{message}\033[0m')


def info(message: str) -> None:
    # Printa uma mensagem de informação
    print(f'\033[96m{message}\033[0m')


def log(message: str) -> None:
    # Print um log normal
    print(message)


def clear() -> None:
    os.system('clear')
