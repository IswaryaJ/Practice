#Program to work with limited lines of a file
m =4
with open('File1.txt' ,'r') as f:
    line = f.readlines()[-m:]
    for i in line:
        print(i)