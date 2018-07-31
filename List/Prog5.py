#Write a Python function that takes two lists and returns True if they have at least one common member

def func(m,n):
    result = False
    for i in m:
        for j in n:
            if(i == j):
                result = True
                return result
print(func([1,2,3,4,5],[6,7,8,9,5]))





0