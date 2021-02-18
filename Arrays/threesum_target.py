A = [0, 2, 1, -3]
target = 1


def three_sum(A, target):
    if not A:
        return None
    if len(A) < 3:
        return 0

    A.sort()
    minimum = float('inf')

    for i in range(len(A) - 2):
        l = i + 1
        r = len(A) - 1
        while l < r:
            threesum = A[i] + A[l] + A[r]
            dist = target - threesum
            if abs(dist) < minimum:
                minimum = abs(dist)
                sumValue = threesum
            if threesum > target:
                r -= 1
            else:
                l += 1
    return sumValue


print(three_sum(A, target))
