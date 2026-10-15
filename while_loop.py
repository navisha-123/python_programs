#while loop

num=int(input("Enter your number: "))
digits=0
total=0
while num!=0:
    rem=num%10
    digits+=1
    num=num//10

print("The total number of digits is: ",digits)
print("sum of digits: ",total)

num=int(input("Enter your number: "))
while not (num>=0 and num<=9):
    sums=0
    while num!=0:
        rem=num%10
        sums+=rem
        num=num//10
    nums=sums
else:
    print(num)

num=int(input())
digits=0
temp=num
temp1=num
while num!=0:
    rem=num%10
    digits+=1
    num=num//10
sums=0
while temp!=0:
    rem=temp%10
    sums=sums+rem**digits
    temp=temp//10
if sums==temp1:
    print("Armstrong number")
else:
    print("Not an Armstrong number")