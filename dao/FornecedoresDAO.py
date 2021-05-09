import uuid
from dao.AbstractDAO import DAO
from model.Fornecedor import Fornecedor


class FornecedoresDAO(DAO):
    def __init__(self):
        super().__init__('dao/store/fornecedores.pkl')

    def add(self, fornecedores: Fornecedor):
        if ((fornecedores is not None) and isinstance(fornecedores, Fornecedor) and isinstance(fornecedores.codigo, uuid.UUID)):
            super().add(fornecedores.codigo, fornecedores)

    def remove(self, fornecedores: Fornecedor):
        if ((fornecedores is not None) and isinstance(fornecedores, Fornecedor) and isinstance(fornecedores.codigo, uuid.UUID)):
            super().remove(fornecedores.codigo)
