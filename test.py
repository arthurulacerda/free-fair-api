import requests

BASE_URL = 'http://127.0.0.1:5000'


print("POST")
response = requests.post(f'{BASE_URL}/v1/fair', {'latitude': '999999999', 'longitude': '-999999999', 'distrito': 'ABC', 'bairro': '001'})
print(response.json())
response = requests.post(f'{BASE_URL}/v1/fair', {'latitude': '888888888', 'longitude': '-888888888', 'distrito': 'DEF', 'bairro': '001'})
print(response.json())
response = requests.post(f'{BASE_URL}/v1/fair', {'latitude': '777777777', 'longitude': '-777777777', 'distrito': 'ABC', 'bairro': '001'})
print(response.json())
response = requests.post(f'{BASE_URL}/v1/fair', {'latitude': '666666666', 'longitude': '-666666666', 'distrito': 'ABC', 'bairro': '002'})
print(response.json())
response = requests.post(f'{BASE_URL}/v1/fair', {'latitude': '555555555', 'longitude': '-555555555', 'distrito': 'DEF', 'bairro': '002'})
print(response.json())
response = requests.post(f'{BASE_URL}/v1/fair', {'latitude': '444444444', 'longitude': '-444444444', 'distrito': 'DEF', 'bairro': '002'})
print(response.json())
response = requests.post(f'{BASE_URL}/v1/fair', {'latitude': '333333333', 'longitude': '-333333333', 'distrito': 'STU', 'bairro': '002'})
print(response.json())
response = requests.post(f'{BASE_URL}/v1/fair', {'latitude': '222222222', 'longitude': '-222222222', 'distrito': 'DEF', 'bairro': '002'})
print(response.json())
response = requests.post(f'{BASE_URL}/v1/fair', {'latitude': '555555555', 'longitude': '-555555555', 'distrito': 'MNO', 'bairro': '002'})
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
response = requests.get(f'{BASE_URL}/v1/fair?page=1')
print(response.json())
response = requests.get(f'{BASE_URL}/v1/fair?distrito=XXX&bairro=002')
print(response.json())
