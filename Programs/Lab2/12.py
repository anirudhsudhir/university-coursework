words = eval(input("Enter the words: "))
target_letter = input("Enter the target letter: ")

filtered_words = filter(lambda word: target_letter in word, words)

print(list(filtered_words))
