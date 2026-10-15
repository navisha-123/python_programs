# print("RGCET")
# name='viju madhu'
# print(name)
# print("how are you"+name)
# a=9
# b=8.9
# c="M"
# d="pravin"num
# e=True
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
# print(100)
# print("100+200")
# print("madhu", 20,"BME")
# print("viji", 20, "BME")




# print("*"*30)
# print((" "*5) ,"STUDENT PROFILE" ,(" "*5))
# print("*"*30)
# name =": Arun"
# print("Name",name)
# age =": 20"
# print("Age", age)
# name= ": CSE"
# print("Department",name)
# name=(":Python" ,"Java" ,"C"sep= ",")
# print("Skills", name),
# name= ":270"
# print("Total Marks", name)
# name= ":30"
# print("Average", name)
# print("*"*30)
# print("Than you ", "viju madhu!")

# name=input("Enter name:")
# tamil=int(input("Enter the tamil mark:"))
# english=int(input("Enter the english mark:"))
# maths=int(input("Enter the maths mark:"))
# print("student: ",name)
# total=tamil+english+maths
# print("total:",total)
# print("average: ", total/3)

# total_minutes=int(input("Enter the total minutes"))
# print("hour:" ,total_minutes//60)
# print("minutes:" , total_minutes%60)

# mark=int(input("Enter the mark:"))
# print(mark >=40)

# mark=int(input("enter the mark:"))
# attendance=int(input("enter the attendance:"))
# print(mark >=40 and attendance >=70)

# initial_balance=float(input("enter the initial balance:"))
# deposit_amount=float(input("enter the deposit amount:"))
# initial_balance+=deposit_amount
# expense_amount=float(input("enter expense amount:"))
# initial_balance-=expense_amount
# print("final balance :" ,initial_balance)

# fruits=["apple" , "mango" , "orange", "banana"]
# fruit_name=(input("enter the fruit namr: "))
# print(fruit_name in fruits)

# mark1=[80,90,100]
# mark2=mark1
# mark3=[80,90,100]
# print(mark1 is mark2)
# print(mark1 is not mark3)
# print(mark1 == mark3)

# a=10
# b=20
# c=a&b
# print(c)

# a=5
# b=2
# c=a&b
# print(c)

# d=a|b
# print(d)

# e=a|b
# print(e)

# f=a^b
# print(f)

# g=a<<b
# print(g)

# h=a>>b
# print(h)

# num=int(input("enter youe number"))
# if num%2==0:
#     print("the num is even")
# else:
#     print("the num is odd")


# mark=int(input())
# if mark>=90 and mark<=100:
#     print("A")
# elif mark>=75 and mark<=89:
#     print("B")
# elif mark>=60 and mark<=74:
#     print("C")
# elif mark>=40 and mark<=59:
#     print("D")
# else:
#     print("FAIL") 

# num=int(input())
# if num>0:
#     print("Positive")
# elif num<0:
#     print("Negative")
# elif num==0:
#     print("Zero")

# num1=int(input())
# num2=int(input())
# num3=int(input())

# if num1<num2:
#     if num1>num3:
#         print("Num3 is greater")
#     else:
#         print("Num3 is greater")
# else:
#     if num2>num3:
#         print("Num2 is greater")
#     else:
#         print("Num3 is bigger")

#discount

# bill =(int(input("Enter the purchase amount: ")))
# if bill>=5000:
#     discount_percentage = 20
#     print("THE DISCOUNT is 20%")
# elif bill>=2000 and bill<=4999:
#     discount_percentage = 10
#     print("THE DISCOUNT is 10%")
# else:
#     print("NO DISCOUNT")

# discount_amount = bill * discount_percentage / 100
# print("Discount Amount:", discount_percentage)
# final_amount = bill - discount_amount
# print("Final Payable Amount:", final_amount)

# food=int(input("enter the food"))
# match food:
#     case 1: print("idly")
#     case 2: print("dosa")
#     case 3: print("pongal")
#     case _: print("invalid menu")



# for i in range(10):

#     print("hello navi")


# for i in range (1,11):
#     print(i)

# for i in range (1,101,3):
#     print(i,end=" ")

# print()
# for i in range (5,0,-1):
#     print(i)

