# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

a = input("Введите адрес сети: ")

ip, mask = a.split("/")
oct0 = ip.split(".")
mask = int(mask)

oct1, oct2, oct3, oct4 = [
        int(oct0[0]),
        int(oct0[1]),
        int(oct0[2]),
        int(oct0[3]),
]

bin_mask = "1" * mask + "0" * (32 - mask)
m1, m2, m3, m4 = [
        int(bin_mask[0:8], 2),
        int(bin_mask[8:16], 2),
        int(bin_mask[16:24], 2),
        int(bin_mask[24:32], 2),
]

ip_output = f"""
Network:
    {oct1:<8}  {oct2:<8}  {oct3:<8}  {oct4:<8}
    {oct1:08b}  {oct2:08b}  {oct3:08b}  {oct4:08b}"""

mask_output = f"""
    Mask:
        /{mask}
        {m1:<8}  {m2:<8}  {m3:<8}  {m4:<8}
        {m1:08b}  {m2:08b}  {m3:08b}  {m4:08b}
        """

print(ip_output)
print(mask_output)
