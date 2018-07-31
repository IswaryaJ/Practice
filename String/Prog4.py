#Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string
m = ('abc', 'xyz')
m1 = m[0]
m2 = m[1]
print(m2[:2]+m1[-1] , m1[:2]+m2[-1])

#Capitalize first and last letters of each word of a given string
def capitalize(str1):
    str1 = result = str1.title()
    result = ""
    for word in str1.split():
        result += word[:-1] + word[-1].upper() + " "
    return result[:-1]


print(capitalize("python exercises practice solution"))
print(capitalize("w3resource"))