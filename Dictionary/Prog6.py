# Write a Python program to combine values in python list of dictionaries.
from collections import Counter
dict = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750} , {'item': 'item2', 'amount': 400}]
result = Counter()
for d in dict:
    result[d['item']] += d['amount']
print(result)

#Program to find the count of letters
s = 'w3resource'
print(Counter(s))

#Program to sort
l = {'n3': [2, 3, 1], 'n2': [5, 1, 2], 'n1': [3, 2, 4]}
m = {x: sorted(y) for x,y in l.items()}
print(m)

#Program to sort by marks
from collections import Counter
x = Counter({'Math':81, 'Physics':83, 'Chemistry':87})
print(x.most_common())


#Program to combine values
def func(list_of_dicts):
    for d in list_of_dicts:
        n1 = d.pop('V')
        n2 = d.pop('VI')
        d['V+VI'] = (n1 + n2)/2
    return list_of_dicts
student_details= [
  {'id' : 1, 'subject' : 'math', 'V' : 70, 'VI' : 82},
  {'id' : 2, 'subject' : 'math', 'V' : 73, 'VI' : 74},
  {'id' : 3, 'subject' : 'math', 'V' : 75, 'VI' : 86}
]
print(func(student_details))