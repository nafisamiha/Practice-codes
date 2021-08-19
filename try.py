rawstr=input('Enter any number : ')
try:
    val=int(rawstr)
except:
    val=-1

if val>0:
    print('well done')
else:
    print('not a number')
