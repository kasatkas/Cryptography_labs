"""
B идентифицирует A по протоколу симметричного "запрос-ответ":ЭЬЧГРТЪЛЫЩЯНЦЛЛ в момент 
времени 4 часов 1 минут 41 секунд с id(B) = КОЛЫКЛЙСЗЫЬ. Найти id(a), если 
A идентифицирует B  по тому же протоколу: ЛДДФХТВВАШКЬЮВВЪ, причем E - шифр де ла Порта
"""

from math import floor

abc_col = list("РСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЖЗИЙКЛМНОП") #возможно будет другой алфавит, надо спрашивать, тогда придется менять и ниже
abc_up = abc_col[:16] #первая половина алфавита в виде массива
abc_down = ["".join(ch for ch in abc_col[16:])] #вторая половина алфавита в виде 1 элемента массива
abc = "АБВГДЕЖЗИЙКЛМНОП"

def shift(abc):
    abc.append(abc.pop(0))
    return abc

def get_index(index, ch):
    for i in range (16):
        if index==abc_down[i].index(ch):
            return i*2+1

for i in range(16):
    abc = shift(list(abc))
    abc_down.append(abc)

idB = "КОЛЫКЛЙСЗЫЬ"
first = "ЭЬЧГРТЪЛЫЩЯНЦЛЛ"
second = "ЛДДФХТВВАШКЬЮВВЪ"

idB = idB[2:8]
first = first[6:12]
second = second[4:]
key, idA = [], []
index = 0

for i in range (6):
    try:
        index = abc_up.index(idB[i])
        key.append(abc_col[get_index(index, first[i])-1])
    except  ValueError:
        index = abc_up.index(first[i])
        key.append(abc_col[get_index(index, idB[i])-1])

print("Недоключ: " + "".join(ch for ch in key))
key = list(input("Введите нормальное слово из строки выше: ").upper()*3)
key = key[4:len(second)+4]

for i in range (len(key)):
    index = abc_col.index(key[i])
    index = floor(int((index)/2))
    try:
        ind = abc_up.index(second[i])
        idA.append(abc_down[index][ind])
    except  ValueError:
        ind = abc_down[index].index(second[i])
        idA.append(abc_up[ind])

print("Ответ: " + "".join(ch for ch in idA))