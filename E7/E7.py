prime = [2]
def primecheck(n):
    if n not in prime:
        flag = 0
        for i in prime:
            if(n % i == 0):
                flag = 1
                break
        if flag == 0:
            prime.append(n)

i = 2
while (len(prime) < 10002):
    primecheck(i)
    i += 1

print(prime[10000])