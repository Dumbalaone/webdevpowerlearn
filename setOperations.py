#Union operation
A = {1, 3, 5}
B = {1, 2, 4}
print('Union using |:', A | B)#using |
print('Union using union():', A.union(B))#using union()

#intersection operation
print('Intersection  using &:', A & B)#using &
print('Intersection using():', A.intersection(B))#using intersection()

#Difference operation
print('Difference using - :',A - B)
print('Difference using difference():', A.difference(B))


#set symmetric difference
print('Using ^:', A ^ B)
print('Using symmetric_difference():', A.symmetric_difference(B))

#check if two sets are equal
a = {1, 3, 5}
b = {3, 5, 1}
if a == b:
    print('set a and b are equal')
else:
    print('set a and  b are not equal')