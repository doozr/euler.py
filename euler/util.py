def is_palindrome(x):
    s = str(x)
    split = int(len(s) / 2 + 1)
    return s[:split] == s[-split:][::-1]

