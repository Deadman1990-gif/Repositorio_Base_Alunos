def lista1():
    L=[8,9,15,10,123,12345]
    for Pedro in L:
        print(Pedro)
#lista1()
def lista2():
    L=["Undertaker,Kane,big show,TripleH"]
    for s in L:
        for letra in s:
            print(letra)
#lista2()
def exibe_máximo():
    L=[1,7,2,4,123,-12432]
    minimo=L[0]
    for e in L:
        if e > minimo:
            minimo=e
    print(minimo)
#exibe_máximo()
def exibe_minimo():
    P=[312,234,564-321,-123]
    minimo=P[0]
    for e in P:
        if e < minimo:
            minimo=e
    print(minimo)
#exibe_minimo()
def forv():
    for v in range(10):
        print(v)
#forv()
def forv2():
    for v in range(5,8):
        print(v)
#forv2()
def fort3():
    for t in range(3,33,3):
        print(t,end=" ")
#fort3()
def combinaçao():
    nome="Pedro Wayne"
    idade=15
    grana=21354678999000.00
    print("%s tem %d anos e R$%f no bolso." % (nome,idade,grana))
    print("%12s tem %03d anos e R$5.2f no bolso." % (nome,idade,grana))
    print("%-12s tem %-3d anos e R$%-5.2f no bolso." % (nome,idade,grana))
combinaçao()