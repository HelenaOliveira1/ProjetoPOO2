from Questao1.Animal import Animal
from Questao1.Calda import Calda

class Peixe(Animal):
    def __init__(self, nome, peso, habitat, tipoCalda):
        super(Peixe, self).__init__(nome, peso, habitat)
        self.tipoCalda = Calda(tipoCalda)

    def __str__(self):
        return (" Nome: %s\n Peso: %.2f Kg\n Habitat: %s\n Tipo calda: " % (self.nome, self.peso, self.habitat))
