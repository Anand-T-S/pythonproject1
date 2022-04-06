def palindrome(s):
    if s==s[::-1]:
        return "palindrome"
    else:
        return "not palindrome"
print(palindrome("abcda"))