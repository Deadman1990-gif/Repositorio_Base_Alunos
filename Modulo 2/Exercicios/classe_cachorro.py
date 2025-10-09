from classe_pai import Animal

class Cachoro(Animal):
    def __init__(self, nome, raça):
        super().__init__(nome)
        self.raça=raça
    def fazer_som(self):
        print(f"{self.nome} está latindo: Au Au!")
    def abanar_rabo(self):
        print(f"{self.nome} está tocando bateria no show do KISS")

animall=Cachoro("Spike", "Pitbull")
animall.comer()
animall.abanar_rabo()
animall.fazer_som()