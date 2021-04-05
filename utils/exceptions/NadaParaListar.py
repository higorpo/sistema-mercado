class NadaParaListar(Exception):
    def __init__(self):
        super().__init__('Não há nada para listar')
