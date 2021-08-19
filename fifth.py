
val=input('Enter x : ')
x=int(val)

if x%2 == 1:
    print('odd number')
elif x%2 == 0:  #means else and if
    print('even number')
print('DONE \n')

value=input('Enter y : ')
y=int(value)

if y<2:
    print('small')
elif y<10:
    print('Big')
elif y<50:
    print('large')
else:
    print('gaint')
