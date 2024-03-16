# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости
от выбранного режима, задавались разные вопросы в запросе о номере
VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]
choose_mode = input("Введите режим работы интерфейса: ")
port = input("Введите тип и номер интерфейса: ")
configrure_interface = {'access': {"mode": access_template,"desc":"Введите номер VLAN: "}, 'trunk': {"mode": trunk_template,"desc":"Введите разрешенные VLANы: "}}
vlan = input(configrure_interface[choose_mode]["desc"])
test = "\n".join(configrure_interface[choose_mode]["mode"]).format(vlan)
interface = f"interface {port}\n"
print(interface + test)
