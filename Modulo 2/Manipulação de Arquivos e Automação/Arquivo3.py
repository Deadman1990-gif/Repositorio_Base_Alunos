import os
os.getcwd()

#os.mkdir("g")
#os.mkdir("e")
#os.mkdir("f")



try:
    for n in range(1,50):
        os.chdir("pasta_1")
        arquivo=open("arquivo_.txt", "w")
        arquivo.write("Oi")
        arquivo.close()
        print(f"""\033[0;50m Pasta ' criada com sucesso! ;D""")
except FileNotFoundError:
    print(f"""\033[0;50m Pasta ' Não encontrada...@_@""")
except OSError:
    print(f"""\033[0;50m  'É um arquivo, não uma pasta !!!+_+""")