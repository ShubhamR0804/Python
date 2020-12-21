
#functions to add , sub , div , mul
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def div(a,b):
    return a/b
def mul(a,b):
    return a*b

print("CALCULATOR")
print("1.Addition\n2.Subtraction\n3.Division\n4.Multiplication")

#To choose which function to perform  
choice=int(input("which operator do you want to perform?...."))

#For user to input numbers 
a=int(input("No.1= "))
b=int(input("No.2= "))

#if...elif condition depending upon the choice of the user will get executed 
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
