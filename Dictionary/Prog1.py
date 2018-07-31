#program on getting sorted dictionaries
import operator
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
item1 = sorted(d.items(),key = operator.itemgetter(0))
item2 = sorted(d.items(),key = operator.itemgetter(0),reverse = True)
print(item1)
print(item2)

