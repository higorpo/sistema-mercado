from dao.AbstractDAO import DAO
from model.Cliente import Cliente


class ClienteDAO(DAO):
    def __init__(self):
        super().__init__('dao/store/cliente.pkl')

    def add(self, cliente: Cliente):
        if ((cliente is not None) and isinstance(cliente, Cliente) and isinstance(cliente.cpf, str)):
            super().add(cliente.cpf, cliente)

    def remove(self, cliente: Cliente):
        if ((cliente is not None) and isinstance(cliente, Cliente) and isinstance(cliente.cpf, str)):
            super().remove(cliente.cpf)
