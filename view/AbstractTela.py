import utils.Log as Log
from utils.exceptions.NenhumaOpcaoSelecionada import NenhumaOpcaoSelecionada
import re
import time
from abc import ABC, abstractmethod
from brutils import cpf, cnpj
from pick import pick

MENSAGEM_ENTRADA_DADOS_INTERROMPIDA = 'AVISO: Entrada de dados interrompida!'


class AbstractTela(ABC):
    @abstractmethod
    def __init__(self, controlador):
        self.__controlador = controlador

    @property
    def _controlador(self):
        return self.__controlador

    def mostrar_opcoes(self, titulo, opcoes=[]):
        Log.clear()

        if len(opcoes) == 0:
            raise NenhumaOpcaoSelecionada

        try:
            option, index = pick(opcoes, titulo)
        except KeyboardInterrupt:
            Log.error(MENSAGEM_ENTRADA_DADOS_INTERROMPIDA)
            exit(0)
        return index

    def encontrar_opcao(self, opcoes=[]):
        option, index = pick([
            'Listar todas as opções...',
            'Pesquisar...'
        ], 'Selecione uma ação...')

        if index == 0:
            return self.selecionar_a_partir_lista_opcoes(opcoes)
        else:
            Log.clear()
            Log.log('Digite o termo da busca:')

            # Abre input para receber a pesquisa do usuário
            buscar_por = self.ler_string()

            # Faz a pesquisa
            lista_opcoes_encontradas = self.__controlador.pesquisar_opcoes(
                buscar_por
            )

            # Se não encontrar nenhuma informação, infoma ao usuário
            if len(lista_opcoes_encontradas) == 0:
                Log.warning(
                    'Nenhuma informação encontrada com esse termo de busca...'
                )
                raise NenhumaOpcaoSelecionada
            else:
                return self.selecionar_a_partir_lista_opcoes(lista_opcoes_encontradas)

    def selecionar_a_partir_lista_opcoes(self, opcoes):
        lista_opcoes = list(map(lambda x: x.nome, opcoes))

        selecionado = self.mostrar_opcoes(
            'Selecione uma opção abaixo',
            lista_opcoes
        )

        return opcoes[selecionado]

    def ler_string(self) -> str:
        while True:
            try:
                inputted_string = input()

                if len(inputted_string) == 0:
                    Log.warning('AVISO: Digite um valor válido...')
                    continue
                else:
                    return inputted_string
            except IOError:
                Log.error('ERRO: Ocorreu um erro ao fazer a leitura do valor')
            except KeyboardInterrupt:
                Log.error(MENSAGEM_ENTRADA_DADOS_INTERROMPIDA)
                exit(0)

    def ler_inteiro(self, min=None, max=None) -> int:
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
                Log.error(MENSAGEM_ENTRADA_DADOS_INTERROMPIDA)
                exit(0)

    def ler_float(self, min=None, max=None) -> float:
        while True:
            try:
                inputted_float = float(input())

                if min == None and max == None or inputted_float >= min and inputted_float <= max:
                    return inputted_float
                else:
                    Log.error(
                        f'ERRO: Você precisa digitar um número entre {min} e {max}')
            except IOError:
                Log.error('ERRO: Ocorreu um erro ao fazer a leitura do valor')
            except ValueError:
                Log.error(
                    'ERRO: O tipo do valor digitado é inválido, digite um número!')
            except KeyboardInterrupt:
                Log.error(MENSAGEM_ENTRADA_DADOS_INTERROMPIDA)
                exit(0)

    def ler_cpf(self) -> int:
        while True:
            try:
                inputted_cpf = input()
                if self.validar_cpf(inputted_cpf):
                    return int(inputted_cpf)
                else:
                    Log.error('ERRO: O CPF digitado é inválido!')
            except IOError:
                Log.error('ERRO: Ocorreu um erro ao fazer a leitura do valor')
            except ValueError:
                Log.error(
                    'ERRO: O tipo do valor digitado é inválido, digite somente números ou no padrão XXX.XXX.XXX-XX')
            except KeyboardInterrupt:
                Log.error(MENSAGEM_ENTRADA_DADOS_INTERROMPIDA)
                exit(0)

    def ler_cnpj(self) -> int:
        while True:
            try:
                inputted_cnpj = input()
                if self.validar_cnpj(inputted_cnpj):
                    return int(inputted_cnpj)
                else:
                    Log.error('ERRO: O CNPJ digitado é inválido!')
            except IOError:
                Log.error('ERRO: Ocorreu um erro ao fazer a leitura do valor')
            except ValueError:
                Log.error(
                    "ERRO: O tipo do valor digitado é inválido, digite somente números ou no padrão 'XX.XXX.XXX/XXXX-XX'!")
            except KeyboardInterrupt:
                Log.error(MENSAGEM_ENTRADA_DADOS_INTERROMPIDA)
                exit(0)

    def ler_email(self):
        while True:
            try:
                inputted_email = input()
                if self.validar_email(inputted_email):
                    return inputted_email
                else:
                    Log.error('O email digitado é inválido!')
            except IOError:
                Log.error('ERRO: Ocorreu um erro ao fazer a leitura do valor')
            except KeyboardInterrupt:
                Log.error(MENSAGEM_ENTRADA_DADOS_INTERROMPIDA)
                exit(0)

    def ler_telefone(self):
        while True:
            try:
                inputted_telefone = input()
                if self.validar_telefone(inputted_telefone):
                    tel_formatado = "".join(
                        re.findall('\d+', inputted_telefone))
                    return int(tel_formatado)
                else:
                    Log.error('O telefone digitado é inválido!')
            except IOError:
                Log.error('ERRO: Ocorreu um erro ao fazer a leitura do valor')
            except KeyboardInterrupt:
                Log.error(MENSAGEM_ENTRADA_DADOS_INTERROMPIDA)
                exit(0)

    def validar_cnpj(self, cnpj_string: str) -> bool:
        cnpj_formatado = cnpj.sieve(cnpj_string)
        return cnpj.validate(cnpj_formatado)

    def validar_cpf(self, cpf_string: str) -> bool:
        cpf_formatado = cpf.sieve(cpf_string)
        return cpf.validate(cpf_formatado)

    def validar_email(self, email: str) -> bool:
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if(re.search(regex, email)):
            return True
        else:
            return False

    def validar_telefone(self, telefone: str):
        # Fiz assim pro usuário poder inserir telefone de diferentes maneiras (DDD obrigatório)
        # (48) 2020-2020, (48) 20202020, (48) 32020-2020, (48) 320202020
        # 48 {valores acima}, 48{valores acima}
        # Daí no método ler_telefone ele vai pegar só os números e converter pra int
        regex = '(\(?\d{2}\)?\s?)(\d{4,5}\-?\d{4})'
        if re.search(regex, telefone):
            return True
        else:
            return False
