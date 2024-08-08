# Program to check if two words are anagrams
word_1 = input("Enter first word: ")
word_2 = input("Enter second word: ")

counter = 0
for i in word_1:
    if i in word_2:
        counter += 1
        print(f"{i} in {word_2}")
if counter == len(word_2):
    print(f"{word_1} is an anagram of {word_2}")
else:
    print(f"{word_1} is not an anagram of {word_2}")    