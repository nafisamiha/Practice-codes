# the absence of value

smallest=None
print('Before ',smallest)
for num in [9,41,12,3,74,15]:

    if smallest is None:
        smallest=num
    elif num<smallest:
        smallest=num
    print(num , smallest)

print('After ',smallest)
