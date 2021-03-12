def birthday(s, d, m):
    return sum([1 for i in range(len(s)-m+1) if sum(s[i:i+m])==d])


nums = [2,2,1,3,2]
print(birthday(nums, 4,2))