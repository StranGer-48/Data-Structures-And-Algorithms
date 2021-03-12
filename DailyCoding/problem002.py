# Problem 002 Statement:
# Given an array of integers, return a new array such that each element
# at index i of the new array is the product of all the numbers in the original
# array except the one at i. For example, if our input was [1, 2, 3, 4, 5], the
# expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1],
# the expected output would be [2, 3, 6].
# Follow-up: what if you can't use division?

a = [1, 2, 3, 4, 5]


def function002(a):
    res = [1]*len(a)
    n = len(a)
    for i in range(n):
        res[0], res[i] = res[i], res[0]
        res[1:] = [j * a[i] for j in res[1:]]
    res.sort(reverse=True)
    return res


print(function002(a))
