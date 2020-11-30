"""
The sum of the squares of the first ten natural numbers is,
1²+2²+...+10²=385
The square of the sum of the first ten natural numbers is,
(1+2+...+10)²=55²=3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
3025-385=2640
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
sum_sq = 0
sq_sum = 0
for num in range(1,101):
    sum_sq += num**2
    sq_sum += num
sq_sum = sq_sum**2

print(sq_sum-sum_sq)
