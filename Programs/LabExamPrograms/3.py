n = int(input('Enter n: '))
for i in range(1, n+1):
    for j in range(i, n):
        print('#', end='')
    for j in range(i, 0, -1):
        print(j, end='')
    print()
