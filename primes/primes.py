import test
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def get_primes(n):
    lst = []
    for i in range(2, n):
        if is_prime(i):
            lst.append(i)
    return lst

lst = get_primes(test.max_prime)
# test.check_primes(lst)
