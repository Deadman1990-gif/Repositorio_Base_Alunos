class Passaro():

    def __init__(self, habitat, tamanho, cores, especie, sexo): 
        self.tamanho=tamanho
        self.cores=cores
        self.especie=especie
        self.sexo=sexo
        self.habitat=habitat

    def cantar(self):
        return print(f'Sou um {self.especie} cantando uma bela canção 🎵')
    
    def voar(self):
        return print("Batendo as asas e: voando...")
    
    def fazer_som(self):
        return print(f"{self.especie} esta fazendo barulho")

passaro1=Passaro(0.14, ['Preto', 'Branco', 'Cinza'], 'Pardal', 'M', 'Floresta Amazônica')
passaro1.cantar()
passaro1.voar()
passaro1.fazer_som()

passaro2=Passaro(0.35, ['Preto', 'Cinza'], 'corvo', 'M', 'Cemitério')
passaro2.cantar()
passaro2.voar()
passaro2.fazer_som

passaro3=Passaro(0.55, ['Azul', 'Branco', 'Amarelo'], 'Arara', 'M', 'Rio de Janeiro')
passaro3.cantar()
passaro3.voar()
passaro3.fazer_som()

passaro4=Passaro(0.45, ['Marrom', 'Preto', 'Cinza'], 'Pombo', 'M', 'Ruas de São Paulo')
passaro4.cantar()
passaro4.voar()
passaro4.fazer_som()

    
    