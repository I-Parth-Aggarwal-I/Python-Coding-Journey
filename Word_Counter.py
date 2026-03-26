def word_counter(text):
    words = text.split()
    return len(words)

s = input("Enter a string: ")
print(f"The number of words in the string is: {word_counter(s)}")