# num=int(input())
# sum=0
# for i in range(1,num+1):
#     sum=sum+i
# print(sum)

# num1=int(input())
# num2=int(input())
# total=0
# for i in range(num1,num2+1):
#     if i%2==0:
#         total=total+i
# print(total)

# num=int(input())
# for i in range(1,11):
#     print(i,"X",num,"=",num*i)

# num=int(input())
# fact=1
# for i in range(num,0-1):
#     fact=fact*i
#     print(i,end=" ")
#     if i!=1:
#         print("*",end=" ")
# print("=",fact)

# num=int(input())
# count=0
# for i in range(1,num+1):
#     if num%i==0:
#         count+=1
# if count==2:
#     print(num,"is prime number")
# else:
#     print(num,"is not prime number")

# num=int(input())
# digits=0
# total=0
# while num!=0:
#     rem=num%10
#     digits+=1
#     total=+rem
#     num=num//10
# print("no of digits:",digits)
# print("sum of digits:",total)

# num=int(input())
# while not (num>=0 and num<=9):
#      sums=0
#      while num!=0:
#         rem=num%10
#         sums+=rem
#         num=num//10
#      num=sums
# else:
#     print(num)

# for i in range(1,21):
#     if i==16:
#         break
#     print(i,end=" ")
# print()
# for i in range(1,6):
#     if i==3:
#         continue
#     print(i,end=" ")

# numbers=[1,2,3,4,5]
# name=["navi","kavi","nauya","raji"]
# mixed=[10,2.3,6,"n","navi"]
# print(numbers)
# print(name)
# print(mixed)
# print(numbers[0])
# print(numbers[2])
# print(numbers[1])
# print(numbers[-1])
# print(numbers[-2])
# print(numbers[-5])
# numbers[2]=400
# print(numbers)

# num=[]
# n=int (input())
# for i in range(n):
#     value=int(input())
#     num.append(value)
#     print(num)


#     arr=[1,2,3,4,5]
# for value in arr:
#     print(value,end=" ")

# print()

# i=0 #2<5
# while i<len(arr):
#     print(arr[i],end=" ")
#     i+=1


#list slicing

# arr=[10,20,30,40,50,60]   #list[start:stop:step]
# print(arr[1:5])
# print(arr[:3])
# print(arr[3:])
# print(arr[::2])
# arr1=[10,20,30,20,50]
# print(30 in arr1)
# print(90 in arr1)
# print(arr1.index(20))
# print(arr1.count(20))
# print(arr1.count(90))
# print(arr[3:])
# print(arr[::2])

# #sort()
# arr2=[10,30,50,200,4000,85]
# arr2.sort()
# print(arr2)
# arr2.sort(reverse=True)
# print(arr2)

# #sort()
# arr3=[10,30,50,200,40]
# arr3.reverse()
# print(arr3)

# arr4=[10,30,50,200,40]
# print(len(arr4))
# print(sum(arr4))
# print(min(arr4))
# print(max(arr4))

# nums=[]
# pos=ng=zero=0
# n=int(input())
# for i in range(n):
#     value=int(input())
#     nums.append(value)
# for value in nums:
#     if value < 0:
#         neg+=1
#     elif value > 0:
#         pos+=1
#     else:
#         zero==1
# print("List values: ",nums)
# print("Pos count: ",pos)
# print("neg count: ",neg)
# print("zeros count: ",zero)

# numbers=(10,20,30,40)
# print(numbers)
# print(type(number))
# arr=(5,)
# print(type(arr))
# print(numbers[2])
# print(numbers[2])
# print(numbers[-1])
# print(numbers[1:4])


# for value in numbers:
#     print(value,end=" ")

# print()
# arr2=(10,20,30,20)
# print(arr2.count(20))
# print(arr2.index(30))
# print(len(arr2))
# print(sum(arr2))
# print(min(arr2))

#unordered

# numbers={45,67,89,90}
# print(number)
# names={"navi","nauya","kavi"}
# print(names)
# empty_set=set()
# empty_set={4,5,6}
# print(empty_set)
# nums={10,20,30,20,30,10}
# print(nums)
# print(len(nums))


# list_1=[10,20,30,20,30,50,10]
# unique_set=set(list_1)
# print(unique_set)

