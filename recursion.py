#recursionn - function calling itself

def greet(n):
    if n==0:
        return
    print("Hello madhu")
    greet(n-1)
greet(5)
print()

def printnum(a):
    if a==11:
        return
    print(a,end=" ")
    printnum(a+1)

printnum(1)

def factorial(num):
    if num==1:
        return 1
    return num*factorial(num-1)

num=int(input("Enter your number; "))
result=factorial(num)
print(result)#recursionn - function calling itself

def greet(n):
    if n==0:
        return
    print("Hello madhu")
    greet(n-1)
greet(5)
print()

def printnum(a):
    if a==11:
        return
    print(a,end=" ")
    printnum(a+1)

printnum(1)

def factorial(num):
    if num==1:
        return 1
    return num*factorial(num-1)

num=int(input("Enter your number; "))
result=factorial(num)
print(result)