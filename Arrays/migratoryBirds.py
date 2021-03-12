def migratoryBirds(arr):
    count = 0
    temp = count
    arr.sort()
    for i in range(len(arr)):
        if arr[1-i] == arr[i]:
            count += 1
            num = arr[i]
        if temp<count:
            temp = count
    return num

arr = [1,2,3,4,5,4,3,2,1,3,4]
print(migratoryBirds(arr))