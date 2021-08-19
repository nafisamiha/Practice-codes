# continue means go to the 1st line

while True:
    line=input ('>')
    if line[1]=='#':
        continue
    if line=='done':
        break
    print(line)
print('end!')
