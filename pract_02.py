def bigger_price(n, products):
    products.sort(key=lambda dic: dic['price'], reverse=True)
    print([products[i] for i in range(n)])

bigger_price(2, [
{"name": "bread", "price": 100},
{"name": "wine", "price": 138},
{"name": "meat", "price": 15},
{"name": "water", "price": 1}
])

#================================================================

import requests
import json

def list_of_names(imported):
    return [elem['name'] for elem in imported]

def names_weapons(imported):
    return {elem['name']: elem['weapon'] for elem in imported if elem['weapon'] is not ''}

data = json.loads(requests.get("https://lego-super-heroes.herokuapp.com/").text)
print(list_of_names(data))
print(names_weapons(data))

# Eсть адрес https://lego-super-heroes.herokuapp.com/
# Вам необходимо собрать все имена героев в лист и вернуть его
# Собрать имена всех героев и их оружие и вернуть в виде {name: weapon} только для тех у кого есть оружие