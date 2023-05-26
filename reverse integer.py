"""Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go 
outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""

def reverse(x):
    lower_limit = -2**31
    upper_limit = 2**31 - 1

    result = 0

    sign = 1
    if x < 0:
        sign = -1
        x *= -1

    while x > 0:
        digit = x % 10
        result = result * 10 + digit
        x //= 10

    result *= sign

    if result < lower_limit or result > upper_limit:
        return 0

    return result
