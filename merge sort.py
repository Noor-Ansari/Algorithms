
def merge_sort_ascending(arr):
    if len(arr)>1:
        m = len(arr)//2
        L = arr[:m]
        R = arr[m:]
        merge_sort_ascending(L)
        merge_sort_ascending(R)

        i = j = k = 0

        while i <len(L) and j<len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i = i+1
            else:
                arr[k] = R[j]
                j = j+1
            k = k+1
        if i >= len(L):
            while j < len(R):
                arr[k] = R[j]
                k =k+1
                j =j+1
        else:
            while i < len(L):
                arr[k] = L[i]
                k = k+1
                i = i+1
    return arr


x = [10,45,2,5,3,1,100,4]

result = merge_sort_ascending(x)

print("Ascending order :-", result)


def merge_sort_descending(arr):
    if len(arr) > 1:
        m = len(arr)//2
        L = arr[:m]
        R = arr[m:]
        merge_sort_descending(L)
        merge_sort_descending(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = R[j]
                j = j+1
            else:
                arr[k] = L[i]
                i = i+1
            k = k+1
        if j >= len(R):
            while i < len(L):
                arr[k] = L[i]
                k = k+1
                i = i+1
        else:
            while j < len(R):
                arr[k] = R[j]
                k = k+1
                j = j+1
    return arr

y = [1,2,3,4,5,6,7,8]

sorted_descending = merge_sort_descending(y)

print("Descending order :-",sorted_descending)