import random

RED, WHITE, BLUE = range(3)

def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]
    smallest = 0
    for i in range(len(A)):
        if A[i] < pivot:
            A[i], A[smallest] = A[smallest], A[i]
            smallest += 1

    largest = len(A) - 1
    for i in reversed(range(len(A))):
        if A[i] < pivot:
            break
        elif A[i] > pivot:
            A[i], A[largest] = A[largest], A[i]
            largest -= 1
    return A

A = [0,1,2,0,2,1,1]

pivot = random.randint(0,2)
pivot_index = A.index(pivot)
partition = dutch_flag_partition(pivot_index, A)
print(partition)