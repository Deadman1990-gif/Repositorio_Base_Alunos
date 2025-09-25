import requests
#response=requests.get("https://www.google.com/?hl=pt_BR&zx=1758627687364&no_sw_cr=1")
#print(response.status_code)
#print(response.text)

usuario={
    "name": "Pedro Henrique",
}

#response=requests.post('https://68d00787ec1a5ff338263f44.mockapi.io/cidade/Cidadaos',json=usuario)

response=requests.delete('https://68d00787ec1a5ff338263f44.mockapi.io/cidade/Cidadaos/5')
print(response.status_code)
print(response.json())