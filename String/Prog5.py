#Write a Python function that takes a list of words and returns the length of the longest one

m = ["PHP", "Exercises", "Backend"]
n = sorted(m , key = len)
print(n[-1])



#Print all permutations with given repetition number of characters of a given string
from itertools import product
def repeat(str1, rno):
  chars = list(str1)
  results = []
  for c in product(chars, repeat = rno):
    results.append(c)
  return results
print(repeat('xyz', 3))
print(repeat('xyz', 2))
print(repeat('abcd', 4))