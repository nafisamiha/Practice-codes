#to break infinite loop

while True:
    line=input('>')
    if line=='done':
        break
    print(line)
print('end!')
