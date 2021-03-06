import PySimpleGUI as sg
from view.AbstractTela import AbstractTela
from utils.Validators import Validators
from messages.Endereco import mensagens

LISTA_ESTADOS = [
    'Acre',
    'Alagoas',
    'Amapá',
    'Amazonas',
    'Bahia',
    'Ceará',
    'Distrito Federal',
    'Espirito Santo',
    'Goiás',
    'Maranhão',
    'Mato Grosso do Sul',
    'Mato Grosso',
    'Minas Gerais',
    'Pará',
    'Paraíba',
    'Paraná',
    'Pernambuco',
    'Piauí',
    'Rio de Janeiro',
    'Rio Grande do Norte',
    'Rio Grande do Sul',
    'Rondônia',
    'Roraima',
    'Santa Catarina',
    'São Paulo',
    'Sergipe',
    'Tocantins'
]


class TelaEndereco(AbstractTela):
    def __init__(self, controlador):
        sg.ChangeLookAndFeel('Reddit')

        super().__init__(controlador, nome_tela='Endereço')

    def init_components(self):
        layout = super().layout_tela_cadastro([
            {
                'key': 'rua',
                'label': mensagens.get('label_rua'),
                'type': 'text'
            },
            {
                'key': 'cidade',
                'label': mensagens.get('label_cidade'),
                'type': 'text'
            },
            {
                'key': 'estado',
                'label': mensagens.get('label_estado'),
                'type': 'combo',
                'values': LISTA_ESTADOS
            },
            {
                'key': 'cep',
                'label': mensagens.get('label_cep'),
                'type': 'text'
            },
            {
                'key': 'complemento',
                'label': mensagens.get('label_complemento'),
                'type': 'text'
            }
        ])

        super().set_tela_layout(layout, size=(300, 400))

    def abrir_tela(self):
        self.init_components()

        # Armazena para cada um dos inputs se ele está válido ou não.
        valido = [False, False, False, False, False]

        while True:
            event, values = super().abrir_tela()

            # Caso o usuário feche a janela do programa
            if event == sg.WIN_CLOSED:
                return ('exited', None)

            # Valida os inputs de texto
            elif event == 'input_rua':
                valido[0] = super().validar_input(
                    event,
                    Validators.validar_string(values[event]) == False,
                    'Endereço inválido, digite um endereço válido.'
                )
                continue
            elif event == 'input_cidade':
                valido[1] = super().validar_input(
                    event,
                    Validators.validar_string(values[event]) == False,
                    'Cidade inválida, digite uma cidade válida.'
                )
                continue
            elif event == 'input_estado':
                valido[2] = super().validar_input(
                    event,
                    values[event] not in LISTA_ESTADOS and
                    Validators.validar_string(values[event]) == False,
                    'Estado inválido, selecione um estado válido.'
                )
                continue
            elif event == 'input_cep':
                valido[3] = super().validar_input(
                    event,
                    Validators.validar_cep(values[event]) == False,
                    'CEP inválido, digite um CEP válido.'
                )
                continue
            elif event == 'input_complemento':
                valido[4] = super().validar_input(
                    event,
                    Validators.validar_string(values[event]) == False,
                    'Complemento inválido, digite um complemento válido.'
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
                    if values['input_estado'] not in LISTA_ESTADOS:
                        valido[4] = super().validar_input(
                            'input_estado',
                            True,
                            'Estado inválido, selecione um estado válido.'
                        )
                        continue
                    else:
                        super().fechar_tela()
                        return (
                            'criar', {
                                'rua': values['input_rua'],
                                'cidade': values['input_cidade'],
                                'estado': values['input_estado'],
                                'cep': values['input_cep'],
                                'complemento': values['input_complemento'],
                            }
                        )
            else:
                return (event, values)
