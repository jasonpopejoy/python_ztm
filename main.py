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
#birth_year = input('What year were you born? ')
#age = 2023 - int(birth_year)
#print(f'You are {age} years old.')

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

#What is the output of this code?
#Before you clikc RUN, guess the output of each print statement!
new_list = ['a', 'b', 'c']
print(new_list[1]) # b
print(new_list[-2]) # b
print(new_list[1:3]) # b c
new_list[0] = 'z' # changes 'a' to 'z' in new_list
print(new_list) # z b c

my_list = [1,2,3] 
bonus = my_list + [5] 
my_list[0] = 'z' 
print(my_list) # z 2 3
print(bonus) # 1 2 3 5

# Matrix - desribes 2D lists - lists inside of lists
matrix = [
    [1,2,3],
    [2,4,6],
    [7,8,9]
]
# 0 accesses first list and 1 access the second index in the first list
print(matrix[0][1])

# using this list: 
basket = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
# access "Oranges" and print it:
print(basket[1][1][0])

# List Methods
#basket = [1,2,3,4,5]

#adding
#new_list = basket.append(100) #modifies list in place, doesn't create a new copy
#basket.insert(0, 101) #modifies list in place, doesn't create new copy
#new_list = basket.extend([102,104])
#print(basket)
#print(new_list)

#removing
#basket.pop() #pops off last item in list
#basket.pop(0) #removes at specified index, will return what is removed
#basket.remove(3) #removes actual value
#basket.clear() #completely clears what is in the list
#print(basket)

#indexing
basket = ['a', 'b', 'c', 'd', 'e', 'd']
print(basket.index('d')) # returns 3, as it specifies index of 'd'
print(basket.index('d', 0, 4)) #starts at index 0 and ends at index 4

print('d' in basket) #returns boolean
print('i' in 'hi my name is Ian')

print(basket.count('d')) #counts how many times a value is in a list

# using this list, 
basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# 1. Remove the Banana from the list
basket.pop(0)
# 2. Remove "Blueberries" from the list.
basket.pop()
# 3. Put "Kiwi" at the end of the list.
basket.append('Kiwis')
# 4. Add "Apples" at the beginning of the list
basket.insert(0, 'Apples')
# 5. Count how many apples in the basket
print(basket.count('Apples'))
# 6. empty the basket
basket.clear()
print(basket)

#sorting
basket = ['a', 'b', 'x', 'd', 'c', 'd', 'f', 'e']
basket.sort() #performs action in place
basket.reverse () #reverses
print(basket)
print(sorted(basket)) #produces a new list
new_basket = basket.copy() #copies to new list
print(new_basket)

#userful list tricks
print(len(basket))
print(basket[::-1]) # list slicing, creates a new list

print(list(range(1,100))) #starts at 1, ends at 99

new_sentence = ' '.join(['hi', 'my', 'name', 'is', 'jojo']) #string method
print(new_sentence)

#List Unpacking
a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
print(other)
print(d)

#fix this code so that it prints a sorted list of all of our friends (alphabetical). Scroll to see answer
friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']
new_friend = ['Stanley']

friends.extend(new_friend)
print(sorted(friends))

# None - represents the absence of value
weapons = None
print(weapons)


#Dictionaries - dict - data type and also a data structure
dictionary = {
    'a': [1,2,3],
    'b': 'hello',
    'x': True
} 
# dictioaries have unordered key:value pairs - scattered across memory
print(dictionary['b'])
print(dictionary)

my_list = [
    {
    'a': [1,2,3],
    'b': 'hello',
    'x': True
},
{
    'a': [4,5,6],
    'b': 'hello',
    'x': False
} 
]
print(my_list[0]['a'][2])
print(dictionary['a'][1])

# Understanding Data Structures
# what data structures to use when
# Dictionary is not sorted, can store more info, key:value pairs
# List has indexes and values

# Dictionary Keys - can be strings, int, bools, but not lists
# needs to be immutable and unique
# usually something descriptive 

# Dictionary Methods
user = {
    'basket': [1,2,3],
    'greet': 'hello',
    'age': 20
}

print(user.get('age')) # returns None because there is no 'age' key in user dict above
# .get is a function
print(user.get('age', 55)) # adds default value to age of 55, if age already exists in
# list, it will return original value

user2 = dict(name='jonjon')
print(user2)
# dict function to build dictionaries but is not as common as the first example

print('basket' in user)
print('size' in user.keys())
print('hello' in user.values())
print('....')
print(user.pop('age')) # .pop removes the key age and returns the value
print(user.items())
print(user.clear()) #clear in place removes - creates an empty dictionary
user2 = user.copy()
print(user2)
print(user.update({'age': 55})) # will update key age with new value, if value doesn't exist, will add it

#1 Create a user profile for your new game. This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'

user_profile = { 
    'age': 23,
    'username': 'Flerp',
    'weapons': ['ak', 'balisong'],
    'is_active': True,
    'clan': 'Derp' 
}

#2 iterate and print all the keys in the above user.
print(user_profile.keys())
#3 Add a new weapon to your user
user_profile['weapons'].append('sais')
print(user_profile)
#4 Add a new key to include 'is_banned'. Set it to false
user_profile.update({'is_banned': False})
print(user_profile)
#5 Ban the user by setting the previous key to True
user_profile['is_banned'] = True
print(user_profile)
#6 create a new user2 my copying the previous user and update the age value and username value. 
user_profile2 = user_profile.copy()
user_profile2.update({'age': 69, 'username': 'Pope'})
print(user_profile2)

# Tuples