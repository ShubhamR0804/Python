# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 18:48:32 2020

@author: Shubham Ramteke
"""

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def div(a,b):
    return a/b
def mul(a,b):
    return a*b

print("CLACULATOR")
print("1.Addition\n2.Subtraction\n3.Division\n4.Multiplication")
choice=int(input("which operator do you want to perform?...."))
a=int(input("No.1= "))
b=int(input("No.2= "))

if choice==1:
    print(a,"+",b,"=",add(a,b))
elif choice==2:
    print(a,"-",b,"=",sub(a,b))
elif choice==3:
    print(a,"/",b,"=",div(a,b))
elif choice==4:
    print(a,"*",b,"=",mul(a,b))
else:
    print("Invalid Choice")    