loja_do_pedrao={"Bateria": [1002,2000.99],
         "Guitarra": [1233, 2000.99],
         "Baixo": [2312, 3000.99],
         "microfone": [23432, 100.99],
         "violao": [1232, 200.99],
         "teclado": [1423, 3000.99],
         "xilofone": [123, 20.98],
         "surdo": [132, 674.99],
         "arpa": [324, 456.99],
         "tambor": [123, 345.76],
         "birimbau": [1233, 65.99],
         "flauta": [1234, 123.99],
         "baquetas": [2123, 32451.99],
         "palhetas": [4132, 132.98],
         "fonebateria": [2134, 34.99],
         "luz de palco": [231, 232.00],
         "maquinadefumaça": [576, 786,99],
         "telao de fundo": [43, 534.97],
         "plataforma de palco": [890, 324,99],
         "bau de backstage": [45657, 12.99]}
sei_lá_oque=input("digite o produto")
venda = [[sei_lá_oque, int(input("digite a quantidade:"))] ]
total = 0
print("Vendas:\n")
for produto in venda:
    if produto:=loja_do_pedrao:
        print(loja_do_pedrao)
    
for operação in venda:
    produto, quantidade = operação 
    preço = loja_do_pedrao[produto][1] 
    custo = preço * quantidade
    print("%12s: %3d x %6.2f = %6.2f" %
		(produto, quantidade,preço,custo))
    loja_do_pedrao[produto][0] -= quantidade 
    total+=custo
else:
    print("insulficiente!")
print(" Custo total: %21.2f\n" % total)
print("Estoque:\n")
for chave, dados in loja_do_pedrao.items(): 
    print("Descrição: ", chave)
    print("Quantidade: ", dados[0])
    print("Preço: %6.2f\n" % dados[1])