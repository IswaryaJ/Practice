from shutil import copyfile
copyfile('File1.txt', 'File2.txt')

with open('File1.txt','r') as f1 , open('File2.txt','r') as f2:
    for m1,m2 in zip(f1,f2):
        print(m1+m2)
