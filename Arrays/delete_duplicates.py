def delete_duplicates(A):
    if not A:
        return 0
    
    write_index = 1
    for i in range(1,len(A)):
        if A[write_index - 1] != A[i]:
            A[write_index] = A[i]
            write_index += 1
    return write_index, A[:write_index]

A = [2,3,5,5,7,11,11,11,13]
print(delete_duplicates(A))