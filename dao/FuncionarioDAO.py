from dao.AbstractDAO import DAO
from model.Funcionario import Funcionario


class FuncionarioDAO(DAO):
    def __init__(self):
        super().__init__('dao/store/funcionarios.pkl')

    def add(self, funcionario: Funcionario):
        if ((funcionario is not None) and isinstance(funcionario, Funcionario) and isinstance(funcionario.codigo, int)):
            super().add(funcionario.codigo, funcionario)

    def remove(self, funcionario: Funcionario):
        if ((funcionario is not None) and isinstance(funcionario, Funcionario) and isinstance(funcionario.codigo, int)):
            super().remove(funcionario.codigo)
