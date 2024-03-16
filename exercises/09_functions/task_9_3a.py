# -*- coding: utf-8 -*-
from pprint import pprint
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта
выглядит так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
def get_int_vlan_map(config_filename):
    acces_port = {}
    trunk_port = {}
    with open(config_filename,'r') as f:
        for line in f:
            if line.startswith("interface FastEthernet"):
                interface = line.split()[1]
                acces_port[interface] = 1
            elif line.startswith(" switchport access vlan"):
                access_vlan = line.split()[3]
                acces_port[interface] = int(access_vlan)
            elif line.startswith(" switchport trunk allowed vlan"):
                vlans = [int(v) for v in line.split()[4].split(',')]
                trunk_port[interface] = vlans
                del acces_port[interface]
    return acces_port, trunk_port
                
pprint(get_int_vlan_map('config_sw2.txt'))