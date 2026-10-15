# #SPACE COMPLEXITY
# #space complexity describes how the memory required by an algorithm grows as its input size increases
# # extra space means the additional memory used excluding the existing input

#O(1)-constant space
listone=[1,2,3,4,56,78,9,10]
total=0
for value in listone:
    total+=value
print(total)

#linear space -0(n)
listtwo=[1,2,3,4]
temp=[]
for values in listtwo:
    temp.append(values*values)
print(temp)