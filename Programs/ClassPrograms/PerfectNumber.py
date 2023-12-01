num = int(input("Enter a number: "))
i = 1
sumDivisor = 0
while i < num:
    if num % i == 0:
        sumDivisor += i
    i += 1
if sumDivisor == num:
    print("It is a perfect number")
else:
    print("It is not a perfect number")
