"""
Устройство связи каждого из четырёх абонентов сети содержит два набора встроенных констант:
[f0 = 9...f11 = 14810]
[u(0) = 1...u(11) = 11620]
С их помощью устройство связи вычисляет сетевой ключ абонента по принципу m_2^10 +  m_3^10 + m_4^10 - 28671857656, 
где m_2, m_3, m_4 - степенни ЛРП,используемые тремя другими абонентами, соответственно в поле(0..34359738367). 
Рассчитать сетевой ключ, если известно, что 
u(12) второго абонента: ЪПЖЦБТЫ, u(12) третьего абонента: ЭТКНЫХГ, u(12) четвертого абонента: ТВДСПЫШ.
"""

import cryptolib as cl

abc = "ЭНОЯШТКГФЮЪМЬХЕЧУДРВЛПЦИАЩЙЖЫЗСБ"
pole = 34359738367

# Задача 45
F = [9, 17, 7, 3, 10, 1, 8, 100, 148, 115, 1494, 14810]
U = [1, 13, 18, 18, 2, 15, 20, 156, 196, 152, 1319, 11620, 0]
words = ["ЪПЖЦБТЫ", "ЭТКНЫХГ", "ТВДСПЫШ"] # Ответ 8 12 5
cnst = -28671857656

mas = []
for j in range(len(words[0])):
    mas += cl.zero_fill(list(cl.toBin(int(cl.word_to_num(abc, words[0])[j]))), 5)

mas = []
M = list(range(3))
for i in range(len(words)):
    for j in range(len(words[i])):
        mas += cl.zero_fill(list(cl.toBin(int(cl.word_to_num(abc, words[i])[j]))), 5)
    M[i] = "".join(str(cl.toDec(list(mas))))
    mas = []

print(M)

u = U.copy()
U12 = list(range(12))
for m in range (3,13):
    i=0
    t=m
    while t<13:
        u[t] = 0
        for j in range(m):
            u[t] += F[j]*u[j+i]
        i+=1
        t+=1
    U12[m-1] = u[12]
    u = U.copy()

for i in range(12):
    print(i+1, U12[i])

print("Если не выдаст нормальное слово, попробуй другие индексы. Для выхода Ctrl+C.")
while True:
    rez = (int(input("Индекс примерно похожего или такого же числа: "))**10 + int(input("Второе:"))**10 + int(input("Третье:"))**10 + cnst)%pole
    print(cl.num_to_word(abc, cl.zero_fill(list(cl.toBin(rez)), 35)))