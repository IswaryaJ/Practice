#Program using islice
from itertools import islice
nlines = 2
with open('File1.txt' , 'r') as f:
    for line in islice(f, nlines):
        print(line)
