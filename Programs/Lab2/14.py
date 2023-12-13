words_list = ["study", "help", "work", "enjoy", "walk"]


def mymap(fn, data):
    new_li = []
    for val in data:
        new_li.append(fn(val))
    return new_li


def add_ing(val):
    return (val, len(val))


print(mymap(add_ing, words_list))
