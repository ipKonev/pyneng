# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
#a=[int(i) for i in input('Enter ip: ').split('.')]
a=input('Enter ip: ')
#a.count('.')
#a.split('.')
b=[int(i) for i in a.split('.') if i.isdigit()]
#for i in [int(i) for i in a.split('.')]
if a.count('.') == 3 and len(b) == 4:
    if (b[0] in range(256)):
        if b[0]==b[1]==b[2]==b[3]==255:
            print('local broadcast')

        elif b[0]==b[1]==b[2]==b[3]==0:
            print('unassigned')

        elif b[0] not in range(1,224):
            if b[0] in range(224,240):
                print('multicast')
            else:
                print('unused')
        else:
            print('unicast')
    else:

        print('Неправильный IP-адрес')
else:
    print('Неправильный IP-адрес')
