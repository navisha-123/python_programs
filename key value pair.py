# for key,value in student_1.items():
#     print(key,":",value)


product_name={
    "Name":"Keyboard",
    "Price":500,
    "Stock":10

}
print(product_name)
product_name["Price"]=650
print(product_name)
product_name["brand"]="Logitech"
print(product_name)

for key,value in product_name.items():
    print(key," :",value)