"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

from math import sqrt
import sympy

reduced_n = int(sqrt(600851475143))
largest = 0
for num in range(3, reduced_n):
    if (600851475143 % num == 0) and (sympy.isprime(num)):
        largest = num

print(largest)
