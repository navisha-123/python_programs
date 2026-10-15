#variables - local and global

def show():
    message="HEllo"    #Local variable
    print(message)
show()

text="Madhumitha"       #global variable
def greet():
    print("Hello",text)

greet()
print("hi",text)