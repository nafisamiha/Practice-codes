
"""
Created on Fri Dec  3 22:57:07 2021

@author: Samiha
"""

# a pure function that takes a number in and returns it by adding 1.

def increment_one(number):
    return number+1

def is_even(number):
    if number%2==0:
        return True

numbers=[1,2,3,45,56,67,84,103,256]

#procedural way
result=[]
for num in numbers:
    result.append(increment_one(num))
print(result)

# The append() method takes a single item as an input parameter and adds that to the end of the list. 
# The items inside a list can be numbers, strings, another list, dictionary.

result2=[]
for num in numbers:
    if is_even(num)==True:
        result2.append(num)
print(result2)

result1=[]
#functional way 
result1=map(increment_one,numbers)
print(result1)

# The map() method creates a new array populated with the results of calling a provided function on every element in the calling array.

result3=[]
result3=filter(is_even,numbers)
print(result3)

# filter is a higher order function that takes on another function


# lamda takes on two functions and executes any operations


#Procedural way 
result4=0
for num in numbers:
    result4=result4+num
    print(result4)
    
result5=0
# functional way 
from functools import reduce
result5=reduce(lambda x, y: x+y,numbers)
print(result5)
 

