def count(a):
    size = len(a)
    maxi = max(a)+1
    count = [0]*maxi
    output = [0]*size

    for i in range(0,size):
        count[a[i]] +=1

    for i in range(1,maxi):
        count[i] += count[i-1] 

    i = size-1

    while i >=0:
        output[count[a[i]]-1] = a[i]
        count[a[i]] -=1
        i -=1
    for i in range(0,size):
        a[i] = output[i]

    return a

arr = [5,17,3,2,9,0,12,41,17]

print("Unsorted array :-",arr)
sorted_arr = count(arr)
print("Sorted array :-",sorted_arr)


