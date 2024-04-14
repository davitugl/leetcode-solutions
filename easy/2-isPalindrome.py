def isPalindrome(x):
    if x < 0:
        return False
    reverse = 0
    tmp = x
    while(tmp != 0):
        reverse = reverse * 10 + tmp % 10
        tmp //= 10
    return x == reverse




print(isPalindrome(121))  # True
print(isPalindrome(-121))  # False
print(isPalindrome(10))  # False
