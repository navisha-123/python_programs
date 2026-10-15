#swapping
n=int(input())
listone=[]
for i in range(n):
    data=int(input())
    listone.append(data)
left=0
right=len(listone)-1
while left<right:
    temp=listone[left]
    listone[left]=listone[right]
    left+=1
    rigth-=1
print(listone)

#with using third variable
a=10
b=20
print(a,",b")
c=a
a=b
b=c
print(a,",b")

#without using third variable
c=10
d=20
print(c,",d")
c=c+d
d=c-d
c=c-d
print(c,"",d)

#move zeros

def movezeros(arr):
    j=0
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[j]=arr[i]
            j+=1
    while j<len(arr):
        arr[j]=0
        j+=1
    print(arr)

arr=[3,0,5,4,0,0,9]
movezeros(arr)