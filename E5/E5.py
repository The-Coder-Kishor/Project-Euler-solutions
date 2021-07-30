primes = [2,3,5,7,11,13,17,19]

def findlcm(x,y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    lcm = int((x * y)/hcf)
    return lcm

lcm = 1
for i in range(1,20):
    lcm = findlcm(i,lcm)
print(lcm)
