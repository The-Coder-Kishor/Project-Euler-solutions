for a in range(1,1001):
    for b in range(1,1001-a):
        for c in range(1,1001-a-b):
            if(a + b + c == 1000):
                if(a<b and b<c):
                    lhs = a**2 + b**2
                    rhs = c**2
                    if(lhs == rhs):
                        prod = a * b * c
                        print(prod)