"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
#Simple brute force algorithm, can be upgraded using dynamic programming or
#other methods.
import sympy

suma = 2
for num in range(3, 2000000):
    if (num % 2 != 0) and (sympy.isprime(num)):
        suma += num

print(suma)
