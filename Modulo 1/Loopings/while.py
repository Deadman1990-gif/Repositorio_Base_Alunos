def tabuada():
    n = int(input("digite um numero:"))
    fim=int(input("digite o final:"))
    x=1
    while x <= fim:
        print(n, "x", "x", "=", x*n)
    x=x+1
print("-----------x-----------")
def whilebreak():
    s=0
    while True:
        v=int(input("digite um numero a somar ou 0 para sair:"))
        if v==0:
            break
        s=s+v
    print(s)
#whilebreak()
print("---------x----------")
def whilecomlista():
    l=[]
    while True:
        n=(input("digite uma palavra(0 sai):"))
        if n=="0":
            break
        l.append(n)
    x=0
    while x < len(l):
        print(l[x])
        x=x+1
    print(l)
whilecomlista()