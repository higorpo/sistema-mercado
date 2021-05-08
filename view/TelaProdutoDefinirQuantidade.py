import PySimpleGUI as sg
from datetime import date
from model.Produto import Produto
from utils.Validators import Validators
from utils.Formatters import Formatters
from view.AbstractTela import AbstractTela
from messages.Produto import mensagens
from messages.Sistema import mensagens as mensagens_sistema

LISTA_ESCOLHAS = ['Sim', 'Não']


class TelaProdutoDefinirQuantidade(AbstractTela):
    def __init__(self, controlador):
        sg.ChangeLookAndFeel('Reddit')

        super().__init__(controlador, nome_tela='Quantidade a comprar')

    def init_components(self, data: list):
        layout = super().layout_tela_cadastro(list(map(lambda produto: ({
            'key': f'quantidade_comprada_{produto.codigo}',
            'label': mensagens.get('label_quantidade_desejada')(produto),
            'type': 'text',
        }), data)
        ), False)

        super().set_tela_layout(layout, size=(300, 400))

    def abrir_tela(self, data: list):
        self.init_components(data)

        # Armazena para cada um dos inputs se ele está válido ou não.
        valido = [False] * len(data)

        while True:
            event, values = super().abrir_tela()

            lista_eventos = [
                f'input_quantidade_comprada_{x.codigo}' for x in data]

            # Caso o usuário feche a janela do programa
            if event == sg.WIN_CLOSED:
                return ('exited', None)

            # Valida os inputs de texto
            elif event in lista_eventos:
                for x in lista_eventos:
                    if x == event:
                        valido[lista_eventos.index(event)] = super().validar_input(
                            event,
                            (Validators.validar_numero(values[event]) and data[lista_eventos.index(event)].qtd_estoque >= int(values[event])) == False, 'Quantidade inválida')
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
                    return {x.codigo: int(values[f'input_quantidade_comprada_{x.codigo}']) for x in data}

            else:
                return (event, values)
