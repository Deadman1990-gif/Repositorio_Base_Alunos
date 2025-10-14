este_dicionario= {"marca": "chevrolet",
                  "modelo": "Opala",
                  "ano": 1969
}
print(len(este_dicionario))

from classe_pai import Animal
from classes_ex_01 import AnimaisMarinhos
from classe_pássaro import Passaro

animal1= Animal(23_000_000, "Megalodon", 18.00, "Rei dos Oceanos")
animal2= AnimaisMarinhos(77, "Seu Sirigueijo", 1.64, "Dono do Siri Cascudo")
animal3= Passaro(20, "DeadBird", 0.70, "Animal de estimação do Undertaker")

def comunicar(qualquer_animal):
    print(f"tentando_comunicar com {qualquer_animal.espécie}")
    qualquer_animal.fazer_som()

print("-"*50)
comunicar(animal1)

print("-"*50)
comunicar(animal2)

print("-"*50)
comunicar(animal3)