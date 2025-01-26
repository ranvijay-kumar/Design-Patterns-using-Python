from math import sqrt, ceil

def gen_primes(number):
    """A generator function to generate prime numbers, starting from number"""
    while True:   # No upperbound!
        if is_prime(number):
            yield number
        number += 1


def is_prime(number:int) -> int:
    if number <= 1:
        return False

    factor = 2
    while (factor <= ceil(sqrt(number))):
        if number % factor == 0: return False
        factor += 1

    return True


if __name__ == '__main__':
    g = gen_primes(8)     # From 8
    for i in range(100000):  # Generate 100 prime numbers
        print(next(g))