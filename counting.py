# counting
z=0
total=0
print('before count',z,'total',total)
for thing in [9,41,12,3,74,15]:
    z=z+1
    total=total+thing
    print(z,thing,total)
print('After count',z,'total',total,'Avg',total/z)

print('Start')
for value in [9,41,12,3,74,15]:
    if value>25:
        print('value',value)
print('end')
