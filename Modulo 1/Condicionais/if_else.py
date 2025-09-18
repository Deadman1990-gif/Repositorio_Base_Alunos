def lula_ladrão():
    saldo=int(input("digite o saldo bancario"))
    saque=int(input("digite o valor de saque"))
    if saldo >=saque:
        sald-=saque
        print("voce realizou um saque comn sucesso", saldo)
    else:
        print("voce nao possui saldo suficiente para realizar essa operaçao", saldo)
#lula_ladrao()
def Lula_corintiano():
    saldo=int(input("deposite valor desejado"))
    pix=int(input("deposite o valor depositado"))
    saldo+=pix
    print("voce realizou o saque com sucesso", saldo)
#lula_corintiano()
def porcentagem():
    valor_parte=float(input("insira o valor parte:"))
    porcentagem=float(input("insira o valor da porcentagem"))
    
    if porcentagem<=0.0:
        print("insira um numero maior que 0")
    else:
        valor_total=valor_parte*(porcentagem/100)
        print(valor_total)
porcentagem()