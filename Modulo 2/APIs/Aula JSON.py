import json
dados_json='{"nome": "Pedro Wayne", "idade":15, "cidade": "Gotham City"}'
dados_python= json.loads(dados_json)
print(dados_python["nome"])
print(dados_python["idade"])
print(dados_python["cidade"])
pythonValue={'isCat':True, 'miceCaught':1, 'name': 'Thomas the Cat', 'felineIQ':None, 'Height': '1.35', 'Weight': '30KG', 'behavior': 'Docil', 'eye color': 'preto', 'fur color': 'Azul com cinza e branco', 'favorite thing': 'caçar ratos', 'Genero': 'Macho', 'Raça': 'Gato domestico', 'idade': '35', 'tutor': 'Ricky e Ginger'}
stringOfJsonData=json.dumps(pythonValue)
print(stringOfJsonData)