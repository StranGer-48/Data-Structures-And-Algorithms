# Write a program that takes an array of integer and finds the length
# of a longest subarray all of whose entries are equal.

# Example: 
# A = [1,3,2,3,4,3,2,4,3,5]
# Output: 4 (3 is repeated 4 times)

def length_subarray_equal(A):
    longest = 0
    count = 0
    for i in range(len(A)):
        for j in range(i+1,len(A)-i-1):
            if A[i] == A[j]:
                count += 1
        if count > longest:
            longest = count
    return longest

A = [1,3,2,3,4,3,2,4,3,5,3]
print(length_subarray_equal(A))
