def ispalindrome(s):
    if s==s[len(s)::-1]:
        return 'Palindrome'
    else:
        return 'Not Palindrome'

s=input('Enter string:')
print(ispalindrome(s))
