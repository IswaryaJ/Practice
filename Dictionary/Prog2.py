#Program on dictionary manipulation
m = {0: 10, 1: 20}
m.update({2:30})
print(m)
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 ={}
for i in (dic1,dic2,dic3):
    dic4.update(i)
    print(dic4)


# Program to get values from dictionary
dict = {1: 10, 2: 20, 3: 30, 4: 40}
print(2 in dict)
print(5 in dict)