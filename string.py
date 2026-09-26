# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 13:12:55 2026

@author: furka
"""

# Single line comment
letter = 'p'                # A string could be a single character or a bunch of texts
print(letter)               # p
print(len(letter))          # 1
greeting  = 'Hello, Wordl!' # String could be  a single or double quote,"Hello, World!"
print(greeting)             # Hello, World!
print(len(greeting))        # 13
sentence = "I hope you are enjoying 30 days of python challenge"
print(sentence)


# Multiline Strings

multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)
# Another way of doing the same thing
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)

# String Concatenation

first_name='john'
last_name = 'Doe'
space = ' '
full_name = first_name + space + last_name
print(full_name) 
# Checking length of a string using len() builtin function
print(len(first_name))  # 4
print(len(last_name))   # 3
print(len(first_name) > len(last_name)) # True
print(len(full_name))   # 8


# Unpacking characters

language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n


# Accessing characters in strings by index
language='Python'
first_letter=language[0]
print(first_letter)     # P
second_letter = language[1]
print(second_letter)    # y
last_index = len(language) -1
last_letter = language[last_index]
print(last_letter)      # n



# If we want to start from right end we can use negative indexing. -1 is the last index
language='Python'
last_letter = language[-1]
print(last_letter) # n
second_last = language[-2]
print(second_last) # o


# Slicing
language='Python'

first_three=language[0:3]
# starts at zero index and up to 3 but not include 3
print(first_three) # Pyt

last_three=language[3:6]
print(last_three)  # hon
# Another way
last_three=language[-3:]  # hon
last_three=language[3:]   # hon

# Skipping character while splitting Python strings
language='Python'
pto=language[0:6:2]
print(pto) # Pto


# Escape sequence

print('I hope every one enjoying the python challenge.\nDo you ?')  # line break
print('Days\tTopics\tExercises')
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')
print('This is a back slash  symbol (\\)')  # To write a back slash
print('In every programming language it starts with \"Hello, World!\"')

# --------------------------------------------------------------------------------------------------
# STRING METHODS

# 1. capitalize(): Converts the first character the string to Capital Letter

challenge = 'thirty days of python'
print(challenge.capitalize()) # 'Thirty days of python'


# 2. count(): returns occurrences of substring in string, count(substring, start=.., end=..)

challenge = 'thirty days of python'

# Counts all 'y' characters in the entire string
print(challenge.count('y')) # 3

# Counts 'y' only between index 7 (inclusive) and index 14 (exclusive)
# It searches inside the substring 'days of' and finds 1 'y' at index 9
print(challenge.count('y', 7, 14))  # 1

# Counts the total occurrences of the substring 'th'
print(challenge.count('th'))  # 2


# 3. endswith(): Checks if a string ends with a specified ending

challenge = 'thirty days of python'

print(challenge.endswith('of'))  # False
print(challenge.endswith('hon')) # True


# 4. expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument

challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(10))  # 'thirty    days      of        python'


# 5. find(): Returns the index of first occurrence of substring

challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th'))  # 0


# 6. format() formats string into nicer output
first_name = 'John'
last_name = 'Doe'
job = 'engineer'
country = 'USA'
sentence = 'I am {} {}. I am an {}. I live in {}.'.format(
    first_name, last_name, job, country)
print(sentence) 


radius = 10
pi = 3.14
area = pi * (radius ** 2)  # Fixed calculation syntax error
result = 'The area of circle with {} is {}'.format(str(radius), str(area))
print(result)  # The area of circle with 10 is 314.0


# 7. index(): Returns the index of substring (Raises ValueError if substring not found)
challenge = 'thirty days of python'
print(challenge.index('y'))  # 5
print(challenge.index('th'))  # 0


# 8. isalnum(): Checks alphanumeric character

# True: Contains only letters
challenge = 'ThirtyDaysPython'
print(challenge.isalnum())  # True

# True: Contains only letters and numbers
challenge = '30DaysPython'
print(challenge.isalnum())  # True

# False: Contains spaces, which are not alphanumeric
challenge = 'thirty days of python'
print(challenge.isalnum())  # False

# False: Contains spaces, even though it has numbers at the end
challenge = 'thirty days of python 2019'
print(challenge.isalnum())  # False


# 9. isalpha(): Checks if all characters are alphabets

challenge = 'thirty days of python'
# False: Contains spaces, which are not alphabetic characters
print(challenge.isalpha())  # False

num = '123'
# False: Contains numbers, not letters
print(num.isalpha())      # False


# 10. isdecimal(): Checks if all characters in the string are decimal characters (0-9)

# True: Contains only official decimal numbers
challenge = '123'
print(challenge.isdecimal())  # True

# False: Contains letters along with numbers
challenge = 'thirty days of python 2019'
print(challenge.isdecimal())  # False

# False: Contains symbols/spaces (even unicode numbers like '\u00B2' [²] return False here)
challenge = '12.3'
print(challenge.isdecimal())  # False


# 11. isdigit(): Checks Digit Characters

challenge = 'Thirty'
print(challenge.isdigit())  # False
challenge = '30'
print(challenge.isdigit())   # True



# 12. isidentifier(): Checks for valid identifier means it check if a string is a valid variable name

challenge = '30DaysOfPython'
print(challenge.isidentifier())  # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier())  # True


# 13. islower(): Checks if all alphabets in a string are lowercase

challenge = 'thirty days of python'
print(challenge.islower())  # True
challenge = 'Thirty days of python'
print(challenge.islower())  # False


# 14. isupper(): returns if all characters are uppercase characters

challenge = 'thirty days of python'
print(challenge.isupper())  # False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper())  # True


# 15. isnumeric(): Checks numeric characters

num = '10'
print(num.isnumeric())      # True
print('ten'.isnumeric())    # False


# 16. join(): Returns a concatenated string

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '#, '.join(web_tech)
print(result)  # 'HTML#, CSS#, JavaScript#, React'


# 17. strip(): Removes both leading and trailing characters from the string

# Example 1: Original code behavior
# It returns ' thirty days of python ' because 'y' is NOT at the absolute start or end (spaces are there)
challenge = ' thirty days of python '
print(challenge.strip('y'))  # ' thirty days of python '

# Example 2: Correct usage for removing spaces
# If empty, it removes spaces from the very beginning and the very end
challenge = ' thirty days of python '
print(challenge.strip())  # 'thirty days of python'

# Example 3: Correct usage for removing specific characters
# It successfully removes 'y' because they are at the absolute start and end of the string
challenge = 'ythirty days of pythony'
print(challenge.strip('y'))  # 'thirty days of python'


# 18. replace(): Replaces substring inside

challenge = 'thirty days of python'
print(challenge.replace('python', 'coding'))  # 'thirty days of coding'


# 19. split(): Splits String from Left

challenge = 'thirty days of python'
print(challenge.split())  # ['thirty', 'days', 'of', 'python']


# 20. title(): Returns a Title Cased String

challenge = 'thirty days of python'
print(challenge.title())  # 'Thirty Days Of Python'


# 21. swapcase(): Converts uppercase characters to lowercase and vice versa

challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # 'tHIRTY dAYS oF pYTHON'


# 22. startswith(): Checks if string starts with the specified prefix

challenge = 'thirty days of python'
print(challenge.startswith('thirty')) # True
print(challenge.startswith('days'))   # False
