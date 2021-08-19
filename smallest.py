# What's the smallest number

smallest=100
print('Before ',smallest)
for num in [9,41,12,3,74,15]:
    if num<smallest:
        print('then',smallest)
        smallest= num
        print('now' , num)
print('After ',smallest)
# not gonna work for very large value
