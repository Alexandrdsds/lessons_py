# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
with open('ospf.txt','r') as f:
    for line in f:
        expression_1 = line.replace(',', " ").replace("[","").replace("]","")[1::].split()
        output = "\n{:25} {}" * 5
        print(output.format(
            "Prefix", expression_1[0],
            "AD/Metric", expression_1[1],
            "Next-Hop", expression_1[3],
            "Last update", expression_1[4],
            "Outbound Interface", expression_1[5],
        ))