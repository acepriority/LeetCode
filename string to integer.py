"""Implement the myAtoi(string s) function, which converts a string to a 32-bit signed 
integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. 
Read this character in if it is either. This determines if the final result is negative or positive respectively. 
Assume the result is positive if neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. 
Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains 
in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.
Note:

Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of the string after the digits."""

def myAtoi(s):
    lower_limit = -2**31
    upper_limit = 2**31 - 1

    s = s.strip()

    if not s:
        return 0

    sign = 1
    if s[0] == '-' or s[0] == '+':
        if s[0] == '-':
            sign = -1
        s = s[1:]

    result = 0
    for char in s:
        if not char.isdigit():
            break
        result = result * 10 + int(char)

    result *= sign

    if result < lower_limit:
        return lower_limit
    elif result > upper_limit:
        return upper_limit

    return result
