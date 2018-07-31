# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters
def func(s1):
    l = 0
    u = 0
    for i in s1:
        if i.isupper():
            l += 1
        elif i.islower():

            u += 1
    print(l)
    print(u)
func("The quick Brow Fox")


