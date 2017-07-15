from Questao3.Pessoa import Pessoa

class Fornecedor(Pessoa):
    def __init__(self, nome, endereco, telefone, valorCredito, valorDivida):
        super(Fornecedor, self).__init__(nome, endereco, telefone)
        self.valorCredito = valorCredito
        self.valorDivida = valorDivida

    def obterSaldo(self):
        valorTotal = self.valorCredito - self.valorDivida
        return valorTotal