num = input("Enter a five digit number: ")
swapNum = num[len(num) - 1] + num[1 : len(num) - 1] + num[0]
print("Swapped number is: ", swapNum)
