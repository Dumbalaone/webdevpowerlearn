number_list = []
num_count = int(input('How many numbers do you need: '))
for i in range (num_count):
    number = float(input(f'Enter numbers {i+1}: '))
    number_list.append(number)
total_sum = sum(number_list)   
print('sum of list: ',total_sum)
    
    
    
