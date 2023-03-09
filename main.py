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