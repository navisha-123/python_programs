dict- mutable

student_1={
    "Name":"Madhumitha",
    "Age":20,
    "Mark":430,
    "Department":"BME"

}

print(student_1)
print(student_1["Name"])
print(student_1["Mark"])
print(student_1["City"])
print(student_1.get("Age"))
print(student_1("City","Not Avaliable"))
student_1["Mark"]=499
print(student_1)
student_1["City"]="Pondy"
print(student_1)
student_1.pop("age")
print(student_1)