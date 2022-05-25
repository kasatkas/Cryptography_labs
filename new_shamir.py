"""
B идентифицирует A с помощью протоколоа, аналогичного Фиата-Шамира (на пером шаге выбираются два z: z_1>(z_1*S)modn и z_2<(z_2*S)modn; на третьем
шаге выбирается (z_1*S)modn при c=1 и (z_2*S)modn при c=0). Известны значения третьего шага для каждого из циклов 1)445040, ..., 15)580843.
На втором шаге каждого из циклов B выбирает случайный бит из некоторого слова. Определить это слово, а также секретный ключ S, если последний
одновременно равен 7766 по модулю 11878, 7668 по модулю 16719, 1019 по модулю 25985. p=4987, q = 191.
"""

import numpy as np
import cryptolib as cl

abc= "ЛЮШРОМЭЫИФНЙАЕЪЖУЬДЯБГТПЗВЦХЧСЩК"

arr = [640734, 416588, 132705, 151135, 534161, 912962, 89132, 311464, 888813, 772479, 931810, 738556, 590114, 424608, 202862]
a, m = [7766, 7668, 1019], [11878, 16719, 25985]
p, q = 4987, 191

n = p*q
S =  cl.chineese_remainder_theorem(a, m)
#print("".join(ch for ch in cl.num_to_word(abc, cl.zero_fill(list(cl.toBin(S)), 20))))  #для проверки S

answ = []
for i in range (len(arr)):
    for z in range(2,n-1):
        if(z*S%n==arr[i]):
            if(z>arr[i]): answ.append("1")
            else: answ.append("0")

answ = np.array(answ, dtype=int)
answ.resize(3,5)

print("".join(str(cl.num_to_word(abc, s)) for s in answ))