from view.AbstractTela import AbstractTela
from utils.Terminal import Terminal
from messages.Produto import mensagens
from messages.Sistema import mensagens as mensagens_sistema
from utils.exceptions.NenhumaOpcaoParaSelecionar import NenhumaOpcaoParaSelecionar
from pick import pick


class TelaProduto(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)

    def adicionar(self):
        dados_produto = {
            'nome': None,
            'qtd_estoque': None,
            'marca': None,
            'preco': None
        }

        print(mensagens.get('label_nome'))
        dados_produto['nome'] = super().ler_string()

        print(mensagens.get('label_estoque'))
        dados_produto['qtd_estoque'] = super().ler_inteiro()

        print(mensagens.get('label_marca'))
        dados_produto['marca'] = super().ler_string()

        print(mensagens.get('label_preco'))
        dados_produto['preco'] = super().ler_float()

        return dados_produto

    def editar(self, cliente):
        dados_produto = {
            'nome': None,
            'qtd_estoque': None,
            'preco': None
        }

        print(mensagens.get('label_nome'))
        print(
            Terminal.warning(
                self,
                mensagens_sistema.get('label_atualmente')
                (
                    'Nome', dados_produto['nome']
                )
            )
        )

        dados_produto['nome'] = super().ler_string(modo_edicao=True)

        print(mensagens.get('label_estoque'))
        print(
            Terminal.warning(
                self,
                mensagens_sistema.get('label_atualmente')
                (
                    'Estoque', dados_produto['qtd_estoque']
                )
            )
        )

        dados_produto['qtd_estoque'] = super().ler_inteiro(modo_edicao=True)

        print(mensagens.get('label_preco'))
        print(
            Terminal.warning(
                self,
                mensagens_sistema.get('label_atualmente')
                (
                    'Preco', dados_produto['preco']
                )
            )
        )

        dados_produto['preco'] = super().ler_float(modo_edicao=True)

        return dados_produto

    # TODO: Os metodos de listar e buscar talvez agora possam ser passados para o Abstract

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

    def definir_quantidade_comprada(self, produto_selecionado, qtd_estoque: int):
        print(mensagens.get('label_quantidade_desejada')
              (produto_selecionado, qtd_estoque))
        return int(super().ler_inteiro())
