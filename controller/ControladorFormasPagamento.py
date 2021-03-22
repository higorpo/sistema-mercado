from controller.AbstractControlador import AbstractControlador
from view.TelaFormaPagamento import TelaFormaPagamento


class ControladorFormasPagamento(AbstractControlador):
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema, TelaFormaPagamento(self))

    def abre_tela(self):
        super().abre_tela('O que você deseja fazer?', [
            'Cadastrar nova forma de pagamento',
            'Listar todas as formas de pagamento'
        ], [
            self.adicionar,
            self.listar  # ,
            # self.buscar
        ])

    def adicionar(self):
        super()._tela.adicionar()

    def listar(self):
        pass

    def buscar(self):
        pass
