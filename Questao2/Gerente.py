from Questao2.Funcionario import Funcionario

class Gerente(Funcionario):
    def __init__(self, salario, matricula, nome, idade, genero, nomeGerencia):
        super(Gerente, self).__init__(nome, idade, genero, salario, matricula)
        self.nomeGerencia = nomeGerencia
