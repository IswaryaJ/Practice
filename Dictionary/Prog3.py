# Simple dictionary manipulations
n = 15
d = {x:x*x for x in range(1,n+1)}
print(d)

d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
d1.update(d2)
print(d1)

dict = {'data1':100,'data2':-54,'data3':247}
print(sum(dict.values()))
del dict['data1']
print(dict)


#Program to print unique values of a dictionary
d1=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
l1=[]
for i in d1:
for x,y in i.items():
if y not in l1:
l1.append(y)
print (l1)