from copy import copy
import numpy as np

def help():
    print("Обратное по модулю: rev_mod(b, n)"
      + "\nЧисло в двоичный вид: toBin(x)"
      + "\nЧисло в десятичный вид: toDec(list)"
      + "\nСдвиг из начала в конец num раз: shiftF2E(list, num)"
      + "\nСдвиг из конца в начало num раз: shiftE2F(list, num)"
      + "\nДополнение 0 в начало до длины num: zero_fill(list, num)"
      + "\nМассив слова в массив 0 и 1: word_to_num(abc, list)"
      + "\nМассив 0 и 1 в слово: num_to_word(abc, list)"
      + "\nИнверсия массива 0 и 1: inverse(list)"
      + "\nЛогическое И: OR(arr1, arr2)"
      + "\nЛогическое ИЛИ: XOR(arr1, arr2)" )

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

def rev_mod(b, n):
    g, x, _ = egcd(b, n)
    #print('w = ', x)
    if g == 1:
        return x % n

def toBin(x):
    x = int(x)
    n = ""
    while x > 0:
        y = str(x % 2)
        n = y + n
        x = int(x / 2)
    return n

def toDec(list):
    number = 0
    len_dat = len(list)
    for i in range(0, len_dat):
        number += int(list[i]) * (2**(len_dat - i -1))
    return number

def shiftF2E(list, num): # из начала в конец num раз
    out = copy(list)
    for i in range(num):
        out.append((out.pop(0)))
    return out

def shiftE2F(list, num): # из конца в начало num раз
    out = copy(list)
    for i in range(num):
        out.insert(0,out.pop())
    return out

def zero_fill(list, num):
    while (len(list)!=num): list.insert(0, '0')
    return list

def word_to_num(abc, list):
    new_list = []
    for i in range(len(list)):
        new_list.append(abc.index(list[i]))
    return new_list

def num_to_word(abc, list): #из массива 0 и 1 в слово
    word = []
    new_list = []
    lengh = int(len(list)/5)
    tmp = np.array(list)
    tmp.resize(lengh, 5)
    for i in range(lengh):
        word.append(toDec(tmp[i]))
    for i in range(len(word)):
        new_list.append(abc[word[i]])
    return new_list

def inverse(list):
    out = []
    for i in range(len(list)):
        if(list[i]==1): out.append(0)
        else: out.append(1)
    return out

def OR(arr1, arr2):
    out = []
    for i in range(len(arr1)):
        if(int(arr1[i])+int(arr2[i])==0):
            out.append(0)
        else: out.append(1)
    return out

def XOR(arr1, arr2):
    out = []
    for i in range(len(arr1)):
        if(int(arr1[i])+int(arr2[i])==0 or int(arr1[i])+int(arr2[i])==2):
            out.append(0)
        else: out.append(1)
    return out