from Questao2.Funcionario import Funcionario
from Questao2.Cliente import Cliente
from Questao2.Gerente import Gerente
from Questao2.Vendedor import Vendedor
from Questao2.Pessoa import Pessoa

def main():

    p1 = Pessoa("Lucas", 22, "Masculino")
    f1 = Funcionario(200.50, 201510, "Jonata", 20,"Masculino")
    g1 = Gerente(500.96, 201315, "Luana", 29, "Feminino", "Markenting")
    v1 = Vendedor(350, 201701, "Amanda", 18, "Feminino", 1002.52, "navio")
    c1 = Cliente("1990", "Manoel", 27, "Masculino")

    print(p1)

    f1.calcularINSS(200.50)
    print(f1)

    g1.calcularINSS(500.96)
    print(g1)

    v1.calcularINSS(350)
    print(v1)

    print(c1)