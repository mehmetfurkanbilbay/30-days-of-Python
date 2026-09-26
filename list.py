# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


empty_list = list() # this is an empty list, no item in the list
print(len(empty_list))  # 0

fruits = ['banana', 'orange','mango','lemon']

vegetables = ['tomato', 'potato','cabbage', 
              'onion', 'carrot']


# Print the lists and its length

print("Fruits:", fruits)
print("Number of fruits:",len(fruits))

print()
print("Vegetables:", vegetables)
print("Number of vegetables:",len(vegetables))

# Modifying list

fruits = ['banana', 'orange','mango','lemon']
first_fruit = fruits[0] # we are accessing the first item using its index
print(first_fruit)      # banana

second_fruit = fruits[1]
print(second_fruit)     # orange

last_fruit = fruits[3]
print(last_fruit)       # Lemon

# Last Index

last_index = len(fruits)-1
last_fruit = fruits[last_index]
print(last_fruit)

# Accessing items

fruits = ['banana', 'orange', 'mango', 'lemon']
last_fruit = fruits[-1]
second_last = fruits[-2]
print(last_fruit)
print(second_last)

# Slicing items

fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4]  # it returns all the fruits
# this is also give the same result as the above
all_fruits = fruits[0:]  # if we don't set where to stop it takes all the rest
orange_and_mango = fruits[1:3]  # it does not include the end index
orange_mango_lemon = fruits[1:]

all_fruits = fruits[-4:]  # it returns all the fruits
# this is also give the same result as the above
orange_and_mango = fruits[-3:-1]  # it does not include the end index
orange_mango_lemon = fruits[-3:]

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'Avocado'
print(fruits)  # ['avocado', 'orange', 'mango', 'lemon']
fruits[1] = 'apple'
print(fruits)  # ['avocado', 'apple', 'mango', 'lemon']
last_index = len(fruits)-1
fruits[last_index] = 'lime'
print(fruits)  # ['avocado', 'apple', 'mango', 'lime']

# checking items
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist) # True
does_exist = 'lime' in fruits
print(does_exist) # False

#-------------------------------------------------------------------------------------------

# append
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('strawberry')
print(fruits)   # ['banana', 'orange', 'mango', 'lemon', 'strawberry']

# insert
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple') # insert apple between orange and mango
print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']

# remove

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.remove('banana')
print(fruits)  # ['orange', 'mango', 'lemon']
fruits.remove('lemon')
print(fruits)  # ['orange', 'mango']


# pop
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()  # deletes the last index
print(fruits) ['banana', 'orange', 'mango'] 

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop(1)
print(fruits) # ['banana', 'mango', 'lemon']

# del 
fruits = ['banana', 'orange', 'mango', 'lemon']
del fruits[0]
print(fruits)       # ['orange', 'mango', 'lemon']

del fruits[1]
print(fruits)       # ['orange', 'lemon']
del fruits
print(fruits)      # This should give: NameError: name 'fruits' is not defined

# clear
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)       # []


# copying a lits
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)       # ['banana', 'orange', 'mango', 'lemon']

# join

positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5, -4, -3, -2, -1]
integers = negative_numbers + zero + positive_numbers
print(integers)

all_numbers = [*negative_numbers, *zero, *positive_numbers]
print(all_numbers)

fruits = ['banana', 'orange', 'mango', 'lemon']
sonuc = ' '.join(fruits)
print(sonuc)  #  banana orange mango lemon

fruits = ['banana', 'orange', 'mango', 'lemon']
sonuc = ', '.join(fruits)
print(sonuc)  # banana, orange, mango, lemon

# join with extend

num1 = [0, 1, 2, 3]
num2 = [4, 5, 6]
num1.extend(num2)
print('Numbers:', num1)


negative_numbers = [-5, -4, -3, -2, -1]
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers)

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits.extend(vegetables)
print('Fruits and vegetables:', fruits)

# count

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))           # 3


# index

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))   # 1

ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))


# Reverse

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits.reverse())
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages.reverse())


# sort
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
ages.sort(reverse=True)
print(ages)






