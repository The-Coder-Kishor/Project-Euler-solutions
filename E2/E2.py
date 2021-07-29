sum = 0 #to store the sum
a = 1
b = 2
sum = 2
c = a + b
while(c <= 4000000):
    if(c%2==0):
        sum += c
    a = b
    b = c
    c = a + b
print(sum)
