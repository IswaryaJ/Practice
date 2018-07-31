#Program which counts both dictionaries
from collections import Counter
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d = Counter(d1) + Counter(d2)
print(d)

#Write a Python program to print all unique values in a dictionary and three highest values.
d1=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
d2 = []
for i in d1:
    for x,y in i.items():
        if y not in d2:
            d2.append(y)
d2 = sorted(d2)
print(d2[-3:])



