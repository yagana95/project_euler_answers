"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

#Approach by brute force since we don't know too much about the distribution
#of primes.

import sympy as spy
#n_prime is the first prime, which is 2
n_prime = 1
iterator = 2
while (n_prime < 10001):
    iterator += 1
#We discard numbers that are divisible by 2 and 5 for a little speedup (around 4ms)
    if (iterator % 2 != 0) and (iterator % 5 != 0) and (spy.isprime(iterator)):
        n_prime += 1
print("Prime number:",iterator," Position:",n_prime)
