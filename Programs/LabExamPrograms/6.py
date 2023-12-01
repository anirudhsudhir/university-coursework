n = int(input('Enter the number of elements to be added: '))
k = int(input('Enter the value of k: '))
li = []
for i in range(n):
    li.append(int(input('Enter a number: ')))
li = sorted(list(set(li)))
if len(li) <= k:
    print("None")
else:
    print(li[k-1])
