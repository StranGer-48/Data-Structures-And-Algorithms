def  isPalindrome(x):
    temp = x
    rev = 0
    istrue = 0
    if x<9:
        istrue = 0
        return bool(istrue)
    while(x>0):
        dig = x % 10
        rev = rev*10+dig
        x = x//10
    if  (temp == rev):
        istrue = 1
    else:
        istrue = 0
    return bool(istrue)
print(isPalindrome(-121))