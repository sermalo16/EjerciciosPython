import string
from ntpath import join
from tokenize import String

def hanoi(n,po,pd,pt):
    if(n>1):
        hanoi(n-1,po,pt,pd)
    print(n,po,pd)
    if(n>1):
        hanoi(n-1,pt,pd,po)

ls = ['hola', 'mundo', 'loco']
print(String.join(ls))

