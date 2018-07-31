#Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself
m = 'restart'
n = ''
for i in  m:
    if i in n and i == m[0]:
        i = '$'
        n += i
    else:
        n  += i
print(n)

