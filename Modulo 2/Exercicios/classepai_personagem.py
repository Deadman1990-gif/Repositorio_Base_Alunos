class Personagem:
    def __init__(self, nome, programa, Altura, Peso, cor):
        self.nome=nome
        self.programa=programa
        self.Altura=Altura
        self.Peso=Peso
        self.cor=cor
    def falar(self):
        print(f"{self.nome} está falando")
    def andar(self):
        print(f"{self.nome} está andando")
    def comer(self):
        print(f"{self.nome} está comendo")
    def beber(self):
        print(f"{self.nome} está bebendo água")
    def brincar(self):
        print(f"{self.nome} está brincando com o cachorro")