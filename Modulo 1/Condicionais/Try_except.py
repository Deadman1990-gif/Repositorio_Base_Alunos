def divide(x,y):
    try:
        result=x/y
    except ZeroDivisionError:
        print("Por favor, não utilize zros!")
    except:
        print("\033[91m Algo deu errado...")
    else:
        print(f"seu resultado é:{result}")
    finally:
        print("\033[92m vamos de novo?]")
divide(13,0)
divide("x", "1")
divide("a", "e")
divide(-56,-54)
divide(3,3,3)