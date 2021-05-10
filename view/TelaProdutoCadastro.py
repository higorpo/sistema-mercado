import PySimpleGUI as sg
from model.Produto import Produto
from utils.Validators import Validators
from utils.Formatters import Formatters
from view.AbstractTela import AbstractTela
from messages.Produto import mensagens


class TelaProdutoCadastro(AbstractTela):
    def __init__(self, controlador):
        sg.ChangeLookAndFeel('Reddit')

        super().__init__(controlador, nome_tela='Produto')

    def init_components(self, modo_edicao, data: Produto):
        layout = super().layout_tela_cadastro([
            {
                'key': 'nome_produto',
                'label': mensagens.get('label_nome'),
                'type': 'text',
                'default_text': '' if modo_edicao == False else data.nome,
                'disabled': modo_edicao
            },
            {
                'key': 'qtd_estoque',
                'label': mensagens.get('label_estoque'),
                'type': 'text',
                'default_text': '' if modo_edicao == False else data.qtd_estoque
            },
            {
                'key': 'marca',
                'label': mensagens.get('label_marca'),
                'type': 'text',
                'default_text': '' if modo_edicao == False else data.marca,
                'disabled': modo_edicao
            },
            {
                'key': 'preco',
                'label': mensagens.get('label_preco'),
                'type': 'text',
                'default_text': '' if modo_edicao == False else data.preco
            },
        ], modo_edicao)

        super().set_tela_layout(layout, size=(300, 400))

    def abrir_tela(self, modo_edicao, data: Produto):
        self.init_components(modo_edicao, data)

        # Armazena para cada um dos inputs se ele está válido ou não.
        valido = [modo_edicao] * 4

        while True:
            event, values = super().abrir_tela()

            # Caso o usuário feche a janela do programa
            if event == sg.WIN_CLOSED:
                return ('exited', None)

            # Valida os inputs de texto
            elif event == 'input_nome_produto':
                valido[0] = super().validar_input(
                    event,
                    Validators.validar_string(values[event]) == False,
                    'Nome de produto inválido, digite um nome válido.'
                )
                continue
            elif event == 'input_qtd_estoque':
                valido[1] = super().validar_input(
                    event,
                    Validators.validar_numero(values[event]) == False,
                    'Quantidade inválida, digite uma quantidade válida.'
                )
                continue
            elif event == 'input_marca':
                valido[2] = super().validar_input(
                    event,
                    Validators.validar_string(values[event]) == False,
                    'Nome de marca inválido, digite um nome válido.'
                )
                continue
            elif event == 'input_preco':
                valido[3] = super().validar_input(
                    event,
                    Validators.validar_float(values[event]) == False,
                    'Preço inválido, digite um preço válido.'
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
                            'nome': values['input_nome_produto'],
                            'qtd_estoque': int(values['input_qtd_estoque']),
                            'marca': values['input_marca'],
                            'preco': float(values['input_preco']),
                            'categoria': None,
                        }
                    )
            else:
                return (event, values)
