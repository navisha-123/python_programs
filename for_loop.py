#for loop
num=int(input())
sum=0
for i in range(1,num+1):
    sum=sum+i
print(sum)

num1=int(input())
num2=int(input())
total=0
for i in range(num1,num2+1):
    if i%2==0:
        total=total+i
print(total)

#multiplication table
num=int(input())
for i in range (1,11):
    print(i,"X",num,"=",num*i)

#factorial numbers

num=int(input())
fact=1
for i in range(num,0,-1):
    fact=fact*i
    print(i,end=" ")
    if i!=1:
        print("*",end=" ")
print("=",fact)

#prime number

num=int(input("Enter your number: "))
count=0
for i in range(1,num+1):
    if num%i==0:
        count+=1
if count==2:
    print(num,"is a prime number")
else:
    print(num,"is not a prime number")