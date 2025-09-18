import types

def diz_o_tipo(a):
  tipo = type(a)
  if tipo == str:
    return("String")
  elif tipo == list:
    return("Lista")
  elif tipo == dict:
    return("Dicionário")
  elif tipo == int:
    return("Número inteiro")
  elif tipo == float:
    return("Número decimal")
  elif tipo == types.FunctionType:
    return("Função")
  elif tipo == types.BuiltinFunctionType:
    return("Função interna")
  else:
    return(str(tipo))

dicionario={"batata":2.00,
            "cenoura":12.33}
def a():
  return
print(diz_o_tipo("Alô"))
print(diz_o_tipo(12))
print(diz_o_tipo(2.34))
print(diz_o_tipo([1,2,3,4]))
print(diz_o_tipo(dicionario))
print(diz_o_tipo(a))
print(diz_o_tipo(len))
print(diz_o_tipo(((1,2,3))))
