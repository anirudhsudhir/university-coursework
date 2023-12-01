dict = {}
for i in range(int(input('Enter the number of elements to be added: '))):
    element = input('Enter the element: ')
    datatype = input('Enter the datatype: ')
    dict[element] = datatype
for i, j in dict.items():
    if j == 'string':
        print(i, end=' ')
