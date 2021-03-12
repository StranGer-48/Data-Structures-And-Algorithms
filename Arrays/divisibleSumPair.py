def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(n):
        for j in range(n):
            if i < j and (ar[i]+ar[j]) % k == 0:
                count += 1
    return count

def divisibleSumPair_modified(n,k,ar):
    count = 0
    l = 0
    r = n-1
    while l < r:
        sumVal = ar[l] + ar[r]
        if sumVal % k == 0:
            count += 1
        if sumVal /k > 0:
            l += 1
        elif sumVal/k < 0:
            r -= 1
    return count
arr = [1, 3, 2, 6, 1, 2]

print(divisibleSumPairs(6, 3, arr))
print(divisibleSumPair_modified(6, 3, arr))