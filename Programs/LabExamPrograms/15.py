string = input('Enter a string: ')
li = []
for i in range(len(string)+1):
    for j in range(i+1, len(string)+1):
        li.append(string[i:j])
li = sorted(list(set(li)))
print(li)
