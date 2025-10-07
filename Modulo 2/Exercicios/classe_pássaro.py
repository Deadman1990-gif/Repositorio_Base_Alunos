class passaro():

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

passaro1=passaro(0.14, ['Preto', 'Branco', 'Cinza'], 'Pardal', 'M', 'Floresta Amazônica')
passaro1.cantar()
passaro1.voar()
passaro1.habitat()

passaro2=passaro(0.35, ['Preto', 'Cinza'], 'corvo', 'M', 'Cemitério')
passaro2.cantar()
passaro2.voar()
passaro2.habitat()

passaro3=passaro(0.55, ['Azul', 'Branco', 'Amarelo'], 'Arara', 'M', 'Rio de Janeiro')
passaro3.cantar()
passaro3.voar()
passaro3.habitat()

passaro4=passaro(0.45, ['Marrom', 'Preto', 'Cinza'], 'Pombo', 'M', 'Ruas de São Paulo')
passaro4.cantar()
passaro4.voar()
passaro4.habitat()


    
    