import PySimpleGUI as sg
from model.Cliente import Cliente
from utils.Validators import Validators
from utils.Formatters import Formatters
from view.AbstractTela import AbstractTela
from messages.Cliente import mensagens

LISTA_ESCOLHAS = ['Sim', 'Não']


class TelaClienteCadastro(AbstractTela):
    def __init__(self, controlador):
        sg.ChangeLookAndFeel('Reddit')

        super().__init__(controlador, nome_tela='Clientes')

    def init_components(self, modo_edicao, data: Cliente):
        layout = super().layout_tela_cadastro([
            {
                'key': 'nome_cliente',
                'label': mensagens.get('label_nome'),
                'type': 'text',
                'default_text': '' if modo_edicao == False else data.nome,
                'disabled': modo_edicao
            },
            {
                'key': 'email',
                'label': mensagens.get('label_email'),
                'type': 'text',
                'default_text': '' if modo_edicao == False else data.email
            },
            {
                'key': 'telefone',
                'label': mensagens.get('label_telefone'),
                'type': 'text',
                'default_text': '' if modo_edicao == False else data.telefone
            },
            {
                'key': 'cpf',
                'label': mensagens.get('label_cpf'),
                'type': 'text',
                'default_text': '' if modo_edicao == False else data.cpf,
                'disabled': modo_edicao
            },
            {
                'key': 'vip',
                'label': mensagens.get('label_vip'),
                'type': 'combo',
                'default_value': '' if modo_edicao == False else data.vip,
                'values': LISTA_ESCOLHAS
            },
        ], modo_edicao)

        super().set_tela_layout(layout, size=(300, 400))

    def abrir_tela(self, modo_edicao, data: Cliente):
        self.init_components(modo_edicao, data)

        # Armazena para cada um dos inputs se ele está válido ou não.
        valido = [modo_edicao] * 5

        while True:
            event, values = super().abrir_tela()

            # Caso o usuário feche a janela do programa
            if event == sg.WIN_CLOSED:
                return ('exited', None)

            # Valida os inputs de texto
            elif event == 'input_nome_cliente':
                valido[0] = super().validar_input(
                    event,
                    Validators.validar_nome(values[event]) == False,
                    'Nome inválido, digite um nome e sobrenome válido.'
                )
                continue
            elif event == 'input_email':
                valido[1] = super().validar_input(
                    event,
                    Validators.validar_email(values[event]) == False,
                    'E-mail inválido, digite um e-mail válido.'
                )
                continue
            elif event == 'input_telefone':
                valido[2] = super().validar_input(
                    event,
                    Validators.validar_telefone(values[event]) == False,
                    'Telefone inválido, digite um telefone válido.'
                )
                continue
            elif event == 'input_cpf':
                valido[3] = super().validar_input(
                    event,
                    Validators.validar_cpf(values[event]) == False,
                    'CPF inválido, digite um CPF válido.'
                )
                continue
            elif event == 'input_vip':
                valido[4] = super().validar_input(
                    event,
                    values[event] not in LISTA_ESCOLHAS and
                    Validators.validar_string(values[event]) == False,
                    'Escolha inválida, selecione uma escolha válida.'
                )
                continue
            elif event == 'btn_salvar':
                # Verifica se todos os campos são válidos, se não forem, exibe mensagem de erro.
                if False in valido:
                    sg.popup_no_buttons(
                        'Existem campos inválidos, corrija-os antes de salvar.',
                        title='Erro'
                    )
                    continue
                else:
                    # Verifica se o valor do combo está certo...
                    if values['input_vip'] not in LISTA_ESCOLHAS:
                        valido[4] = super().validar_input(
                            'input_vip',
                            True,
                            'Escolha inválida, selecione uma escolha válida.'
                        )
                        continue
                    else:
                        super().fechar_tela()
                        return (
                            'criar', {
                                'vip': True if values['input_vip'] == "Sim" else False,
                                'nome': values['input_nome_cliente'],
                                'email': values['input_email'],
                                'telefone': Formatters.formatar_telefone(values['input_telefone']),
                                # por questões de validação...
                                'cpf': Formatters.formatar_cpf(values['input_cpf']),
                            }
                        )
            else:
                return (event, values)