# num_1={10,20,30}
# nums_1={10,20,30}
# nums_1.add(40)
# print(nums_1)
# nums_1.remove(50)
# print(nums_1)
# # nums_1.remove(150)
# # print(nums_1)
# nums_1.discard(40)
# print(nums_1)
# nums_1.discard(140)
# print(nums_1)
# num_1.discard(140)
# print(num_1)
# num_1.discard(140)
# print(num_1)
# for value in num_1:
#     print(value,end=" ")

#a={1,2,3}
# b={3,4,5}
# print()
# print(a.union(b))
# print(a.intersection(b))
# print(a.isdifference)

# a={10,20}
# b={10,20,30,40}
# c={50,60}
# print()
# print(a.issubset(b))
# print(b.issubset(a))
# print(a.isdisjoint(b))
# print(b.isdisjoint(c))

#dict- mutable

#
#     "Name":"Madhumitha",
#     "Age":20,
#     "Mark":430,
#     "Department":"BME"

# }

# print(student_1)
# print(student_1["Name"])
# print(student_1["Mark"])
# # print(student_1["City"])
# print(student_1.get("Age"))
# print(student_1("City","Not Avaliable"))
# student_1["Mark"]=499
# print(student_1)
# student_1["City"]="Pondy"
# print(student_1)
# student_1.pop("age")
# print(student_1)

# for key,value in student_1.items():
#     print(key,":",value)

# product_name={
#     "name":"keyboard",
#     "price":500,
#     "stock":10
#     }
# print(product_name)
# product_name["price"]=650
# print(product_name)
# product_name["brand"]="Logitech"
# print(product_name)

# for key,value in product_name.items():
#     print(key," :",value)


# name="madhu"
# course="python"
# print(name)
# print(course)
# print(type(name))
# print(type(course))
# print(course[0])
# print(course[1])
# print(course[-1])
# #pyt
# print(course[0:3])
# #thon
# print(course[2:1])
# #pyth
# print(course[0:4])
# #nohtyp
# print(course[::-1])

# text="Python"   #1000
# text="j"+text[1:] #2000
# print(text)

# print(len(text))

# for value in text:
#     print(value,end=" ")
# print()
# text_1="Hello Python"
# print(text_1.upper())
# print(text_1.lower())
# print(text_1.replace("Python","Java","C","C++"))
# print(text_1)
# print(text_1.count('o'))
# print(text_1.find("Python"))
# print(text_1.startswith("Hello"))
# print(text_1.endswith("Python"))

# text_2="                         navisha varadhu                  "
# print(text_2.strip())

# text_3="C C++ Java Python"
# print(text_3)
# courses=text_3.split()
# print(courses)

# text_4=["C","C++","java","python"]
# text_5=" ".join(text_4)
# print(text_5)

# word=input("Enter the word: ").lower()
# if word==word[::-1]:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")
 
# def greet():
#     print("good morning navi")

# def addition(a,b):
#     print(a+b)

# def multiplication(a,b):
#     return a*b

# greet()
# greet()

# addition(3,4)
# addition(10,20)

# result=multiplication(3,4)
# print(result)

# def fun_square():
#     return num*num

# num = int(input("enter your number:"))

# result = fun_square(num)

# print("square =",result)
 
#variables - local and global

# def show():
#     message="HEllo"    #Local variable
#     print(message)
# show()

# text="navi"       #global variable
# def greet():
#     print("Hello",text)

# greet()
# print("hi",text)

#Lamba function - a lambda function is a small anonymous function containing a single expression
#syntax 
# lambda arguments:expression

# square=lambda n:n*n
# n=int(input())
# result=square(n)
# print(result)

# addition=lambda a,b:a+b
# total=addition(4,5)
# print(total)

# def greet(n):
#     if n==0:
#         return
#     print("Hello madhu")
#     greet(n-1)
# greet(5)
# print()

# def printnum(a):
#     if a==11:
#         return
#     print(a,end=" ")
#     printnum(a+1)

# printnum(1)

# def factorial(num):
#     if num==1:
#         return 1
#     return num*factorial(num-1)

# num=int(input("Enter your number; "))
# result=factorial(num)
# print(result)

   
# class student:
#     name="unknow"
#     mark=0

