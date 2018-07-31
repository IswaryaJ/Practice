str = "malayalam"
for i in xrange(0,len(str)/2):
    if str[i]!= str[len(str)-i-1]:
        print ("Not a palindrome")
    else:
        print ("Palindrome")