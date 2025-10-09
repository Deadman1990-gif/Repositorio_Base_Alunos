class Pessoa:
    def __init__(self, nome, altura, peso, sexo, comida_favorita, roupa, filme_favorito, musica_favorita, esporte_favorito, Cor_favorita):
        self.__nome=nome
        self._altura=altura
        self._peso=peso
        self.__sexo=sexo
        self.__comida_favorita=comida_favorita
        self._roupa=roupa
        self.__filme_favorito=filme_favorito
        self.__musica_favorita=musica_favorita
        self._esporte_favorito=esporte_favorito
        self.__Cor_favorita=Cor_favorita
    def fazer_comida(self):
        print(f"{self.nome} está fazendo feijoada")
    def Assistir_filme(self):
        print(f"{self.nome} esta assistindo Batman")
    def Se_vestir(self):
        print(f"{self.nome} esta trocando de roupa")
    def Andar(self):
        print(f"{self.nome} esta andando na rua")
    def Respirar(self):
        print(f"{self.nome} esta respirando")
    def escutando(self):
        print(f"{self.nome} esta escutando Rock n' Roll")
    def tocando(self):
        print(f"{self.nome} esta tocando bateria no KISS")
    def observando(self):
        print(f"{self.nome} esta observando o show do Iron Maiden")
    def gostar(self):
        print(f"{self.nome} esta gostando de alguem")
    def não_gostar(self):
        print(f"{self.nome} não esta gostando de fazer lição")
pessoa1=Pessoa("Ricky", "1.60", "80Kg", "masculino", "Macarrão", "Blusa Azul e Calça", "O show de Tom e Jerry", "The Tom And Jerry Show Theme", "Ficar sentado", "Azul")
pessoa1.fazer_comida()

@property
def nome (self):
    return self.__nome

@property
def altura (self):
    return self._altura

@property
def peso (self):
    return self._peso

@property
def sexo (self):
    return self.__sexo

@property
def comida_favorita (self):
    return self.__comida_favorita

@property
def roupa (self):
    return self._roupa

@property
def filme_favorito (self):
    return self.__filme_favorito

@property
def musica_favorita (self):
    return self.__musica_favorita

@property
def esporte_favorito (self):
    return self._esporte_favorito

@property
def Cor_favorita (self):
    return self.__Cor_favorita

@nome.setter
def nome(self,valor):
    self._nome=valor

@altura.setter
def altura(self,valor):
    self._altura=valor

@peso.setter
def peso(self,valor):   
    self._peso=valor

@sexo.setter
def sexo(self,valor):
    self._sexo=valor

@comida_favorita.setter
def comidas_favorita(self,valor):
    self._comida_favorita=valor

@roupa.setter
def roupa(self,valor):
    self._roupa=valor

@filme_favorito.setter
def filme_favorito(self,valor):
    self._filme_favorito=valor

@musica_favorita.setter
def musica_favorita(self,valor):
    self._musica_favorita=valor

@esporte_favorito.setter
def esporte_favorito(self,valor):
    self._esporte_favorito=valor

@Cor_favorita.setter
def Cor_favorita(self,valor):
    self._Cor_favorita=valor


