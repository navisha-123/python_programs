#linear search
listtwo=[85,65,45,25,44]
find=200
found=False
for i in range(len(listtwo)):
    if listtwo[i]==find:
        found=True
        break
if found:
    print("Found")
else:
    print("Not Found")