# Problem 001 Statement:
# Given a list of numbers and a number k, return
# whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return
# true since 10 + 7 is 17.

def function(a, k):
    a.sort()
    l = 0
    r = len(a) - 1
    while l < r:
        if (a[l] + a[r] > k):
            r -= 1
        elif a[l] + a[r] < k:
            l += 1
        else:
            return 1
    return 0


a = [10, 15, 3, 7]
print(function(a, 17))
