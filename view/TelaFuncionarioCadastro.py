import PySimpleGUI as sg
from datetime import date
from model.Funcionario import Funcionario
from utils.Terminal import Terminal
from utils.exceptions.NenhumaOpcaoParaSelecionar import NenhumaOpcaoParaSelecionar
from view.AbstractTela import AbstractTela
from messages.Funcionarios import mensagens
from messages.Sistema import mensagens as mensagens_sistema


class TelaFuncionarioCadastro(AbstractTela):
    def __init__(self, controlador):
        sg.ChangeLookAndFeel('Reddit')

        super().__init__(controlador, nome_tela='Funcionários')

    def init_components(self, modo_edicao, data):
        layout = super().layout_tela_cadastro([
            {'key': 'nome_funcionario', 'label': 'Nome do funcionário'},
            {'key': 'email', 'label': 'E-mail do funcionário'},
            {'key': 'telefone', 'label': 'Telefone do funcionário'},
            {'key': 'cpf', 'label': 'CPF do funcionário'},
            {'key': 'salario', 'label': 'Salário do funcionário'},
        ])

        super().set_tela_layout(layout, size=(300, 400))

    def abrir_tela(self, modo_edicao, data):
        self.init_components(modo_edicao, data)

        # Armazena para cada um dos inputs se ele está válido ou não.
        valido = [False, False, False, False, False]

        while True:
            event, values = super().abrir_tela()

            print(event)
            print(values)

            # Caso o usuário feche a janela do programa
            if event == sg.WIN_CLOSED:
                return ('exited', None)

            # Valida os inputs de texto
            elif event == 'input_nome_funcionario':
                valido[0] = super().validar_input(
                    event,
                    super().validar_nome(values[event]) == False,
                    'Nome inválido, digite um nome e sobrenome válido.'
                )
                continue
            elif event == 'input_email':
                valido[1] = super().validar_input(
                    event,
                    super().validar_email(values[event]) == False,
                    'E-mail inválido, digite um e-mail válido.'
                )
                continue
            elif event == 'input_telefone':
                valido[2] = super().validar_input(
                    event,
                    super().validar_telefone(values[event]) == False,
                    'Telefone inválido, digite um telefone válido.'
                )
                continue
            elif event == 'input_cpf':
                valido[3] = super().validar_input(
                    event,
                    super().validar_cpf(values[event]) == False,
                    'CPF inválido, digite um CPF válido.'
                )
                continue
            elif event == 'input_salario':
                valido[4] = super().validar_input(
                    event,
                    super().validar_numero(values[event]) == False,
                    'Salário inválido, digite um salário válido.'
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
                    return (
                        'criar', {
                            'data_atual': date.today().strftime('%d/%m/%Y'),
                            'salario': values['input_salario'],
                            'nome': values['input_nome_funcionario'],
                            'email': values['input_email'],
                            'telefone': values['input_telefone'],
                            'cpf': values['input_cpf'],
                        }
                    )
            else:
                return (event, values)