#     def display(self):
#         print("name: ",self.name)
#         print("mark: ",self.mark)

# s1=student()
# s1.name="Navisha"
# s1.mark=90
# s2=student()
# s2.name="Nabba"
# s2.mark=89
# s3=student()
# s3.name="Nala"
# s3.mark=40
# s1.display()
# s2.display()
# s3.display()



# class student:
#     name="unknown"
#     mark=0
#     def __init__(self,name,mark):
#         self.name=name
#         self.mark=mark
#     def setdetails (self,name,mark):
#         self.name=name
#         self.mark=mark
#     def display(self):
#         print("name: ",self.name)
#         print("mark: ",self.mark)

# s1=student("navi",89)
# s1.setdetails("navi",67)
# s1.display()

#inheritance
#single inheritance - one parent->one child
# class device:
#     def power_on(self):
#     print("device switched on ")
# class phone(device):
#     def call (self):
#         print("making a phone call")
# samsung=phone()
# samsung.call()
# samsung.power_on ()
# #multilevel inheritance grandparent->parent->child
# class device:
#     def power_on(self):
#         print("device switched on ")
# class comperter(device):
#     def run_program(self):
#     print("running a python program")
# class laptop(computer):
#      def change(self):
# class laptop(computer):
#     def charge(self):
#         print("laptop battery charging")
# asus=laptop()
# asus.power_on()
# asus.run_program()
# asus.charge()
# print()

# #MULTIPLE INHERITANCE - FATHER -> MOTHER -> CHILD

# class camera:
#     def take_photo(self):
#         print("Taking a photo")
# class musicplayer:
#     def playmusic(self):
#         print("Playing a music")
# class smartphone(camera,musicplayer):
#     def call(self):
#         print("Making a phone call")
# mi=smartphone()
# mi.playmusic()
# mi.take_photo()
# mi.call
# print()

#HIERARCHICAL INHERITANCE ONE PARENT -> MULTIPLE CHILD

# class Device:
#     def power_on(self):
#         print("Device switched on")
# class phone(Device):
#     def call(self):
#         print("Making a phone call")
# class computer(Device):
#     def run_program(self):
#         print("Running a python program")
# iphone=phone()
# iphone.power_on()
# iphone.call()
# hp=computer()
# hp.power_on()
# hp.run_program()
# print()

#polymorphism many forms
#method overriding
# class phone:
#     def camera(self):
#         print("taking a normal photo")
# class smartphone(phone):
#     def camera(self):
#         print("taking a protrait photo"):
# mi=smartphone()
# # mi.camera()
# # nokia=phone()
# # nokia.camera()
# # print()

#ENCAPSULATION

mi=smartphone()
# mi.camera()
# nokia=phone()
# nokia.camera()
# print()

#ENCAPSULATION

# class phone:
#     __battery="30%"
#     def printbattery(self):
#         print(self.__battery)
# iphone15=phone()
# iphone15.printbattery()

#abstraction - hiding the internal detail and showing only essential
#features
# form abc import ABC,abstractmethod
# class payment(ABC):
#     @abstractmethod
#     def pay(self):
#         pass
# class UPI(payment):
#     def pay(self):
#         print("payment compeleted using upi")
# class Gpay(payment):
#     def pay(self):
#         print("payment compeleted using gpay")
# class Gpay(payment):
#     def pay(self):
#         print("payment compeleted using phonepe")
# payment=UPI()
# payment.pay()
# payment=Gpay()
# payment.pay()
# payment=Phonepe()
# payment.pay()

#time and space complexity
#time complexity describes how the numbr of operations in an algorithm
#performs grows as its inout size increases
#it measures growth rather than the exact running time in second

#o(1) - constant time
# names=["madhu","mash","mace"]
# print(names[2])
# print(names[1])

# #linear time -o(n)

# n=100
# for i in range(n):
#     print(i,end=" ")

# #quadraticc - o(n^2)
# num=5
# for i in range(1,num+1):for j in range(1,num+1):
#         print(j,end=" ")
#     print()

# #Logarithmic time - o(log n)
# nums=16
# while num>1:
#     print(nums)
#     num//=2
#space complexity describes how the memory required by an algorithm grows
# as its input size increases
# extra space means the additional memory used excluding the existing 
#input
#O(1)-constant space
































