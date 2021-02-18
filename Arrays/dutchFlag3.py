import random

RED, WHITE, BLUE = range(3)

def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]
    smaller, equal, larger = 0,0,len(A)

    while equal < larger:
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal = smaller + 1, equal + 1, equal
        elif A[equal] == pivot:
            equal += 1
        else:
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]
    
    return A

A = [0,1,2,0,2,1,1]

pivot = random.randint(0,2)
pivot_index = A.index(pivot)
partition = dutch_flag_partition(pivot_index, A)
print(partition)