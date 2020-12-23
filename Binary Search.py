
# Recursive implementation of Binary search
def Binary_search(arr,data,l,r):
    if r>=l:
        mid = (l+r)//2
        if arr[mid] == data:
            return mid
        elif arr[mid] < data:
            return Binary_search(arr,data,mid+1,r)
        else:
            return Binary_search(arr,data,l,mid-1)
    else:
        return -1

array = [10,43,53,63,72,100]
data = 72
result = Binary_search(array,data,0,len(array)-1)

if result != -1:
    print("{} is present at index {}.".format(data,result))
else:
    print("{} is not present in the array.".format(data))


 # Iterative implementation of Binary search 
def binary(a,data,low,high):
    while low<=high:
        mid = (low+high)//2
        if a[mid] == data:
            return mid
        elif a[mid]>data:
            high = (mid-1)
        else:
            low = mid+1

    return -1

arr = [10,12,34,64,99,101,187]

low = 0
high = len(arr)-1
data1 = 101
result1 = binary(arr,data1,low,high)

if result1 !=-1:
    print(f"{data1} is present at position {result1}.")
else:
    print(f"{data1} is not present in the array.")           