def lê_binário():
    try:
        with open("binary.jpg" ,"rb") as fs1:
            dados=fs1.read()
            print(type(dados))
        with open("cópia.jpg" ,"wb") as fs2:
            fs2.write(dados)
    except FileNotFoundError as e:
        fs1.write(dados)
    except IOError as e:
        print('Deu algo errado') 
        print("Ok!")
lê_binário()
