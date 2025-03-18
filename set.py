#create a set of integer
student_id = {112, 114, 116, 118, 115}
print('Student ID:', student_id)

#create a set of string type
vowel_letters = {'a', 'e', 'i', 'o', 'u'}
print('Vowel letters:', vowel_letters)

#Create a set of mixwd data types
mixed_set = {'Hello', 101, -2, 'Bye'}
print('Set of mixed data types:', mixed_set) 

#create empty set
empty_set =set()
empty_dictionary ={}
print('Data type of empty_set:', type(empty_set))
print('Data type of empty_dictionary:', type(empty_dictionary))
 
 #duplicataee items
numbers = {2, 4, 6, 6, 2, 8}
print(numbers)
numbers.add(5) #Add items to a set
print('Updated Set:', numbers)

#method update()
companies = {'Lacoste', 'Ralph Lauren'}
tech_companies = ['apple', 'google', 'apple']
companies.update(tech_companies)
print(companies)

#remove an element from set
languages = {'Swift', 'Java', 'Python'}
print('Initial set:', languages)
languages.discard('Java')
print('Updated set:', languages)

#iterate over a set in python
fruits = {"Apple", "Peach", "Mango"}
for fruit in fruits:
    print(fruit)