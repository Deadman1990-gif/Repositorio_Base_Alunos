def cachorrada():
    valor_total = 0
    raça = input("digite uma raça")
    raças = ['pug', 'pastor-alemão', 'labrador']
    if raça in raças:
        if raças == 'pug':
            valor_total=70.99
            print(valor_total)
        elif raça=='pastor-alemão':
            valor_total=120.99
            print(valor_total)
    else:
        print("atendimento não disponivel")
cachorrada()