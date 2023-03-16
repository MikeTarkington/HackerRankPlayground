import math

# https://www.hackerrank.com/challenges/extra-long-factorials/problem?isFullScreen=true

# n * n-1 * n-2 ...

def extraLongFactorials(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact

print(extraLongFactorials(30))

# built in function makes it easy but
# the above solves as problem was probably intended
print(math.factorial(30))
