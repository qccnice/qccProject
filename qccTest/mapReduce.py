# -*- coding: utf-8 -*-
from functools import reduce

def normalize(name):
    lowerStr=name.lower().title()
    return lowerStr

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize,L1))
print('结果：',L2)

def prod(L):
    def getres(x,y):
        return x*y
    return reduce(getres,L)
L = [1,2,3,4,5]
num = prod(L)
print(num)


def str2float(s):
    def fn(x,y):
        return x*10+y
    n = s.index('.')
    n1 = list(map(int,[x for x in s[:n]]))
    n2 = list(map(int,[x for x in s[n+1:]]))
    print(reduce(fn, n1))
    print(reduce(fn,n2)/10**len(n2))
    return reduce(fn,n1)+reduce(fn,n2)/10**len(n2)
print (str2float('123.456'))