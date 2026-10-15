#time and space complexity
#time complexity describes how the numbr of operations in an algorithm
#performs grows as its inout size increases
#it measures growth rather than the exact running time in second

#o(1) - constant time
names=["madhu","mash","mace"]
print(names[2])
print(names[1])

#linear time -o(n)

n=100
for i in range(n):
    print(i,end=" ")

#quadraticc - o(n^2)
num=5
for i in range(1,num+1):
    for j in range(1,num+1):
        print(j,end=" ")
    print()

#Logarithmic time - o(log n)
nums=16
while nums>1:
    print(nums)
    nums//2