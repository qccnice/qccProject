# -*- coding: utf-8 -*-
import os
from collections import Iterable
def change_arg(a,b=0,*arg):
    print('a =',a,'b =',b,'arg =',arg)

change_arg(3,8,9,10)

def key_arg(a,b,*arg,**kw):
    print('a =',a ,'b =',b,'arg =',arg,'kw =',kw)

key_arg(1,2,3,4,5,x=1,y=3,z=7)


def get_max_min(list):
    max=list[0]
    min=list[0]
    for i in list:
        if i > max:
            max=i
    for j in list:
        if j < min:
            min = j
    return max,min

print(get_max_min([-2,1,2,3,4,5,100]))


def get_map(maps):
    for key in maps:
        print(key,maps.get(key))

    for value in maps.values():
        print('value:',value)
    for k,v in maps.items():
        print(k,v)

get_map({'a':1,'b':2})

print(isinstance(3,int))
print(isinstance('abc',Iterable))

print(list(range(1,20)))
print([x*x for x in range(1, 11) if x % 2 == 0])

L = ['Hello', 'World', 18, 'Apple', None]
print([s.lower() for s in L if isinstance(s,str)== True ])
print([s.lower()  if isinstance(s,str)== True else "XD" for s in L ])


