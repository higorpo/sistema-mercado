import PySimpleGUI as sg
from model.FormaPagamento import FormaPagamento
from utils.Validators import Validators
from view.AbstractTela import AbstractTela
from messages.FormaPagamento import mensagens
from messages.Sistema import mensagens as mensagens_sistema


class TelaFormaPagamentoCadastro(AbstractTela):
    def __init__(self, controlador):
        sg.ChangeLookAndFeel('Reddit')

        super().__init__(controlador, nome_tela='Forma de pagamento')

    def init_components(self):
        layout = super().layout_tela_cadastro([
            {
                'key': 'metodo',
                'label': mensagens.get('label_metodo_pagamento'),
                'type': 'text',
            },
        ], False)

        super().set_tela_layout(layout, size=(300, 400))

    def abrir_tela(self):
        self.init_components()

        # Armazena para cada um dos inputs se ele está válido ou não.
        valido = [False] * 1

        while True:
            event, values = super().abrir_tela()

            # Caso o usuário feche a janela do programa
            if event == sg.WIN_CLOSED:
                return ('exited', None)

            # Valida os inputs de texto
            elif event == 'input_metodo':
                valido[0] = super().validar_input(
                    event,
                    Validators.validar_string(values[event]) == False,
                    'Nome do método de pagamento inválido, digite um nome válido.'
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
                    super().fechar_tela()
                    return (
                        'criar', {
                            'metodo': values['input_metodo'],
                        }
                    )
            else:
                return (event, values)
