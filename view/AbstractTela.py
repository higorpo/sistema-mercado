import re
import time
import PySimpleGUI as sg
from abc import ABC, abstractmethod
from brutils import cpf, cnpj
from pick import pick
from utils.Terminal import Terminal
from utils.exceptions.NenhumaOpcaoSelecionada import NenhumaOpcaoSelecionada
from utils.exceptions.NenhumaOpcaoParaSelecionar import NenhumaOpcaoParaSelecionar
from utils.exceptions.LayoutNotDefined import LayoutNotDefined
from messages.Sistema import mensagens as mensagens_sistema

MENSAGEM_ENTRADA_DADOS_INTERROMPIDA = 'AVISO: Entrada de dados interrompida!'
MENSAGEM_ERRO_LEITURA_VALOR = 'ERRO: Ocorreu um erro ao fazer a leitura do valor'


class AbstractTela(ABC):
    @abstractmethod
    def __init__(self, controlador, nome_tela=''):
        self.__controlador = controlador
        self.__nome_tela = nome_tela
        self.__window = None

        self.__table_key = None
        self.__layout_tabela = False

    @property
    def _controlador(self):
        return self.__controlador

    @property
    def _window(self):
        return self.__window

    def abrir_tela(self):
        return self.__window.Read()

    def fechar_tela(self):
        self._window.close()

    def set_tela_layout(self, layout, size=(900, 680)):
        if layout == None:
            raise LayoutNotDefined

        self.__window = sg.Window(
            self.__nome_tela, size=size
        ).Layout(layout(size))

    def layout_tela_cadastro(self, inputs):
        def map_inputs(input):
            inputElement = None

            if input['type'] == 'combo':
                inputElement = sg.Combo(
                    input['values'],
                    key='input_' + input['key'],
                    size=(21, 8),
                    font=('Arial', 15),
                    enable_events=True,
                    background_color='#ffffff',
                )
            elif input['type'] == 'text':
                inputElement = sg.Input(
                    key='input_' + input['key'],
                    default_text=input['default_text'] if 'default_text' in input else '',
                    background_color='#ffffff',
                    font=('Arial', 15),
                    size=(22, 2),
                    enable_events=True
                )

            return [
                sg.Column([
                    [
                        sg.Text(input['label'])
                    ],
                    [
                        inputElement
                    ],
                    [
                        sg.Text(
                            'Preencha este campo.',
                            key='input_' + input['key'] + '_hint',
                            font=('Arial', 8),
                            text_color='#ff0000',
                            visible=True,
                            auto_size_text=True,
                            size=(40, 1)
                        )
                    ]
                ])
            ]

        lista_inputs = list(map(map_inputs, inputs))

        lista_inputs.append([
            sg.Button(
                'Salvar',
                key='btn_salvar',
                size=(32, 2)
            )
        ])

        def callable(size):
            size_height = 150*len(lista_inputs) + 100
            size = (size[0], size_height)

            return [
                [
                    sg.Column(
                        lista_inputs,
                        size=size,
                        pad=(0, 0),
                        scrollable=True, vertical_scroll_only=True
                    )
                ]
            ]

        return callable

    def layout_tela_lista(self, headings=[], values=[], key='-TABLE-', modulo_nome='', btn_deletar_enabled=True, btn_editar_enabled=True):
        self.__table_key = key
        self.__layout_tabela = True

        buttons = []

        if btn_deletar_enabled:
            buttons.append(sg.Button(
                f'Deletar {modulo_nome}',
                key='btn_deletar',
                button_color='#e32f2f',
                size=(40, 2)
            ))

        if btn_editar_enabled:
            buttons.append(sg.Button(
                f'Editar {modulo_nome}',
                key='btn_editar',
                button_color='#000000',
                size=(40, 2)
            ))

        def callable(size):
            if len(values) > 0:
                tableElement = sg.Table(
                    values=values,
                    headings=headings,
                    enable_events=True,
                    auto_size_columns=True,
                    hide_vertical_scroll=False,
                    num_rows=20,
                    justification='center',
                    key='-TABLE-',
                    row_height=30,
                    alternating_row_color='#e0e0e0',
                    select_mode=sg.TABLE_SELECT_MODE_BROWSE,
                )
            else:
                tableElement = sg.Text(
                    'Não há dados para serem exibidos... Comece cadastrando-os!',
                    s=(40, 2),
                    justification='center'
                )

            return [
                [
                    sg.Column([
                        [
                            tableElement
                        ],

                        [
                            sg.Button(
                                f'Cadastrar novo(a) {modulo_nome}',
                                key='btn_cadastrar',
                                size=(40, 2)
                            ),
                            sg.Column(
                                [
                                    buttons
                                ],
                                key='column_editar_deletar',
                                visible=False
                            )
                        ]

                    ], justification='center' if len(values) == 0 else 'left', vertical_alignment='center' if len(values) == 0 else 'top')
                ]
            ]
            return [
                [
                    tableElement
                ],
                [
                    [
                        sg.Button(
                            f'Cadastrar novo(a) {modulo_nome}',
                            key='btn_cadastrar',
                            size=(40, 2)
                        ),
                        sg.Column(
                            [
                                buttons
                            ],
                            key='column_editar_deletar',
                            visible=False
                        )
                    ]
                ]
            ]

        return callable

    def mostrar_opcoes(self, titulo, opcoes=[]):
        Terminal.clear_all(self)

        if len(opcoes) == 0:
            raise NenhumaOpcaoSelecionada

        try:
            option, index = pick(opcoes, titulo)
        except KeyboardInterrupt:
            print(Terminal.error(self, MENSAGEM_ENTRADA_DADOS_INTERROMPIDA))
            exit(0)
        return index

    def encontrar_opcao(self, opcoes=[], titulo_tela: str = "Selecione uma ação..."):
        option, index = pick([
            'Listar todas as opções...',
            'Pesquisar...'
        ], titulo_tela)

        if index == 0:
            return self.selecionar_a_partir_lista_opcoes(opcoes)
        else:
            Terminal.clear_all(self)
            print('Digite o termo da busca:')

            # Abre input para receber a pesquisa do usuário
            buscar_por = self.ler_string()

            # Faz a pesquisa
            lista_opcoes_encontradas = self.__controlador.pesquisar_opcoes(
                buscar_por
            )

            # Se não encontrar nenhuma informação, infoma ao usuário
            if len(lista_opcoes_encontradas) == 0:
                print(Terminal.warning(
                    self,
                    'Nenhuma informação encontrada com esse termo de busca...'
                ))
                time.sleep(1)
                self.encontrar_opcao(opcoes)
            else:
                return self.selecionar_a_partir_lista_opcoes(lista_opcoes_encontradas)

    def selecionar_a_partir_lista_opcoes(self, opcoes):
        try:
            lista_opcoes = list(map(lambda x: x.nome, opcoes))
        except AttributeError:
            lista_opcoes = list(map(lambda x: x.metodo, opcoes))

        selecionado = self.mostrar_opcoes(
            'Selecione uma opção abaixo',
            lista_opcoes
        )

        return opcoes[selecionado]

    def listar(self, lista, mensagens):
        Terminal.clear_all(self)
        print(Terminal.info(self, mensagens.get('mostrando_cadastros')))
        if len(lista) == 0:
            print(mensagens_sistema.get('nada_cadastrado'))
        else:
            for item in lista:
                print(mensagens.get('lista_valores')(item))
        print(Terminal.warning(self, mensagens_sistema.get('enter_continuar')))
        input()

    def buscar(self, lista, titulo_tela, mensagens):
        if len(lista) == 0:
            print(Terminal.error(
                self,
                mensagens.get('nada_cadastrado_busca')
            ))
            print(Terminal.warning(self, mensagens_sistema.get('enter_continuar')))
            input()
            raise NenhumaOpcaoParaSelecionar

        return self.encontrar_opcao(lista, titulo_tela)

    def ler_string(self, modo_edicao: bool = False) -> str:
        while True:
            try:
                inputted_string = input()

                if inputted_string == '--' and modo_edicao == True:
                    return inputted_string

                if len(inputted_string) == 0:
                    print(Terminal.warning(
                        self,
                        'AVISO: Digite um valor válido...'
                    ))
                    continue
                else:
                    return inputted_string
            except IOError:
                print(Terminal.error(self, MENSAGEM_ERRO_LEITURA_VALOR))
            except KeyboardInterrupt:
                print(Terminal.error(self, MENSAGEM_ENTRADA_DADOS_INTERROMPIDA))
                exit(0)

    def ler_inteiro(self, min=None, max=None, modo_edicao: bool = False) -> int:
        while True:
            try:
                inputted_int = input()

                if inputted_int == '--' and modo_edicao == True:
                    return inputted_int

                inputted_int = int(inputted_int)

                if min == None and max == None or inputted_int >= min and inputted_int <= max:
                    return inputted_int
                else:
                    print(
                        Terminal.error(self,
                                       f'ERRO: Você precisa digitar um número entre {min} e {max}')
                    )
            except IOError:
                print(Terminal.error(self, MENSAGEM_ERRO_LEITURA_VALOR))
            except ValueError:
                print(Terminal.error(self,
                                     'ERRO: O tipo do valor digitado é inválido, digite um número!'))
            except KeyboardInterrupt:
                print(Terminal.error(self, MENSAGEM_ENTRADA_DADOS_INTERROMPIDA))
                exit(0)

    def ler_float(self, min=None, max=None, modo_edicao: bool = False) -> float:
        while True:
            try:
                inputted_float = input()

                if inputted_float == '--' and modo_edicao == True:
                    return inputted_float

                inputted_float = float(inputted_float)

                if min == None and max == None or inputted_float >= min and inputted_float <= max:
                    return inputted_float
                else:
                    print(Terminal.error(self,
                                         f'ERRO: Você precisa digitar um número entre {min} e {max}'))
            except IOError:
                print(Terminal.error(self, MENSAGEM_ERRO_LEITURA_VALOR))
            except ValueError:
                print(Terminal.error(self,
                                     'ERRO: O tipo do valor digitado é inválido, digite um número!'))
            except KeyboardInterrupt:
                print(Terminal.error(self, MENSAGEM_ENTRADA_DADOS_INTERROMPIDA))
                exit(0)

    def ler_cpf(self, modo_edicao: bool = False) -> str:
        while True:
            try:
                inputted_cpf = input()

                if inputted_cpf == '--' and modo_edicao == True:
                    return inputted_cpf

                if self.validar_cpf(inputted_cpf):
                    if '.' not in inputted_cpf:
                        inputted_cpf = cpf.display(inputted_cpf)
                    return inputted_cpf
                else:
                    print(Terminal.error(self, 'ERRO: O CPF digitado é inválido!'))
            except IOError:
                print(Terminal.error(self, MENSAGEM_ERRO_LEITURA_VALOR))
            except ValueError:
                print(Terminal.error(self,
                                     'ERRO: O tipo do valor digitado é inválido, digite somente números ou no padrão XXX.XXX.XXX-XX'))
            except KeyboardInterrupt:
                print(Terminal.error(self, MENSAGEM_ENTRADA_DADOS_INTERROMPIDA))
                exit(0)

    def ler_cnpj(self, modo_edicao: bool = False) -> str:
        while True:
            try:
                inputted_cnpj = input()

                if inputted_cnpj == '--' and modo_edicao == True:
                    return inputted_cnpj

                if self.validar_cnpj(inputted_cnpj):
                    if '.' not in inputted_cnpj:
                        inputted_cnpj = cnpj.display(inputted_cnpj)
                    return inputted_cnpj
                else:
                    print(Terminal.error(self, 'ERRO: O CNPJ digitado é inválido!'))
            except IOError:
                print(Terminal.error(self, MENSAGEM_ERRO_LEITURA_VALOR))
            except ValueError:
                print(Terminal.error(self,
                                     'ERRO: O tipo do valor digitado é inválido, digite somente números ou no padrão \'XX.XXX.XXX/XXXX-XX\'!'))
            except KeyboardInterrupt:
                print(Terminal.error(self, MENSAGEM_ENTRADA_DADOS_INTERROMPIDA))
                exit(0)

    def ler_email(self, modo_edicao: bool = False) -> str:
        while True:
            try:
                inputted_email = input()

                if inputted_email == '--' and modo_edicao == True:
                    return inputted_email

                if self.validar_email(inputted_email):
                    return inputted_email
                else:
                    print(Terminal.error(self, 'O email digitado é inválido!'))
            except IOError:
                print(Terminal.error(self, MENSAGEM_ERRO_LEITURA_VALOR))
            except KeyboardInterrupt:
                print(Terminal.error(self, MENSAGEM_ENTRADA_DADOS_INTERROMPIDA))
                exit(0)

    def ler_telefone(self, modo_edicao: bool = False) -> int:
        while True:
            try:
                inputted_telefone = input()

                if inputted_telefone == '--' and modo_edicao == True:
                    return inputted_telefone

                if self.validar_telefone(inputted_telefone):
                    return self.formatar_telefone(inputted_telefone)

                else:
                    print(Terminal.error(self, 'O telefone digitado é inválido!'))
            except IOError:
                print(Terminal.error(self, MENSAGEM_ERRO_LEITURA_VALOR))
            except KeyboardInterrupt:
                print(Terminal.error(self, MENSAGEM_ENTRADA_DADOS_INTERROMPIDA))
                exit(0)

    def ler_cep(self):
        while True:
            try:
                inputted_cep = input()
                if self.validar_cep(inputted_cep):
                    return self.formatar_cep(inputted_cep)
                else:
                    print(Terminal.error(self, 'O CEP digitado é inválido!'))
            except IOError:
                print(Terminal.error(self, MENSAGEM_ERRO_LEITURA_VALOR))
            except KeyboardInterrupt:
                print(Terminal.error(self, MENSAGEM_ENTRADA_DADOS_INTERROMPIDA))
                exit(0)

    def ler_vip(self, modo_edicao: bool = False) -> str:
        while True:
            try:
                inputted_boolean = input()

                if inputted_boolean == '--' and modo_edicao == True:
                    return inputted_boolean

                if inputted_boolean.lower() == 's':
                    return 'sim'
                elif inputted_boolean.lower() == 'n':
                    return 'não'
                else:
                    print(Terminal.error(
                        self, 'O valor digitado é inválido! Digite \'s\' para \'sim\', ou \'n\' para \'não\'!'))
            except IOError:
                print(Terminal.error(self, MENSAGEM_ERRO_LEITURA_VALOR))
            except KeyboardInterrupt:
                print(Terminal.error(self, MENSAGEM_ENTRADA_DADOS_INTERROMPIDA))
                exit(0)

    def validar_input(self, key: str, validator: bool, error_message: str) -> bool:
        hint = self._window.FindElement(key + '_hint')
        if validator:
            hint.Update(
                error_message,
                visible=True
            )
            return False
        else:
            hint.Update(visible=False)
            return True

    def validar_nome(self, nome: str) -> bool:
        regex = '^[A-ZÀ-Ÿ][A-zÀ-ÿ\']+\s([A-zÀ-ÿ\']\s?)*[A-ZÀ-Ÿ][A-zÀ-ÿ\']+$'
        return True if re.search(regex, nome) else False

    def validar_cnpj(self, cnpj_string: str) -> bool:
        cnpj_formatado = cnpj.sieve(cnpj_string)
        return cnpj.validate(cnpj_formatado)

    def validar_cpf(self, cpf_string: str) -> bool:
        cpf_formatado = cpf.sieve(cpf_string)
        return cpf.validate(cpf_formatado)

    def validar_email(self, email: str) -> bool:
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        return True if re.search(regex, email) else False

    def validar_string(self, string: str) -> bool:
        regex = '^[A-Za-záàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ0-9 ]+$'
        return True if re.search(regex, string) else False

    def validar_numero(self, numero: str) -> bool:
        regex = '^([\s\d]+)$'
        return True if re.search(regex, numero) else False

    def validar_telefone(self, telefone: str) -> bool:
        # Maneiras possíveis de inserir o telefone (DDD obrigatório):
        # (48) 2020-2020, (48) 20202020, (48) 32020-2020, (48) 320202020
        # 48 {valores acima}, 48{valores acima}, (48){valores acima}
        regex = '(\(?\d{2}\)?\s?)(\d{4,5}\-?\d{4})'
        return True if re.search(regex, telefone) else False

    def validar_cep(self, cep: str):
        regex = '(\d{5})-?(\d{3})'
        return True if re.search(regex, cep) else False

    def formatar_telefone(self, telefone: str):
        tel_soh_numeros = ''.join(re.findall('\d+', telefone))
        lista_pra_formatar = list(tel_soh_numeros)
        lista_pra_formatar.insert(0, '(')
        lista_pra_formatar.insert(3, ')')
        lista_pra_formatar.insert(4, ' ')
        lista_pra_formatar.insert(-4, '-')
        telefone_formatado = ''.join(lista_pra_formatar)
        return telefone_formatado

    def formatar_cep(self, cep: str):
        cep_soh_numeros = ''.join(re.findall('\d+', cep))
        lista_numeros_do_cep = list(cep_soh_numeros)
        lista_numeros_do_cep.insert(-3, '-')
        cep_formatado = ''.join(lista_numeros_do_cep)
        return cep_formatado
