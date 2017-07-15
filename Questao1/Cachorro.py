from Questao1.Animal import Animal

class Cachorro(Animal):
    def __init__(self, nome, peso, habitat, raca):
        super(Cachorro, self).__init__(nome, peso, habitat)
        self.raca = raca

    def brincar(self):
        print("%s cachorro brincando" % self.nome)

    def vigiar(self):
        print("%s cachorro vigiando" % self.nome)

    def __str__(self):
        return (" Nome: %s\n Peso: %.2f Kg\n Habitat: %s\n Raça: %s"%(self.nome, self.peso, self.habitat, self.raca))
