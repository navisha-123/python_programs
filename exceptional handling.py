try:
    a=int(input("Enter your number: "))
    b=int(input("Enter your number: "))
    print(a//b)
except ValueError:
    print("Please enter interger only")
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Something")