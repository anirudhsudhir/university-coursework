nums = [i for i in range(int(input("Enter the range of numbers to be added: ")) + 1)]


def myreduce(fn, vals):
    if len(vals) == 1:
        return vals[0]
    vals[1] = fn(vals[0], vals[1])
    return myreduce(fn, vals[1:])


count = 0


def my_fn(x, y):
    return x + y


print(myreduce(my_fn, nums))
