string = input('Enter a string: ')
updatestring = ''
for i in string:
    if i.isalpha():
        if i == 'z':
            updatestring += 'a'
        elif i == 'Z':
            updatestring += 'A'
        else:
            updatestring += chr(ord(i)+1)
    else:
        updatestring += i
print(updatestring)
