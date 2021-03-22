from abc import ABC, abstractmethod
import utils.Log as Log
from brutils import cpf, cnpj
import re
from pick import pick
import time

MENSAGEM_ENTRADA_DADOS_INTERROMPIDA = 'AVISO: Entrada de dados interrompida!'


class AbstractTela(ABC):
    @abstractmethod
    def __init__(self, controlador):
        self.__controlador = controlador

    def mostrar_opcoes(self, titulo, opcoes=[]):
        Log.info('• Abrindo opções de seleção, aguarde...')
        time.sleep(2)
        try:
            option, index = pick(opcoes, titulo)
        except KeyboardInterrupt:
            Log.error(MENSAGEM_ENTRADA_DADOS_INTERROMPIDA)
            exit(0)
        Log.warning(f'Opção selecionada: {option}')
        return index

    def ler_string(self) -> str:
        while True:
            try:
                inputted_string = input(mensagem)
                return inputted_string
            except IOError:
                Log.error('ERRO: Ocorreu um erro ao fazer a leitura do valor')
            except KeyboardInterrupt:
                Log.error(MENSAGEM_ENTRADA_DADOS_INTERROMPIDA)
                exit(0)

    def ler_numero(self, min=None, max=None) -> int:
        while True:
            try:
                inputted_int = int(input())

                if min == None and max == None or inputted_int >= min and inputted_int <= max:
                    return inputted_int
                else:
                    Log.error(
                        f'ERRO: Você precisa digitar um número entre {min} e {max}')
            except IOError:
                Log.error('ERRO: Ocorreu um erro ao fazer a leitura do valor')
            except ValueError:
                Log.error(
                    'ERRO: O tipo do valor digitado é inválido, digite um número!')
            except KeyboardInterrupt:
                Log.error('AVISO: Entrada de dados interrompida!')
                exit(0)

    def validar_cnpj(self, numero) -> bool:
        return cnpj.validate(str(numero))

    def validar_cpf(self, numero) -> bool:
        return cpf.validate(str(numero))

    def validar_email(self, email: str) -> bool:
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if(re.search(regex, email)):
            return True
        else:
            return False
