#Program to multiply
m = [2,4,5,8,9]
n = 1
for i in m:
    n = i*n
    i+=1
print(n)


#Write a Python program to flatten a shallow list
import itertools
original_list = [[2,4,3],[1,5,6], [9], [7,9,0]]
merged_list = list(itertools.chain(*original_list))
print(merged_list)