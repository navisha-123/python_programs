mark=int(input())
if mark>=90 and mark<=100:
    print("A")
elif mark>=75 and mark<=89:
    print("B")
elif mark>=60 and mark<=74:
    print("C")
elif mark>=40 and mark<=59:
    print("D")
else:
    print("FAIL") 

num=int(input())
if num>0:
    print("Positive")
elif num<0:
    print("Negative")
elif num==0:
    print("Zero")

num1=int(input())
num2=int(input())
num3=int(input())

if num1<num2:
    if num1>num3:
        print("Num3 is greater")
    else:
        print("Num3 is greater")
else:
    if num2>num3:
        print("Num2 is greater")
    else:
        print("Num3 is bigger")