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
#str
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

