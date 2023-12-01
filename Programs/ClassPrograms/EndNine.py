end = int(input("Enter the end of the range: "))
count = 0
for i in range(end):
    if i % 10 == 9:
        if count == 0:
            print("The numbers which end with 9 in the given range are: ")
            count += 1
        print(i)
if count == 0:
    print("There are no numbers which end with 9 in the given range")
