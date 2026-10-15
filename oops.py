#oops

class Student:
    Name="Madhumitha"
    Age=20
    def marks(self):
        print("English: 90, Physics: 85")

s1=Student()
print(s1.name)
print(s1.age)
s1.marks

class student:
    name="Unknown"
    mark=0

    def display(self):
        print("Name: ",self.name)
        print("Mark: ",self.mark)

s1=student()
s1.name="Madhu"
s1.mark=90
s2=student()
s2.name="Mash"
s2.mark=98
s3=student()
s3.name="Mace"
s3.mark=85
s1.display()
s2.display()
s3.display()


class student:
    name="Unkonwn"
    mark=0
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark

#def setdetails(self,name,mark):
    #self.name=name
    #self.mark=mark

    def display(self):
        print("name: ",self.name)
        print("mark: ",self.mark)

s1=student("madhu",89)
#s1.setdetails("madhu",67)
s1.display()