def print_matrix():
    for i in range(n):
        for j in range(n):
            print(li[i][j], end=' ')
        print()


n = int(input('Enter the number of rows : '))
li, templi = [], []
for i in range(n):
    for j in range(n):
        templi.append(int(input('Enter a number: ')))
    li.append(templi)
    templi = []
print_matrix()
print("Transpose: ")
for i in range(n):
    for j in range(i, n):
        temp = li[i][j]
        li[i][j] = li[j][i]
        li[j][i] = temp
print_matrix()
