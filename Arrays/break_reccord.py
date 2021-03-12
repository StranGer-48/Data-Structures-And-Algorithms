scores =  [10,5,20,20,4,5,2,25,1]
#scores = [3,4,21,36,10,28,35,5,24,42]

def breakingRecords(scores):
    min_val = scores[0]
    min_count = 0
    max_val = scores[0]
    max_count = 0
    for i in range(1,len(scores)):
        if max_val <scores[i]:
            max_val = scores[i]
            max_count += 1
        elif min_val > scores[i]:
            min_val = scores[i]
            min_count += 1
    return max_count, min_count
print(breakingRecords(scores))