# Write a Python program to count the number of characters (character frequency) in a string.
from collections import Counter
m = 'google.com'
count = Counter(m)
print(count)

#Prgram to reverse words the string
def reverse_string_words(text):
    for line in text.split('\n'):
        return(' '.join(line.split()[::-1]))
print(reverse_string_words("The quick brown fox jumps over the lazy dog."))
print(reverse_string_words("Python Exercises."))