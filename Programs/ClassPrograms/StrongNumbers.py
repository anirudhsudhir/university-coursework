end = int(input("Enter the range to find Strong numbers: "))
count = 0
i = 1
while i < end:
    sumFactorial = 0
    num = i
    while num > 0:
        factorial = 1
        for j in range(int(num % 10)):
            if j != 0:
                factorial *= j
        sumFactorial += factorial
        num /= 10
    if sumFactorial == i:
        if count == 0:
            print("The strong numbers present in the given range are:")
            count += 1
        print(i)
    i += 1

if count == 0:
    print("No strong numbers present in the given range")
