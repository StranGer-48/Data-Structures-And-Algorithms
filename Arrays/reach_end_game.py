def can_reach_end(A):
    further_reach_so_far, last_index = 0, len(A)-1
    i = 0
    while i <= further_reach_so_far and further_reach_so_far < last_index:
        further_reach_so_far = max(further_reach_so_far, A[i] + i)
        i += 1
    return further_reach_so_far >= last_index

#A = [3,3,1,0,2,0,1]
A = [3,2,0,0,2,0,1]
print(can_reach_end(A))