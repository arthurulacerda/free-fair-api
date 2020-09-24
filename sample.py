import requests
import json
BASE_URL = 'http://127.0.0.1:5000'


print("POST")
response = requests.post(f'{BASE_URL}/v1/fair', {"longitude": "-46550164", "latitude": "-23558733", "setcens": "355030885000091", "areap": "3550308005040", "coddist": "87", "distrito": "VILA FORMOSA", "codsubpref": "26", "subpref": "ARICANDUVA-FORMOSA-CARRAO", "regiao5": "Leste", "regiao8": "Leste 1", "nome_feira": "VILA FORMOSA", "registro": "4041-0", "logradouro": "RUA MARAGOJIPE", "numero": "S/N", "bairro": "VL FORMOSA", "referencia": "TV RUA PRETORIA"})
print(response.json())
response = requests.post(f'{BASE_URL}/v1/fair', {'latitude': '888888888', 'longitude': '-888888888', 'distrito': 'DEF', 'bairro': '001'})
print(response.json())

print("PUT")
response = requests.put(f'{BASE_URL}/v1/fair/10', {'latitude': '111111111'})
print(response.json())
response = requests.put(f'{BASE_URL}/v1/fair/14', {'setcens': 'XYZ'})
print(response.json())


print("DELETE")
response = requests.delete(f'{BASE_URL}/v1/fair/12')
print(response.json())

print("GET")
response = requests.get(f'{BASE_URL}/v1/fair/1')
print(response.json())
response = requests.get(f'{BASE_URL}/v1/fair/2')
print(response.json())
response = requests.get(f'{BASE_URL}/v1/fair/3')
print(response.json())
response = requests.get(f'{BASE_URL}/v1/fair/4')
print(response.json())
response = requests.get(f'{BASE_URL}/v1/fair/5')
print(response.json())

print("GET")
response = requests.get(f'{BASE_URL}/v1/fair?page=1000')
print(response.json())
response = requests.get(f'{BASE_URL}/v1/fair?distrito=XXX&bairro=002')
print(response.json())
