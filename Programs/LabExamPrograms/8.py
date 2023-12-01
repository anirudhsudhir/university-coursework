n = int(input('Enter the number of rows : '))
li, templi = [], []
for i in range(n):
    for j in range(n):
        templi.append(int(input('Enter a number: ')))
    li.append(templi)
    templi = []
sum = 0
for i in range(n):
    sum += li[i][i]
print(sum)
