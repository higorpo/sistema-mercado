from view.AbstractTela import AbstractTela
from utils.Terminal import Terminal
from messages.Produto import mensagens
from messages.Sistema import mensagens as mensagens_sistema
from utils.exceptions.NenhumaOpcaoParaSelecionar import NenhumaOpcaoParaSelecionar
from pick import pick
import PySimpleGUI as sg


class TelaProduto(AbstractTela):
    def __init__(self, controlador):
        sg.ChangeLookAndFeel('Reddit')

        super().__init__(controlador, nome_tela='Produtos')

    def init_components(self, data):
        headings = ['Nome', 'Qtd. Estoque', 'Marca', 'Preço', 'Categoria']

        layout = super()\
            .layout_tela_lista(headings=headings, values=data, modulo_nome='produto')

        super().set_tela_layout(layout)

    def abrir_tela(self, data):
        self.init_components(data)

        while True:
            event, values = super().abrir_tela()

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
                print(f'Event: {event}\nValues: {values}')
                return (event, values['-TABLE-'][0])
            else:
                return (event, values)

    # TODO: Implementar seleção múltipla de produtos
    def selecionar_produtos(self, opcoes, titulo_tela):
        if len(opcoes) == 0:
            print(Terminal.warning(self, mensagens.get('estoque_vazio')))
            print(Terminal.warning(self, mensagens_sistema.get('enter_continuar')))
            input()
            raise ValueError

        lista_opcoes = list(map(lambda x: x.nome, opcoes))
        produtos_selecionados = pick(
            lista_opcoes, titulo_tela, multiselect=True, min_selection_count=1)
        produtos, index = zip(*produtos_selecionados)
        return [x for x in opcoes if x.nome in produtos]

    # TODO: Mover essa ação pra uma nova tela separada (fazer com que cada evento de clique adicione o index do produto
    # numa lista, sempre checando se há um igual ou não. Depois, abra uma tela que mostre os nomes dos produtos
    # selecionados como label e nos inputs permitir digitar a quantidade de produtos a ser comprada)
    def definir_quantidade_comprada(self, produto_selecionado, qtd_estoque: int):
        print(mensagens.get('label_quantidade_desejada')
              (produto_selecionado, qtd_estoque))
        return int(super().ler_inteiro())
