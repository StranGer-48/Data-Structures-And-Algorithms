def ksum(s, t, k):

    s.sort()
    count = 0
    sumVal = 0

    if len(s) == 0:
        return 0
    
    for i in range(len(s)):
        if i == 0 or s[i-1] != s[i]:
            l, r = 0, len(s) - 1
            while l < r:
                for j in range(k):
                    sumVal = s[l] + s[r]
                if sumVal < t or (l < 0 and s[l] == s[l-1]):
                    l += 1
                elif sumVal > t or (r < len(s)-1 and s[r] == s[r + 1]):
                    r -= 1
                else:
                    l += 1
                    r -= 1
                    sumVal = 0
            count += 1
    return count

nums = [2,2,1,3,2]
print(ksum(nums, 4,2))
