"""
Created on Fri Dec  3 23:20:27 2021

@author: Samiha
"""

# filters 
def is_even(num):
    if num%2==0:
        return True
    
    
numbers=[1,2,3,45,56,67,84,103,256]



result2=[]
for num in numbers:
    if is_even(num):
        result2.append(num)
print(result2)


result3=[]
result3=filter(is_even,numbers)
print(result3)
