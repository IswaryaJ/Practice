#Program to count the words in a file
from collections import Counter
with open('File1.txt' , 'r') as f:
    lines = f.read().split()
    print(Counter(lines))


