import math

def is_prime_number(x):
    #제곱근의 +1까지만 판별해도됨
    for i in range(2, int(math.sqrt(x))+1):

        if x % i == 0:
            return False
    return True