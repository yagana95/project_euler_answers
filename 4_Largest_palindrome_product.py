"""
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
#Since we want the largest we start from the end.

def ispalindrome(arg):
    answer = 0
    compare = arg
    while (arg>0):
        remainder = arg % 10
        answer = (answer * 10) + remainder
        arg = arg//10
    if (answer == compare):
        return True
    return False

answer = 0
multi = 0

for num in range(900, 1000):
    for num2 in range(900,1000):
        multi = num*num2
        if (multi>answer) and (ispalindrome(multi)):
            answer = multi

print(answer)
