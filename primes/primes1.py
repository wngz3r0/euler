import test
primes = []
def is_prime(n):
    global primes
    for i in primes:
        if n % i == 0:
            return False
    return True

def get_primes(n):
    global primes
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
    return primes

lst = get_primes(test.max_prime)
# test.check_primes(lst)
