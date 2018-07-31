#Program using zip
color_dict = {'red':'#FF0000',
          'green':'#008000',
          'black':'#000000',
          'white':'#FFFFFF'}

m = sorted(color_dict.items())
print(m)

keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']
m = dict(zip(keys,values))
print(m)


my_dict = {'x':500, 'y':5874, 'z': 560}
n = max(my_dict.values())
print(n)
