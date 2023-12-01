def shift(i):
    if i == 'Z' or i == 'z':
        return chr(ord(i)-27)
    elif i.isalpha():
        return chr(ord(i)+1)
    return i


string = input('Enter a sentence: ')
move = int(input('Enter the shift value: '))
finalstring = ''
for i in string:
    temp = i
    for j in range(move):
        temp = shift(temp)
    finalstring += temp
print(finalstring)
