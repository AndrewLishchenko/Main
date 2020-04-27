# -*- coding: utf-8 -*-
"""
Created on Wed May 15 18:21:30 2019

@author: Andrew
"""
import math
'''
#Question 1
s1=int(input('Enter length of side 1:'))
s2=int(input('Enter length of side 2:'))
s3=int(input('Enter length of side 3:'))

if s1+s2>s3 and s2+s3>s1 and s3+s1>s2 and s1>0 and s2>0 and s3>0:
    print('Valid')
    s=(s1+s2+s3)/2
    area=math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
    print(area)
else:
    print('This is mathematically impossible')



#Question 2

a=int(input('a= '))
b=int(input('b= '))
c=int(input('c= '))

discrim=sqrt((b*b)-(4*a*c))
if discrim.imag!=0:
    print('This polynomial has no real roots, but the imaginary roots are',((-b+discrim)/2),"and",(-b-discrim)/2,)
else:
    print(((-b+discrim.real)/2),"and",(-b-discrim.real)/2)

'''
#Question 3

num=int(input('Enter the numerator: '))
den=int(input('Enter the denominator: '))

if den==0:
    print('Mathimatically impossible, scrub')
elif num//den==0:
    print(num,'/',den)
elif num//den!=0 and num>0 and den>0:
    print(num//den,' ',num%den,'/',den)
else:
    print('-',abs(num)//abs(den),' ',abs(num)%abs(den),'/',abs(den))
