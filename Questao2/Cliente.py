from Questao2.Pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nascimento, nome, idade, genero):
        super(Cliente, self).__init__(nome, idade, genero)
        self.nascimento = nascimento