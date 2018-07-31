#Program to find the largest word
with open('File1.txt' , 'r') as f:
    words = f.read().split()
    print(words)
max_len = len(max(words, key=len))
print(max_len)
print[word for word in words if len(word) == max_len]


