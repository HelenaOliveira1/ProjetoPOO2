from Questao2.Funcionario import Funcionario
from Questao2.Produto import Produto

class Vendedor(Funcionario):
    def __init__(self, salario, matricula, nome, idade, genero, valorVendas, vendas):
        super(Funcionario, self).__init__(nome, idade, genero, salario, matricula)
        self.valorVendas = valorVendas
        self.vendas = [Produto(vendas)]
