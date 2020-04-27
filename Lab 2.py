# -*- coding: utf-8 -*-
"""
Created on Thu May  9 17:11:48 2019

@author: Andrew
"""

#Question 1
a=[1,2,3]+[4,5,6];print('a)',a)
b=[1,2,3];b.append([4,5,6]);print('b)',b)
c=[1,2,3];c.extend([4,5,6]);print('c)',c)
d=len([]);print('d)',d)
e=list(range(5,0,-1));print('e)',e)
f=len(range(0,5));print('f)',f)
g=sum(range(0,5));print('g)',g)
h=max([17,99,42]);print('h)',h)
i=[1,2,3,4];i.reverse();print('i)',i)
j=max(["Hello","there","world","how","are","yeh?"]);print('j)',j)
k="Hello world";print('k)',k[3:6])
print('l)',k[:])
print('m)',k[-1:-5:-1])
print('n)',k[::-1])
o=42 in range(0,100);print('o)',o)
p='7' in str(123456);print('p)',p)

#Question 2
