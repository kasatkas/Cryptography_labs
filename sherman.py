"""
Рассчитать открытый ключ по секретному ключу n = РУДА, если он равен сумме всех возможных (a-eplislon*b)
при epsilon = {-1}, для которых (a-eplislon*b, n) - искомый нетривиальный делитель n по алгоритмы Шермана-Лемана.
"""

import cryptolib as cl
import math as m

""" #Задача №
abc = "ДЪКУЮОАМЬЭЕНГХИЙВТЦБЯПФЧЗЖЛЫРШЩС"
key = "СЛОН" """

#Задача №
abc = "ДЯКШЮЪТМЬЭЕНГХИАВЙЩБОПФЧЗЖЛЫСУЦР"
key = "РУДА"

epsilon = -1
n=""
A_arr, B_arr = [],[]
rez = 0

key = cl.word_to_num(abc, list(key))

for i in range(len(key)):
    n+="".join(cl.zero_fill(list(cl.toBin(int(key[i]))),5))
n = cl.toDec(list(n))

k_max = int(n**(1/3))
k = range(1,k_max), 
d_max = int(n**(1/6)/(4*m.sqrt(k[0]))) + 1
d = range(1,d_max)

for d in range(1, d_max+1):
    for k in range(1, k_max+1):
        a = int(m.sqrt(4*k*n)) + d
        x = a*a - 4*k*n
        if(x>0):
            B = m.sqrt(x)
            if(B.is_integer()):
                A_arr.append(a)
                B_arr.append(int(B))

for i in range(len(A_arr)):
    rez+= A_arr[i]-epsilon*B_arr[i]

print(cl.num_to_word(abc, cl.zero_fill(list(cl.toBin(int(rez))),20)))