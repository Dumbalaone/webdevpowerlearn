languages = ["Python" ,"Swift" , "C++", "C", "Java", "Rust"]
print(languages[-3])

#slicing list:
my_list = ['p','r','o','g','r','a','m','i','z']
print(my_list[2:5]) #print from index 2 to 4
print(my_list[::3]) #Takes every third element
print(my_list[::-1]) #reversing the list
print(my_list[5:]) #from index 1 to end

#using append
numbers = [21, 34, 54, 12]
print("Before Append:",numbers)
numbers.append(32)
print("After append:",numbers)

#using extend
prime_numbers = [2, 3, 5]
print("list1",prime_numbers)
even_numbers = [4, 6, 8]
print("list2",even_numbers)
prime_numbers.extend(even_numbers)
print("List after extend",prime_numbers)

#Change list item
languages[2] = 'C'
print(languages)

#Remove an Item
del languages[1]
print(languages)

#Using remove
languages.remove("Python")
print(languages)

#Iterating through a list using a for loop
for language in languages:
    print(language)
    
#Python list comprehension
squares = [x**2 for x in range(1, 6)]
print(squares)

#leap years from 1930 to 2025
leap_years = [year for year in range(1930, 2026) if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))]
print("Leap years: ",leap_years)