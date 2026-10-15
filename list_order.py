# list- ordered, mutable collection of elements and allow duplicate

numbers=[1,2,3,4,5]
names=["madhumitha","mash","mace"]
mixed=[10,2.3,6,"k","madhu"]
print(numbers)
print(names)
print(mixed)
print(numbers[0])
print(numbers[3])
print(numbers[1])
print(numbers[-1])
print(numbers[-2])
print(numbers[-5])
numbers[2]=400
print(numbers)


num=[]
n=int(input())
for i in range(n):
    value=int(input())
    num.append(value)
print(num)

arr=[1,2,3,4,5]
for value in arr:    #for each loop.
    print(value,end=" ")

print()

i=0 #2<5
while i<len(arr):
    print(arr[i],end=" ")
    i+=1