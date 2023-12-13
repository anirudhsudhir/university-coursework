s = [
    ("890", "ram", (95, 78, 99)),
    ("123", "kishan", (90, 98, 89)),
    ("567", "arjun", (59, 68, 100)),
]

sorted_list_one = []
sorted_list_two = []


def return_name(tuple_data):
    return tuple_data[1]


def return_total_marks(tuple_data):
    marks = tuple_data[2]
    return sum(marks)


def sort(s):
    global sorted_list_one, sorted_list_two
    sorted_list_one = sorted(s, key=return_name)
    sorted_list_two = sorted(s, key=return_total_marks, reverse=True)


sort(s)
print(sorted_list_one)
print(sorted_list_two)
