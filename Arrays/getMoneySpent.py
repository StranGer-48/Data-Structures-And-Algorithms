def getMoneySpent(keyboards, drives, b):
    num = 0
    for i in range(len(keyboards)):
        for j in range(len(drives)):
            sumVal = keyboards[i] + drives[j]
            if sumVal <= b:
                num = max(num, sumVal)
            else:
                num = -1
    return num


def getMoneySpent_efficient(keyboards, drives, b):
    return max([sum([x,y]) for x in keyboards for y in drives if sum([x,y]) <= b] + [-1] )


keyboards = [3]
drives = [5]
b = 4
print(getMoneySpent_efficient(keyboards, drives, b))
