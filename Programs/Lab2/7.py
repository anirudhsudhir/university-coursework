inp = eval(input("Enter a tuple: "))
threshold = int(input("Enter the threshold: "))

filtered_vals = list(filter(lambda x: x > threshold, inp))

square_vals = map(lambda x: x * x, filtered_vals)

square_vals = tuple(square_vals)

sum_square_vals = sum(square_vals)

print("sum is: ", sum_square_vals)
