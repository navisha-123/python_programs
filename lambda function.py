# Lamba function - a lambda function is a small anonymous function containing a single expression
# syntax 
# lambda arguments:expression


square=lambda n:n*n
n=int(input())
result=square(n)
print(result)

addition=lambda a,b:a+b
total=addition(4,5)
print(total)


numbers = [1, 2, 3, 4, 5]
cubed = list(map(lambda x: x**3, numbers))
print("Cube list:", cubed)
print("____________________________________________")