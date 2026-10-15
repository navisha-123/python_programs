#immutable collection of characters

name="madhu"
course="python"
print(name)
print(course)
print(type(name))
print(type(course))
print(course[0])
print(course[1])
print(course[-1])
#pyt
print(course[0:3])
#thon
print(course[2:1])
#pyth
print(course[0:4])
#nohtyp
print(course[::-1])

text="Python"   #1000
text="j"+text[1:] #2000
print(text)

print(len(text))

for value in text:
    print(value,end=" ")
print()
text_1="Hello Python"
print(text_1.upper())
print(text_1.lower())
print(text_1.replace("Python","Java","C","C++"))
print(text_1)
print(text_1.count('o'))
print(text_1.find("Python"))
print(text_1.startswith("Hello"))
print(text_1.endswith("Python"))

text_2="                         Madhumitha Kalaivendan                   "
print(text_2.strip())

text_3="C C++ Java Python"
print(text_3)
courses=text_3.split()
print(courses)

text_4=["C","C++","java","python"]
text_5=" ".join(text_4)
print(text_5)