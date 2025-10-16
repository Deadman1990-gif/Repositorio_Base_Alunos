from classes_ex_03 import Pessoa

class SalaDeAula:
    def __init__(self, numero: int, capacidade: int):
        self.numero=numero
        self.capacidade=capacidade
        print(f"Sala {self.numero} esta disponivel")
class Professor(Pessoa):
        def dar_aula(self,sala: SalaDeAula):
            print(f"O Prof. {self.nome} de {self.disciplina} esta dando aula na sala {sala.numero}.")

