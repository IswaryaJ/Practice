#Program to join a tuple
tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
str1 = ''.join(tup)
print(str1)


# Write a Python program to create the colon of a tuple.
from copy import deepcopy
tuplex = ("HELLO", 5, [], True)
print(tuplex)
tuplex_clone = deepcopy(tuplex)
tuplex_clone[2].append(50)
print(tuplex_clone)
print(tuplex)

#Program on tuple manipulation
num = [10,20,(10,20),40]
m = 0
for i in num:
    if isinstance(i,tuple):
        break
    m += 1
print(m)

#Sort tuple by its float element
import operator
k=[('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
print (list(reversed(sorted(k,key=operator.itemgetter(1)))))