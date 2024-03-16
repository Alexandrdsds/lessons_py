# -*- coding: utf-8 -*-
from pprint import pprint
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
list_mac = []
with open('CAM_table.txt') as f:
    for line in f:
        lines = line.split()
        if lines and lines[0].isdigit():
            vlan, mac, _, interface = lines
            list_mac.append([vlan,mac,interface])
           
enter = input("Enter VLAN number: ")
for vlan,mac,interface in sorted(list_mac):
    if enter == vlan:
        print(f"{vlan:<9}{mac:20}{interface}")
    
