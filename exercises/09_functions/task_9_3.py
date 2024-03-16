# -*- coding: utf-8 -*-
from pprint import pprint
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный
файл коммутатора и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов,
  а значения access VLAN (числа):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов,
  а значения список разрешенных VLAN (список чисел):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент
имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

def get_int_vlan_map(config_filename):
    acces_port = {}
    trunk_port = {}
    with open(config_filename,'r') as f:
        for line in f:
            if line.startswith("interface"):
                interface = line.split()[1]
            elif line.startswith(" switchport access vlan"):
                access_vlan = line.split()[3]
                acces_port[interface] = int(access_vlan)
            elif line.startswith(" switchport trunk allowed vlan"):
                trunk_vlan = line.split()[4].split(',')
                vlan_list = [int(v) for v in trunk_vlan]
                trunk_port[interface] = vlan_list
    return acces_port, trunk_port
                
pprint(get_int_vlan_map('config_sw1.txt'))