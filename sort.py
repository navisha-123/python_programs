#sort()
arr2=[10,30,50,200,4000,85]
arr2.sort()
print(arr2)
arr2.sort(reverse=True)
print(arr2)


arr3=[10,30,50,200,40]
arr3.reverse()
print(arr3)

arr4=[10,30,50,200,40]
print(len(arr4))
print(sum(arr4))
print(min(arr4))
print(max(arr4))

nums=[]
pos=ng=zero=0
n=int(input())
for i in range(n):
    value=int(input())
    nums.append(value)
for value in nums:
    if value < 0:
        neg+=1
    elif value > 0:
        pos+=1
    else:
        zero+=1
print("List values: ",nums)
print("Pos count: ",pos)
print("NEg count: ",neg)
print("Zeros count: ",zero)