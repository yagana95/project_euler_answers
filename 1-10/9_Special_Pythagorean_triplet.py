"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a²+ b² = c²

For example, 3² + 4² = 9 + 16 = 25 = 5².

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
#We generate triples using Euclid formula and check if they sum up to 1000.

def pyth_product():
    n, m = 1, 2
    while (m < 1000):
        while (n < m):
            a = m**2 - n**2
            b = 2*m*n
            c = m**2 + n**2
            if (a+b+c == 1000):
                return(a*b*c)
            n += 1
        m += 1
        n = 1

print(pyth_product())
