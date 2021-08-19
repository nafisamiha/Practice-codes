count=0
total=0
while True:
    val=input('Enter a Number: ')
    if val=='done':
        break
    try:
        fval=float(val)
    except:
        print('Invalid Input')
        continue
    print(fval)
    count=count+1
    total=total+fval

print('ALL DONE')
print('count',count,'total',total)
