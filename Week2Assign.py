#create an empty list
my_list = []

#append elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

#insert elements
my_list.insert(1, 15)
print("updated #1 :",my_list)

#extend elements
my_list2 = [50, 60, 70]
my_list.extend(my_list2)
print("updated #2 :", my_list)

#remove an element
my_list.pop(7)
print("update #3 :",my_list)

#sort in ascending
my_list.sort()
print("updated #4 :",my_list)

#find and print index value of 30
index = my_list.index(30)
print(f"The index of '{30}' is : {index}")