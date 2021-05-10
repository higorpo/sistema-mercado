import PySimpleGUI as sg
from model.Fornecedor import Fornecedor
from utils.Validators import Validators
from utils.Formatters import Formatters
from view.AbstractTela import AbstractTela
from messages.Fornecedor import mensagens


class TelaFornecedorCadastro(AbstractTela):
    def __init__(self, controlador):
        sg.ChangeLookAndFeel('Reddit')

        super().__init__(controlador, nome_tela='Fornecedores')

    def init_components(self, modo_edicao, data: Fornecedor):
        layout = super().layout_tela_cadastro([
            {
                'key': 'nome',
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
                'key': 'cnpj',
                'label': mensagens.get('label_cnpj'),
                'type': 'text',
                'default_text': '' if modo_edicao == False else data.cnpj,
                'disabled': modo_edicao
            }
        ], modo_edicao)

        super().set_tela_layout(layout, size=(300, 400))

    def abrir_tela(self, modo_edicao, data: Fornecedor):
        self.init_components(modo_edicao, data)

        # Armazena para cada um dos inputs se ele está válido ou não.
        valido = [modo_edicao] * 4

        while True:
            event, values = super().abrir_tela()

            # Caso o usuário feche a janela do programa
            if event == sg.WIN_CLOSED:
                return ('exited', None)

            # Valida os inputs de texto
            elif event == 'input_nome':
                valido[0] = super().validar_input(
                    event,
                    Validators.validar_string(values[event]) == False,
                    'Nome de fornecedor inválido, digite um nome válido.'
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
            elif event == 'input_cnpj':
                valido[3] = super().validar_input(
                    event,
                    Validators.validar_cnpj(values[event]) == False,
                    'CNPJ inválido, digite um CNPJ válido.'
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
                            'nome': values['input_nome'],
                            'cnpj': Formatters.formatar_cnpj(values['input_cnpj']),
                            'email': values['input_email'],
                            'telefone': Formatters.formatar_telefone(values['input_telefone']),
                            'fornece': None,
                        }
                    )
            else:
                return (event, values)
