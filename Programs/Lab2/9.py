def read_len(file1):
    counter = 0
    for letter in file1.read():
        if letter.isalpha():
            counter += 1

    return counter


def fn(fn1):
    with open("sample.txt") as file:
        print("sample.txt: ", fn1(file))
    with open("test.txt") as file:
        print("test.txt: ", fn1(file))


fn(read_len)
