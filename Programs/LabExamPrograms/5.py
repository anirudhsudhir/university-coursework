n = int(input('Enter the number of elements to be added to the list: '))
li, li2, li3 = [], [], []
for i in range(n):
    li.append(input('Enter the element: '))
for i in li:
    if li.count(i) == 2:
        li2.append(i)
li2 = list(set(li2))
for i in li2:
    li3.extend([i, i])
print(li, li3)
