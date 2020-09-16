import requests

BASE_URL = 'http://127.0.0.1:5000'

print("POST")
response = requests.post(f'{BASE_URL}/fair/1', {'latitude': '9999999999', 'longitude': '-9999999999', 'setcens': 'ABC'})
print(response.json())
response = requests.post(f'{BASE_URL}/fair/2', {'latitude': '8888888888', 'longitude': '-8888888888', 'setcens': 'DEF'})
print(response.json())
response = requests.post(f'{BASE_URL}/fair/3', {'latitude': '7777777777', 'longitude': '-7777777777', 'setcens': 'GHI'})
print(response.json())
response = requests.post(f'{BASE_URL}/fair/4', {'latitude': '6666666666', 'longitude': '-6666666666', 'setcens': 'JKL'})
print(response.json())
response = requests.post(f'{BASE_URL}/fair/5', {'latitude': '5555555555', 'longitude': '-5555555555', 'setcens': 'MNO'})
print(response.json())
response = requests.post(f'{BASE_URL}/fair/6', {'latitude': '4444444444', 'longitude': '-4444444444', 'setcens': 'PQR'})
print(response.json())
response = requests.post(f'{BASE_URL}/fair/7', {'latitude': '3333333333', 'longitude': '-3333333333', 'setcens': 'STU'})
print(response.json())
response = requests.post(f'{BASE_URL}/fair/8', {'latitude': '2222222222', 'longitude': '-2222222222', 'setcens': 'VWX'})
print(response.json())
response = requests.post(f'{BASE_URL}/fair/2', {'latitude': '5555555555', 'longitude': '-5555555555', 'setcens': 'MNO'})
print(response.json())


print("PUT")
response = requests.put(f'{BASE_URL}/fair/1', {'latitude': '1111111111'})
print(response.json())
response = requests.put(f'{BASE_URL}/fair/4', {'setcens': 'XYZ'})
print(response.json())


print("DELETE")
response = requests.delete(f'{BASE_URL}/fair/3')

print("GET")
response = requests.get(f'{BASE_URL}/fair/1')
print(response.json())
response = requests.get(f'{BASE_URL}/fair/2')
print(response.json())
response = requests.get(f'{BASE_URL}/fair/3')
print(response.json())
response = requests.get(f'{BASE_URL}/fair/4')
print(response.json())
response = requests.get(f'{BASE_URL}/fair/5')
print(response.json())

print("GET")
response = requests.get(f'{BASE_URL}/fairs?page=1')
print(response.json())
response = requests.get(f'{BASE_URL}/fairs?per_page=2&page=3')
print(response.json())
