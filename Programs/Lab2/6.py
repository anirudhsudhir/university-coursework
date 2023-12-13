li1 = eval(input("List 1: "))
li2 = eval(input("List 2: "))

set1 = set(li1)
set2 = set(li2)
print("Common elements: ", list(set1.intersection(set2)))
