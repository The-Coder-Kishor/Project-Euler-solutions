def palindrome(n): #program to check whether palindrom
    s = str(n)
    rev = s[::-1] #getting reverse
    if(s == rev):
        return True
l = 0 #to store largest
for i in range(100,1000):
    for j in range(100,1000):
        p = i * j
        if(palindrome(p) == True):
            if(p > l):
                l = p
print(l)
