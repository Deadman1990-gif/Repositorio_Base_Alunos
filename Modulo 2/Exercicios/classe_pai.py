class Animal:
    def __init__(self, nome):
        self.nome=nome

    def comer(self):
        print(f"{self.nome} está comendo")

    def fazer_som(self):
        print(f"{self.nome} está fazendo um som genérico")
