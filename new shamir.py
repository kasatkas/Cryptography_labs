import numpy as np
import cryptolib as cl

abc= "ЛЮШРОМЭЫИФНЙАЕЪЖУЬДЯБГТПЗВЦХЧСЩК"

p = 4957
q = 173
n = p*q
S =  303117
  
answ = []
arr = [445040, 396719, 439271, 590869, 556063, 100771, 765271, 396832, 722791, 769361, 535195, 490911, 417161, 470638, 580843]
for i in range (len(arr)):
    for z in range(2,n-1):
        if(z*S%n==arr[i]):
            if(z>arr[i]): answ.append("1")
            else: answ.append("0")

answ = np.array(answ, dtype=int)
answ.resize(3,5)

print("".join(str(cl.num_to_word(abc, s)) for s in answ))