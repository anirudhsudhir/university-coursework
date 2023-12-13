words = ["3erd", "food", "90ul", "cold"]


def myfilter(fn, data):
    new_li = []
    for val in data:
        if fn(val):
            new_li.append(val)

    return new_li


def check_first_num(v):
    if len(v) > 0 and v[0].isdigit():
        return False
    return True


print(myfilter(check_first_num, words))
