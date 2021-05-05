from datetime import date
from model.Funcionario import Funcionario
from utils.Terminal import Terminal
from utils.exceptions.NenhumaOpcaoParaSelecionar import NenhumaOpcaoParaSelecionar
from view.AbstractTela import AbstractTela
from messages.Funcionarios import mensagens
from messages.Sistema import mensagens as mensagens_sistema
import PySimpleGUI as sg
import time


class TelaFuncionario(AbstractTela):
    def __init__(self, controlador):
        sg.ChangeLookAndFeel('Reddit')

        super().__init__(controlador, nome_tela='Funcionários')

    def init_components(self, data):
        headings = ['Nome', 'E-mail', 'Telefone', 'CPF', 'Endereço']

        layout = super()\
            .layout_tela_lista(headings=headings, values=data, modulo_nome='funcionário')

        super().set_tela_layout(layout)

    def abrir_tela(self, data):
        self.init_components(data)

        while True:
            event, values = super().abrir_tela()

            print(event)
            print(values)

            # Quando fechar a tela
            if event == sg.WIN_CLOSED:
                return ('exited', None)
            if event == '-TABLE-' and len(values['-TABLE-']) != 0:
                column_editar_deletar = super()._window.FindElement(
                    'column_editar_deletar'
                )
                column_editar_deletar.Update(visible=True)
            elif (event == 'btn_editar' or event == 'btn_deletar') and len(values['-TABLE-']) == 0:
                sg.popup_no_buttons(
                    'Você precisa selecionar um item da lista para\npoder realizar esta ação.',
                    title='Erro'
                )
            elif (event == 'btn_editar' or event == 'btn_deletar') and len(values['-TABLE-']) != 0:
                return (event, values['-TABLE-'][0])
            else:
                return (event, values)

    def editar(self, funcionario: Funcionario):
        dados_funcionario = {
            'salario': funcionario.salario,
            'email': funcionario.email,
            'telefone': funcionario.telefone
        }

        print(mensagens.get('label_email'))
        print(
            Terminal.warning(
                self,
                mensagens_sistema.get('label_atualmente')
                (
                    'E-mail', dados_funcionario['email']
                )
            )
        )
        dados_funcionario['email'] = super().ler_email(modo_edicao=True)

        print(mensagens.get('label_telefone'))
        print(
            Terminal.warning(
                self,
                mensagens_sistema.get('label_atualmente')
                (
                    'Telefone', dados_funcionario['telefone']
                )
            )
        )
        dados_funcionario['telefone'] = super().ler_telefone(modo_edicao=True)

        print(mensagens.get('label_salario'))
        print(
            Terminal.warning(
                self,
                mensagens_sistema.get('label_atualmente')
                (
                    'Salário', dados_funcionario['salario']
                )
            )
        )
        dados_funcionario['salario'] = super().ler_float(modo_edicao=True)

        return dados_funcionario
