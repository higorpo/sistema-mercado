from utils.Terminal import Terminal
from view.AbstractTela import AbstractTela
from messages.FormaPagamento import mensagens
from messages.Sistema import mensagens as mensagens_sistema
from utils.exceptions.NenhumaOpcaoParaSelecionar import NenhumaOpcaoParaSelecionar


class TelaFormaPagamento(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)

    def adicionar(self):
        print(mensagens.get('label_metodo_pagamento'))
        return super().ler_string()
