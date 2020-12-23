
def partition(arr,lb,ub):
    pivot = arr[lb]
    start = lb
    end = ub
    while (start<end):
        while arr[start]<=pivot and start<ub:
            start = start+1
        while arr[end]>pivot and end>lb:
            end = end-1
        if (start<end):
            arr[start],arr[end] = arr[end],arr[start]
    arr[lb],arr[end] = arr[end],arr[lb]
    return end


def quick_sort_ascending(arr,lb,ub):
    if lb<ub:
        pivot = partition(arr,lb,ub)
        # Now as we have found the location of pivot element let's 
        # call the the function on both partition recursively

        quick_sort_ascending(arr,lb,pivot-1)
        quick_sort_ascending(arr,pivot+1,ub)
    return arr

a = [3,2,1]

high = len(a)-1
low = 0

print("Before sorting :-",a)
quick_sort_ascending(a,low,high)

print("After sorting :-",a)



def partition1(arr,lb,ub):
    pivot = arr[lb]
    start = lb 
    end = ub
    while start<end:
        while arr[start] >= pivot and start<ub:
            start = start+1
        while arr[end] < pivot and end>lb:
            end = end - 1 
        if start<end:
            arr[start], arr[end] = arr[end], arr[start]
    arr[lb], arr[end] = arr[end], arr[lb]
    return end


def quick_sort_descending(arr,lb,ub):
    if lb<ub:
        pivot = partition1(arr,lb,ub)

        quick_sort_descending(arr,lb,pivot-1)
        quick_sort_descending(arr,pivot+1,ub)
    return arr

b = [-4,-3,-2,-1,0,2,3,4]

high1 = len(b)-1
low1 = 0

print("Before sorting :-",b)

quick_sort_descending(b,low1,high1)

print("After sorting :-",b)

