from Questao2.Pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, salario, matricula, nome, idade, genero):
        super(Funcionario, self).__init__(nome, idade, genero)
        self.salario = salario
        self.matricula = matricula

    def calcularINSS(self, salario):
       self.inss = salario/0.11
       return self.inss

