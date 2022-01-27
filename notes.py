# -*- coding: utf-8 -*-

import random
num = random.randint(0,10)
print(num)

# Conditionals

age = 19

if age < 17:
    print('Too young')
elif age <= 30 and age >= 18 : # and & or are spelled out in Python
    print('You\'re good')
else:
    print('Ok boomer')

'spider' in 'spider-man' #Returns true

# Loops

b = 0;

while b <= 6:
    print("hi")
    b += 1


for i in range(1,10):
    print(i)
    
var = [1,3,10]

for j in var:
    print(j)
    
# Strings
#   Are immutable but operate like vectors

s = "hello world"
s[0] # First character
s[-1] # Can also index from reverse using neg values (last character is -1)

s[3:6] # Slices a string from the 3rd to 6th index
s[0:len(s):2] #Slices same thing but with a step of 2 (every two chars)
s[::-1] #Reverses (also note you can omit numbers)
s[4:1:-2]

s = 'y' + s[1:len(s)] # Can use something like this to change characters
# Can concatenate two strings together using +

# Two ways to use loops with strings
for i in range(len(s)):
    if s[i] == 'i':
        print("Found i")

for char in s:
    if s[i] == 'i':
        print("Found i")


    
# Functions
#   def FunctionName (parameter)
#   """ stands for the function information

def is_even (i):
    """

    Parameters
    ----------
    i : a positive integer
        

    Returns True if Even, False if Odd
    -------

    """
    remainder = i%2
    return remainder == 0


# Tuples
#   Immutable objects (can't change values once they're stored)
#   Can consist of any class of data
#   Denote with ()

print(is_even(3))

t = (2,"mit",3)
e = (5,6)
r = t+e
print(r)
print(t[1:3])


# Lists
#   Are mutable objects (can change what's inside)
#   Denote with []

ShoppingList = ['milk','bread','tofu']
print(ShoppingList)
ShoppingList.append('apples')
print(ShoppingList)

print(len(ShoppingList)) # Gives length
print(ShoppingList[1])

ShoppingList[1] = "bananas" # Can change elements
print(ShoppingList)

ShoppingList.extend(['avocados','pineapples']) # Extends list by these elements
ShoppingList2 = ['eggs','chicken']
ShoppingList += ShoppingList2 # Can add two lists together
print(ShoppingList)

del(ShoppingList[2]) # Deletes by index
ShoppingList.pop() # Removes last element
ShoppingList.remove('eggs')
print(ShoppingList)

s = "I love CS"
list(s) # Converts list into string of every character
s.split(' ') # Seperates into words by splitting at certain characters
L = ['b','c','d','a']
' '.join(L) # Joins lists into strings

L2 = sorted(L) # Sorts L but does not change the list
L.sort() # Sorts L and changes it
L.reverse() # Reverses L

L3 = L[:] # Cloning a list to make a copy

warm = ['yellow','orange']
hot = ['red']
brightcolors = [warm,hot] #Can have nested lists
print(brightcolors) 
print(brightcolors[0][1])

L4 = [1,2,3,4]
L5 = [1,2,5,6]

def remove_dups (L4,L5):
    L4_copy = L4[:] #When working with loops and lists make sure to make a copy for the looping
    for i in L4_copy:
        if i in L5:
            L4.remove(i)

remove_dups(L4,L5)
print(L4)


# Dictionaries
#   Difference b/w lists is that it indexes based off a key and not just integers 0 to inf
#   Uses curly braces, and notation of {'key1':'val1, 'key2':'val2', etc. }
#   To access elements, you call dictionary_name['key1'] and the output would be 'val1'
#   Keys need to be unique from each other
#   Keys also need to be immutable (int,float,string,bool,etc.)
#   Values could any type
#   No order is guaranteed

empty = {} # Empty dictionary

grades = {'John':'A+','Ana':'B','Denise':'A','Katy':'A'}
grades['John']
grades['Sylvan'] = 'A' # To add something into the dictionary
'John' in grades # Tests if a key is in the dictionary (returns T or F)
del(grades['Ana']) # Deletes an entry
grades.keys() # Returns an iterable (acts like a tuple) of all the keys
grades.values() # Same but returns all of the values

# Debugging in Python

# Exceptions
#   Does entire try statement and if without bugs it runs fine
#   If there is a bug it will run the code in the except block instead of giving an error
#   Can have multiple except blocks for different errors (like if else blocks)
try: 
    a = int(input("Input first number:"))
    b = int(input("Input second number:"))
    print(a/b)
except ValueError:
    print("Could not convert into a number")
except ZeroDivisionError:
    print("Can't divide by 0")
except:
    raise Exception("Bad args for input") # Can raise your own exceptions
else: # Executes when code in try block ran successfully
    print("Hooray")
finally: # Always going to get executed
    print("This always happens")

# Assertions
#   Example of defensive programming
#   Usually at beginning or end of function
#   Asserts that the parameters given to a function are exactly what the function is supposed to take in
grades = [90,85,78]
grades_null = []
def avg_grades(grades):
    assert len(grades) != 0, 'No grades data' # asserts that there is a non-zero input
    return (sum(grades)/len(grades))

print(avg_grades(grades))
print(avg_grades(grades_null)) 
    
# Objects
#   Classes allow you to create your own type of objects
#   These can then be used and mutated like any other object class (ie lists, dictionaries, int, etc.)

class Coordinate (object): # in parentheses is the class parent (object is the basic type)
    # Put class attributes (data and procedures that belong to the class)
    # Data are the other objects that make up this class
    # Procedures are like functions that only work on this class
    def __init__(self,x,y): # Special function that initializes the object
        self.x = x # Self is a placeholder to refer to any characteristics of the class before it is actually created
        self.y = y
        
c = Coordinate(3,4) # Can then use class (no need for self arg) (3 and 4 are passed into init function)
print(c.x) # Use the dot notation to access 


# Examples

# Bisection Search

n = int(input("Enter number: "))
lower_bound = int(input("Lower bound: "))
upper_bound = int(input("Upper bound: "))

def bisection_search(n,lower_bound,upper_bound):
    found_num = False
    while found_num == False:
        guess = int((upper_bound + lower_bound)/2)
        
        if guess == n:
            found_num = True
            return guess
        
        elif n < guess:
            upper_bound = guess
            
        elif n > guess:
            lower_bound = guess
            
        print("Upper bound: ", upper_bound, "Lower bound: ", lower_bound)
        
print(bisection_search(n,lower_bound,upper_bound))
