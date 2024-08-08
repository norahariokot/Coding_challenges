# Program to check if two words are anagrams
word_1 = input("Enter first word: ")
word_2 = input("Enter second word: ")

# First check for length equality
if len(word_1) == len(word_2):
    # 1. if equal create dictionaries to check for the  frequencies of the characters in each word
    char_frequency1 = {}
    char_frequency2 = {}
    for i in word_1:
        if i in char_frequency1:
            char_frequency1[i] += 1
        else:
            char_frequency1[i] = 1
    for i in word_2:
        if i in char_frequency2:
            char_frequency2[i] += 1
        else:
            char_frequency2[i] = 1  

     # compare the dictionaries for equality        
    if char_frequency1 == char_frequency2:
        print(f"{word_1} is an anagram of {word_2}")
    else:
        print(f"{word_1} is not an anagram of {word_2}")         
else:
    print(f"{word_1} is not an anagram of {word_2}")

#print(char_frequency1)  
#print(char_frequency2)  


