import PySimpleGUI as sg
from utils.Validators import Validators
from view.AbstractTela import AbstractTela
from messages.Pedido import mensagens
from datetime import date


class TelaPedidoCadastro(AbstractTela):
    def __init__(self, controlador):
        sg.ChangeLookAndFeel('Reddit')

        super().__init__(controlador, nome_tela='Pedido')

    def init_components(self):
        layout = super().layout_tela_cadastro([
            {
                'key': 'observacao',
                'label': mensagens.get('label_observacao'),
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
            elif event == 'input_observacao':
                valido[0] = super().validar_input(
                    event,
                    Validators.validar_string(values[event]) == False,
                    'Observação inválida, digite uma observação válida.'
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
                            'observacao': values['input_observacao'],
                            'data_pedido': date.today().strftime('%d/%m/%Y'),
                            'cliente': None,
                            'funcionario': None,
                            'forma_pagamento': None,
                        }
                    )
            else:
                return (event, values)

    def sem_estoque(self):
        sg.popup_no_buttons(
            'Não há produtos em estoque, cadastre-os primeiro....',
            title='Erro'
        )
