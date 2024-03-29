# Checks to see if n is a prime number
max_prime = 50000
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def check_primes(primes):
    cur_prime_idx = 0
    for i in range(2, max_prime):
        if is_prime(i):
            if cur_prime_idx >= len(primes) or primes[cur_prime_idx] != i:
                print (i, "IS a prime but wasn't in the array")
                return False
            cur_prime_idx += 1
        elif cur_prime_idx < len(primes) and primes[cur_prime_idx] == i:
            print (i, "is NOT a prime but WAS in the array")
            return False

