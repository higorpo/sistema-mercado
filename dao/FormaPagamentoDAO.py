from dao.AbstractDAO import DAO
from model.FormaPagamento import FormaPagamento


class FormaPagamentoDAO(DAO):
    def __init__(self):
        super().__init__('dao/store/forma_pagamento.pkl')

    def add(self, forma_pagamento: FormaPagamento):
        if ((forma_pagamento is not None) and isinstance(forma_pagamento, FormaPagamento) and isinstance(forma_pagamento.codigo, int)):
            super().add(forma_pagamento.codigo, forma_pagamento)

    def remove(self, forma_pagamento: FormaPagamento):
        if ((forma_pagamento is not None) and isinstance(forma_pagamento, FormaPagamento) and isinstance(forma_pagamento.codigo, int)):
            super().remove(forma_pagamento.codigo)
