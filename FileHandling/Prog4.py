#Program to find the length of the lines
with open('File1.txt','r') as f:
    lines = f.readlines()
    print(len(lines))