capital_city = {"Nepal": "Kathmandu", "Italy": "Rome", "England": "London"}
print(capital_city)

#Add elements
print("Intial Dictionary:",capital_city)
capital_city["Japan"] = "Tokyo"
print("Updated Dictionary:",capital_city)

#change value
student_id = {111: "Eric", 112: "Kyle", 113: "Butters"}
print("initial Dictionary:",student_id)
del student_id[111]
print("Updated Dictionary:",student_id)

#Accesing elements
print(student_id[113])

#methods
print(len(student_id))
print(sorted(student_id))

#Membership test for dictionary keys
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
print(1 in squares)
print(2 not in squares)
print(49 in squares)

#membership test:
student = {"Name": "Philip", "City": "Nairobi", "Age": "15"}
print(student)
print("Contact" in student)
print("Contact" not in student)
print("Name" in student)

#Iterating
for value in student.values(): 
   print(value)
