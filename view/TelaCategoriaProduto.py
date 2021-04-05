import time
from utils.Terminal import Terminal
from view.AbstractTela import AbstractTela
from model.CategoriaProduto import CategoriaProduto
from utils.exceptions.NenhumaOpcaoParaSelecionar import NenhumaOpcaoParaSelecionar
from messages.CategoriaProduto import mensagens
from messages.Sistema import mensagens as mensagens_sistema


class TelaCategoriaProduto(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)

    def adicionar(self):
        print(mensagens.get('label_nome_categoria'))
        return super().ler_string()
