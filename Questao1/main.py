from Questao1.Animal import Animal
from Questao1.Cachorro import Cachorro
from Questao1.Peixe import Peixe

def main():
    a1 = Animal("Steve", 54.5, "Floresta")
    c1 = Cachorro("Wev", 15.9, "Doméstico", "Hot Dog")
    p1 = Peixe("Nada", 5, "Mar", "Brilhante")

    a1.mover()
    a1.locomover()
    print(a1)

    c1.mover()
    c1.locomover()
    c1.brincar()
    c1.vigiar()
    print(c1)

    p1.mover()
    p1.locomover()
    print(p1)


if (__name__ == "__main__"):
    main()
