string1 = input('Enter a string: ')
string2 = input('Enter a string: ')
list1, list2 = sorted(list(string1)), sorted(list(string2))
if list1 == list2:
    print('Anagrams')
else:
    print('Not Anagrams')
