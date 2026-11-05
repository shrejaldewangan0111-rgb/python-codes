'''dict1 = {"stu_name":"rudra","age":17,"percentage":88.9}
print(dict1)
for key in dict1:
    print(key)
print()
for i in dict1.items():
    print(i)


print(dict1.get("stu_name"))
print(dict1["stu_name"])'''


# 18 sep

'''students = {"str1":{"name":"l1","age":21},
            "str2":{"name":"13","age":21}}
for i in students.values():
    print(i)

print(students["str1"]["name"])'''


car1={"top_speed":234,"color":"red","price":1200000}
car1["on_road_price"]=1300000
print(car1)

'''stu1={"name":"shrejal","class":"FA09","section":"J"}
stu1["phone_number"]=9098080911
print(stu1) '''

'''# Remove element
car1.pop("on_road_price")
print(car1)

car1.popitem()
print(car1)

# dictionary will be there only elements will be removed
car1.clear()
print(car1)

# dictionary hi delete ho jyega
del car1
print(car1)'''