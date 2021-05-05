import time
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

        while True:
            event, values = super().abrir_tela()

            print(event)
            print(values)

            if event == sg.WIN_CLOSED:
                return ('exited', None)
            else:
                return (event, values)
