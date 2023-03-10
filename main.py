#name = input('What is your name? ')
#print('Hello ' + name)

#Fundamental Data Types
#int - whole numbers
print(type(2 + 4))
print(type(2 - 4))
print(type(2 * 4))
print(type(2 / 4))
print(2 ** 3)
print(5 // 4) # gets rounded to the nearest int
print(5 % 4) # divides and displays remainder 
print(round(3.1)) #rounds the number
print(abs(-21)) #returns absolute value of number (no negative)
#float - floating point number (ie. has a decimal point)
#bool
#str - string, ie a piece of text
#list
#tuple
#set
#dict

#Classes -> custom types
#Specialized Data Types - modules
#None 
#complex - used in complex math but is rarely used



#Operator precedence
print(20 - 3 * 4) #multiplies first
# ()
# **
# * /
# + - 
#
# Guess the output of each answer before you click RUN
# Try to write down your answer before and see how you do... keep it mind I made it a little tricky for you :)
print((5 + 4) * 10 / 2)
45.0
print(((5 + 4) * 10) / 2)
45.0
print((5 + 4) * (10 / 2))
45.0
print(5 + (4 * 10) / 2)
25.0
print(5 + 4 * 10 // 2)
25

print(bin(666)) #prints binary number
print(int('0b101', 2)) #converts bin to int

#Variables - store info in our proram/script
#Best practices / rules for writing variables:
#snake_case
#start with lowercase or underscore
#letters, numbers, underscores
#case sensitive
#don't overwrite keywords
#don't use dunders ie. __variable_name
#make variable names descriptive 

user_iq = 190 #user_iq is the variable
print(user_iq)
user_age = user_iq/4
a = user_age
print(a)

a,b,c = 1,2,3 #quick way to assign multiple variables
print(a)
print(b)
print(c)
#constants 
PI = 3.14 # all caps to indicate it's a constant, good practice not to change the varialbe

iq = 100 #this is also a statement
user_age = iq / 5 #expression is 'iq / 5'
#statement is 'user_age = iq / 5' the whole line of code

#augmented assignment operator
some_value = 5
some_value += 2 #-= *= etc., operator goes to the left of the = sign
print(some_value)

counter = 0

counter += 1
counter += 1
counter += 1
counter += 1
counter -= 1
counter *=2

#Before you click RUN, guess what the counter variable holds in memory!
6
print(counter)

#strings
print(type('Hi, hello there'))
username = 'supercoder'
password = 'supersecret'
long_string = '''
WOW
O.O
---
'''
print(long_string)
#''' for multiline strings
first_name = 'Derp'
last_name = 'McGurp'
full_name = first_name + ' ' + last_name
print(full_name)

#string concatination - only works with strings, not ints
print('hello' + ' derp')

#type conversion
print(type(str(100))) #converted 100 into a string
# ^ same as:
a = str(100)
b = type(a)
print(b)

#escape sequence
weather = '\t It\'s "kind of" sunny \n hope you have a good day'
print(weather)
# \t tabs, \n newline

#formatted strings 
name = 'Johnny'
age = 55
print(f'Hi, {name}. You are {age} years old')
#.format - usually used in python 2. fstrings are better/easier
print('Hi, {}. You are {} years old'.format(name, age))

#string indexes
selfish = '01234567'
#          01234567
#slicing      v
print(selfish[0])
print(selfish[7])
#[start:stop:stepover]
print(selfish[0:2])
print(selfish[0:8])
print(selfish[0:8:2])
print(selfish[1:])
print(selfish[:5])
print(selfish[::1])
print(selfish[-1])
print(selfish[::-1]) #reverses order of sring

#Guess the output of each print statement before you click RUN!
python = 'I am PYTHON'

print(python[1:4])
# am 
print(python[1:])
# am PYTHON
print(python[:])
#I am PYTHON
print(python[1:100])
# am PYTHON
print(python[-1])
#N
print(python[-4])
#T
print(python[:-3])
#I am PYT
print(python[-3:])
#HON
print(python[::-1])
#NOHTYP ma I

#Immutability 
#selfish[0] = '8' is invalid code because of immutability 
# only way to change is to reassign string to selfish 

#Built in Functions and Methods
print(len('hellooooooo')) #len() calulates the length of a string, starting at 1
#.format() - method starts with dot .
quote = 'to be or not to be'
print(quote.upper()) #uppercase string
print(quote.capitalize()) #capitalizes first letter
print(quote.find('be')) #be starts at index 3
print(quote.replace('be', 'me'))

#Booleans
#bool can only be either True or False
name = 'Andrei'
is_cool = False

is_cool = True

print(bool(1))
#1 evaluates to True, 0 to False

#Type conversion exercise
birth_year = input('What year were you born? ')
age = 2023 - int(birth_year)
print(f'You are {age} years old.')

# Developer Fundametals II
# https://realpython.com/python-comments-guide/


# Lists - ordered sequence of objects of any type
# aka 'arrays' in other languages
li = [1,2,3,4,5]
li2 = ['a', 'b', 'c']
li3 = [1, 2, 'a', True]

amazon_sucks = ['notebooks', 'sunglasses']
print(amazon_sucks[0]) #accessing index of list

# List slicing
amazon_sucks = [
    'notebooks',
    'sunglasses',
    'board games',
    'cheap crap'
]
print(amazon_sucks[0:2]) #functions similar to string slicing
print(amazon_sucks[0::2])

amazon_sucks[0] = 'laptop' 
print(amazon_sucks[0:3])
print(amazon_sucks)

# Copies to a new list  v
new_cart = amazon_sucks[:]

# Matrix - desribes 2D lists - lists inside of lists
matrix = [
    [1,2,3],
    [2,4,6],
    [7,8,9]
]
# 0 accesses first list and 1 access the second index in the first list
print(matrix[0][1])


# List Methods