#Program to convert into a set
m = [2,4,6,3,4,2]
print(list(set(m)))


#Write a Python program to remove duplicates from a list of lists.
num = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
n2=[]
for i in num:
if i not in n2:
n2.append(i)
print(n2)