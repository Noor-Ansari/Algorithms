def radixsort(a):
    maxi = max(a)
    n = len(a)
    pos=1
    while maxi//pos>0:
        sorted_arr = countsort(a,pos,n)
        pos = pos*10
    return sorted_arr
    
def countsort(a,pos,n):
    count = [0]*10
    output = [0]*n
    for i in range(0,n):
        count[(a[i]//pos)%10] += 1
    
    for i in range(1,len(count)):
        count[i] += count[i-1]
    j=n-1
    while j>=0:
        output[count[(a[j]//pos)%10]-1] = a[j]
        count[(a[j]//pos)%10] -=1 
        j -= 1

    for i in range(0,n):
        a[i] = output[i]
    return a  


arr = [43,8,53,90,88,23]

print("Unsorted array :-",arr)
sorted_array = radixsort(arr)
print("Sorted array :-",sorted_array)