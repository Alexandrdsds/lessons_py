# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

while True:
   ip_address = input("Введите ІР адрес: ")
   octets = ip_address.split('.')
   correct_ip = True

   if len(octets) != 4:
      correct_ip = False
   else:
      for octet in octets:
         if not(octet.isdigit() and int(octet) in range(256)):
            correct_ip = False
   if not correct_ip == True:
      print("Неправильный IP-адрес")
      
   else:
      if int(octets[0]) in range(1,224):
         print("unicast")
         break
      elif int(octets[0]) in range(224,240):
         print("multicast")
         break
      elif ip_address == "255.255.255.255":
         print("local broadcast")
         break
      elif ip_address == "0.0.0.0":
         print("unassigned")
         break
      else:
         print("unused")
         break