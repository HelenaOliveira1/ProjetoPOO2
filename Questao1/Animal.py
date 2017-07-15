class Animal():
    def __init__(self, nome, peso, habitat):
        self.nome = nome
        self.peso = peso
        self.habitat = habitat

    def mover(self):
        print("Animal se movendo!")

    def locomover(self):
        print("Animal se locomovendo!")

    def __str__(self):
        return (" Nome: %s\n Peso: %.2f Kg\n Habitat: %s"%(self.nome, self.peso, self.habitat))
