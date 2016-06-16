def is_palindrome(s):
    split = int(len(s) / 2 + 1)
    return s[:split] == s[-split:][::-1]

