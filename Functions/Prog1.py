#Program to find the largest number
def func(list1):
    n = 0
    for i in list1 :
        if i > n:
            n = i
    return n
print(func([5,3,7,8,2]))