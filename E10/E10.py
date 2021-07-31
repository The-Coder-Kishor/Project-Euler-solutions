import math
import time
def is_prime(n):
    if n <= 1:
        return False
    max_div = math.floor(math.sqrt(n))
    for i in range(2, 1 + max_div):
        if n % i == 0:
            return False
    return True

t0 = time.time()
sum = 0
c = 0 #for counting
for n in range(1,2000000):
    if is_prime(n):
        sum = sum + n
print(sum)
t1 = time.time()
print("Time required :", t1 - t0)