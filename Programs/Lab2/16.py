names = ["Raj", "Prakash", "David", "Quack"]


def myreduce(fn, vals):
    if len(vals) == 1:
        return vals[0]
    vals[1] = fn(vals[0], vals[1])
    return myreduce(fn, vals[1:])


count = 0


def my_fn(x, y):
    global count
    count += 1
    return x[:count] + y[0]


print(myreduce(my_fn, names))
