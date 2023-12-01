n = int(input('Enter the number of elements to be added: '))
li, j, li2 = [], 0, []
for i in range(n):
    li.append(int(input('Enter a number: ')))
for i in range(len(li)):
    if i == len(li)-2:
        j = li[i+1]
        k = li[0]
    elif i == len(li)-1:
        j = li[0]
        k = li[1]
    else:
        j = li[i+1]
        k = li[i+2]
    li2.append(j+k)
print(li2)
