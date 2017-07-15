from Questao3.Pessoa import Pessoa
from Questao3.Fornecedor import Fornecedor
from Questao3.Funcionario import Funcionario

def main():

    a1 = Pessoa("Duda", "Dinamerica", 40028922)
    print(a1)

    a2 = Pessoa("Creança", "Lagoa NOVA", 12356)
    print(a2)

    f1 = Fornecedor("Creança", "Lagoa NOVA", 12356, 2555, 8485)
    f1.obterSaldo()

    func1 = Funcionario("Duda", "Dinamerica", 40028922, 52, 45, 11)
    func1.calcularSalarioTotal()

if __name__ == "__main__":
    main()