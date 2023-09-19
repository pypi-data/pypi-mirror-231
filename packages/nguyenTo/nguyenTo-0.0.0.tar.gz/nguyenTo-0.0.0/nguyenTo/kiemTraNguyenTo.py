import math

def check(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    
    max_divisor = math.isqrt(x) + 1
    for i in range(3, max_divisor, 2):
        if x % i == 0:
            return False
    
    return True