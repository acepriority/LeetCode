"""Given a string s, return the longest 
palindromic substring in s."""

def longestPalindrome(s):
    n = len(s)
    start = 0
    max_length = 0
    dp = [[False] * n for _ in range(n)]

    for i in range(n - 1, -1, -1):
        dp[i][i] = True
        for j in range(i + 1, n):
            if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                dp[i][j] = True
                length = j - i + 1
                if length > max_length:
                    max_length = length
                    start = i

    return s[start : start + max_length]
