#bubble sort
listone=[3,5,7,9,10]
for i in range(len(listone)-1):
    for j in range(len(listone)-1-i):
        if listone[j]>listone[j+1]:
            temp=listone[j]
            listone[j]=listone[j+1]
            listone[j+1]=temp
print(listone)