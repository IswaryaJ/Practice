# Program to find the larger num
m = [2,5,4,8,6]
n = 0
for i in m:
    if (i>n):
        n = i
print(n)


#Write a Python program to sort a list of nested dictionaries.
new_list = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]
print("Original List: ")
print(new_list)
new_list.sort(key=lambda e: e['key']['subkey'], reverse=True)
print("Sorted List: ")
print(new_list)