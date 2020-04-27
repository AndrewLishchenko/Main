# -*- coding: utf-8 -*-
"""
Created on Thu May 16 17:26:55 2019

@author: Andrew
"""
#Question 1
'''
def above_average(*elems):
    numHigh=0
    for x in range(len(elems)):
        if elems[x-1]>(sum(elems)/len(elems)):
           numHigh+=1
    print(sum(elems)/len(elems),' ',numHigh)
    
above_average(0,2,4,6,8,10)

#Question 2

def falling_power(n,k):
    total=1
    for x in range(n-k+1,n+1):
        total*=x
    print(total)

falling_power(-4,5)

#Question 3
def  forward_difference(elems):
    newList=[]
    num=0
    if len(elems)>0:
        for i in range(len(elems)-1):
            num=elems[i+1]-elems[i]
            newList.append(num)
    print(newList)

forward_difference([4,2,7,1,8,3])

#Question 4
def shift_characters(text):
    array=list(text)
    newtext=''
    for x in range(len(text)):
        array[x]=chr(ord(array[x])+1)
        newtext+=array[x]
    print(newtext)

shift_characters('Hello World')

#Question 5a

def ques5a(elems):
    sum=0
    for x in range(len(elems)):
        if x%2==0:
            sum+=elems[x]
        else:
            sum-=elems[x]
    print(sum)

ques5a([3,5,2,4,8,2])
'''
#Question 5b

def dominates(first, second):
    fail=0
    if(len(first)>len(second)):
        for x in range(len(second)):
            if first[x]<=second[x]:
                fail+=1
        if fail>0:
            print("List 1 does not dominate")
        else:
            print("List 1 dominates")
    else:
        print("List 1 does not dominate")
    
    
dominates([6,10,2,4],[3,5,2])

#Question 5c
def parity_partitions(numbers):
    final=[]
    
    for x in range(len(numbers)):
        if numbers[x]%2==0:
            final.append(numbers[x])
            
    for x in range(len(numbers)):
        if numbers[x]%2==1:
            final.append(numbers[x])
    print(final)
    
parity_partitions([7,0,2,-1,3,4,1])

#Question 5d
def extract_antidiagonal(matrix):
    
extract_antidiagonal([[7,5,2,9],[1,-3,6,2],[7,4,4,1],[3,9,0,2]])