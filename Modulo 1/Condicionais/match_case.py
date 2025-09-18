import random
value=random.randint(0, 2)
match value:
    case 0:
        print("zero!")
    case 1:
        print("um!")
    case _:
        print("Inesperado!")