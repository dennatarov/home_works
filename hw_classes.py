# Задача-1
# У вас есть список(list) IP адрессов. Вам необходимо создать
# класс который будет иметь методы:
# 1) Получить список IP адресов
# 2) Получить список IP адресов в развернутом виде
# (10.11.12.13 -> 13.12.11.10)
# 3) Получить список IP адресов без первых октетов
# (10.11.12.13 -> 11.12.13)
# 4) Получить список последних октетов IP адресов
# (10.11.12.13 -> 13)

class AddressIP:
    def __init__(self, list_ip):
        self.__list_ip = list_ip

    @property
    def list_ip(self):
        return self.__list_ip

    def reversed_list_ip(self):
        ln_ip = []
        for ip in self.__list_ip:
            l_ip = ip.split('.')
            l_ip.reverse()
            ln_ip.append('.'.join(l_ip))
        return ln_ip

    def without_octs(self):
        return [ip.partition('.')[2] for ip in self.__list_ip]

    def last_octs(self):
        return [ip.rpartition('.')[2] for ip in self.__list_ip]

list_ip = ['10.11.12.13', '192.0.1.2', '172.19.18.192']

ips = AddressIP(list_ip)

# print(ips.list_ip)
# print(ips.reversed_list_ip())
# print(ips.without_octs())
# print(ips.last_octs())

# Задача-2
# У вас несколько JSON файлов. В каждом из этих файлов есть
# произвольная структура данных. Вам необходимо написать
# класс который будет описывать работу с этими файлами, а
# именно:
# 1) Запись в файл
# 2) Чтение из файла
# 3) Объединение данных из файлов в новый файл
# 4) Получить путь относительный путь к файлу
# 5) Получить абсолютный путь к файлу

import json
import os

class JsonProcessing:
    def __init__(self, list_of_jsons):
        self.list_of_jsons = list_of_jsons

    def json_read(self, file_name):
        with open(file_name, 'r') as r:
            return json.load(r)

    def json_add_dict(self, data: dict, file_name):
        """Add to json dictionary from file_name new keys from data and rewrite extended dictionary.
        Do not raise error if data in file and/or in data are not dict"""

        data_in_file = self.json_read(file_name)
        if type(data_in_file) is dict and type(data) is dict:
            if data_in_file.keys() & data.keys():
                print("NOTE: keys intersection is {}!\nAppropriate item(-s) in source updated!"
                      .format(data_in_file.keys() & data.keys()))
            with open(file_name, 'w') as w:
                json.dump({**data_in_file, **data}, w, indent=4)
        else:
            print("{} hasn't been changed! Data and file must be dicts.".format(file_name))

    def merge_json_list(self, new_file):
        """Merge data from .json files into a list and write it in new_file"""
        with open(new_file, 'w') as w:
            json.dump([self.json_read(file) for file in self.list_of_jsons], w, indent=4)

    def abs_path(self, file_name):
        return os.path.abspath(file_name)

    def rel_path(self, file_name):
        return os.path.relpath(file_name)

jsons = JsonProcessing(["first.json", "second.json", "third.json"])

# data_test = ["A long-long string", 1, 2, 3, 4, 5]
dict_for_test = {
    'active': {
        'name': 'Zaphod Beeblebrox',
        'species': 'Betelgeusian'
    }
}

# jsons.json_add_dict(dict_for_test, jsons.list_of_jsons[0])
# print(jsons.json_read(jsons.list_of_jsons[0]))
# jsons.merge_json_list("merged.json")
# print(jsons.abs_path(jsons.list_of_jsons[2]))

# Задача-3
#
# Создайте класс который будет хранить параметры для
# подключения к физическому юниту(например switch). В своем
# списке атрибутов он должен иметь минимальный набор
# (unit_name, mac_address, ip_address, login, password).
# Вы должны описать каждый из этих атрибутов в виде гетеров и
# сеттеров(@property). У вас должна быть возможность
# получения и назначения этих атрибутов в классе.

class UnitConnectionInfo:
    def __init__(self, unit_name, mac_address, ip_address, login, password):
        self._unit_name = unit_name
        self._mac_address = mac_address
        self._ip_address = ip_address
        self._login = login
        self._password = password

    @property
    def unit_name(self):
        return self._unit_name

    @unit_name.setter
    def unit_name(self, new_name):
        self._unit_name = new_name

    @property
    def mac_address(self):
        return self._mac_address

    @mac_address.setter
    def mac_address(self, new_addr):
        self._mac_address = new_addr

    @property
    def ip_address(self):
        return self._ip_address

    @ip_address.setter
    def ip_address(self, new_ip):
        self._ip_address = new_ip

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, new_login):
        self._login = new_login

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_pswrd):
        self._password = new_pswrd

# unit_1 = UnitConnectionInfo("Modem_01", "148.17.17.17", "178.0.0.1", "modem01", "password")
# unit_2 = UnitConnectionInfo("Modem_02", "153.325.812.0", "168.168.178.178", "modem02", "password")