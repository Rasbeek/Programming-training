#Импорт фреймфорка pytest
import pytest

#Импорт библиотеки requests
import requests

#Вывод списка всех доступных питомцев
status = 'available'

res = requests.get(f'https://petstore.swagger.io/v2/pet/findByStatus?status={status}', headers={'accept':'application/json'})

#Вывод кода запроса
print(res.status_code)

#Создание нового питомца
headers = {'accept': 'application/json', 'Content-Type': 'application/json'}

data = {"id": 9223372036854741000, "category": {"id": 0, "name": "string"},
    "name": "Jhon", "photoUrls": ["string"], "tags": [{"id": 0, "name": "string"}],
    "status": "available"}

res = requests.post(f'https://petstore.swagger.io/v2/pet', headers=headers, json=data)

#Вывод кода твета и данных о питомце запроса
print(res.status_code)
print(res.json)

#Изменение данных питомца
headers = {'accept': 'application/json', 'Content-Type': 'application/json'}

data = {"id": 9223372036854741000, "category": {"id": 0, "name": "string"}, "name": "SARAH", "photoUrls": ["string"],
    "tags": [{"id": 0, "name": "string"}], "status": "available"}

res = requests.put(f'https://petstore.swagger.io/v2/pet', json=data)

#Вывод кода твета и данных о питомце запроса
print(res.status_code)
print(res.json)

#Удаление данных питомца
res = requests.delete(f'https://petstore.swagger.io/v2/pet/{9223372036854741000}', headers={'accept':'application/json'})

#Вывод кода твета и данных о питомце запроса
print(res.status_code)
print(res.json)

#Вывод списка всех доступных питомцев
status = 'available'

res = requests.get(f'https://petstore.swagger.io/v2/pet/findByStatus?status={status}', headers={'accept':'application/json'})

#Вывод кода запроса
print(res.status_code)