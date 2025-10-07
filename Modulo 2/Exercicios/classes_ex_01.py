class AnimaisMarinhos():
    def __init__(self, tem_escamas, especie, nome, sexo, cor):
        self.tem_escamas=tem_escamas
        self.especie=especie
        self.nome=nome
        self.sexo=sexo
        self.cor=cor

    def nadar_sem_lixo(self):
        return print(f'sou um {self.especie} que respira melhor')
    def nadar(self):
        return print(f'Sou um {self.especie} que esta nadando')
    def mergulhar(self):
        return (f'Sou um {self.especie} que está mergulhando')
    def observar(self):
        return print(f'Sou um {self.especie} que está observando') 
    def pular(self):
        return print(f'Sou um {self.especie} que está pulando')