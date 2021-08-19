# What's the largest number

Largest=-1
print('Before ',Largest)
for num in [9,41,12,3,74,15]:

    if num>Largest:
        print('then',Largest)
        Largest= num
        print('now' , num)
print('After ',Largest)
