from view.AbstractTela import AbstractTela
from utils.Terminal import Terminal
from messages.Produto import mensagens
from messages.Sistema import mensagens as mensagens_sistema
from utils.exceptions.NenhumaOpcaoParaSelecionar import NenhumaOpcaoParaSelecionar


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
            'marca': None,
            'preco': None
        }

        print(mensagens.get('label_nome'))
        print(
            Terminal.warning(
                self,
                mensagens.get('label_atualmente')
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
                mensagens.get('label_atualmente')
                (
                    'Estoque', dados_produto['qtd_estoque']
                )
            )
        )

        dados_produto['qtd_estoque'] = super().ler_inteiro(modo_edicao=True)

        print(mensagens.get('label_marca'))
        print(
            Terminal.warning(
                self,
                mensagens.get('label_atualmente')
                (
                    'Marca', dados_produto['marca']
                )
            )
        )

        dados_produto['marca'] = super().ler_string(modo_edicao=True)

        print(mensagens.get('label_preco'))
        print(
            Terminal.warning(
                self,
                mensagens.get('label_atualmente')
                (
                    'Preco', dados_produto['preco']
                )
            )
        )

        dados_produto['preco'] = super().ler_float(modo_edicao=True)

        return dados_produto

    # TODO: Os metodos de listar e buscar talvez agora possam ser passados para o Abstract
    def listar(self, produtos):
        Terminal.clear_all(self)
        print(Terminal.info(self, mensagens.get('mostrando_cadastros')))
        if len(produtos) == 0:
            print(mensagens.get('nada_cadastrado'))
        else:
            for produto in produtos:
                print(mensagens.get('lista_valores')(produto))
        print(Terminal.warning(self, mensagens_sistema.get('enter_continuar')))
        input()

    def buscar(self, produtos, titulo_tela):
        if len(produtos) == 0:
            print(Terminal.error(
                self,
                mensagens.get('nada_cadastrado_busca')
            ))
            print(Terminal.warning(self, mensagens_sistema.get('enter_continuar')))
            input()
            raise NenhumaOpcaoParaSelecionar

        return super().encontrar_opcao(produtos, titulo_tela)
