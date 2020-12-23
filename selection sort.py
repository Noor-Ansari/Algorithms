
def selection_ascending(arr):
    for i in range(0, len(arr)-1):
        mini = i
        for j in range(i+1, len(arr)):
            if arr[j]<arr[mini]:
                mini = j
        if mini != i:
            arr[i],arr[mini] = arr[mini], arr[i]
    return arr

a = [10,3,6,7,3,3,2,1,10]

sorted_arr = selection_ascending(a)

print("Ascending order :-",sorted_arr)

def selection_descending(arr):
    for i in range(0, len(arr)-1):
        maxi = i
        for j in range(i+1, len(arr)):
            if arr[maxi] < arr[j]:
                maxi = j 
        if maxi != i:
            arr[i], arr[maxi] = arr[maxi], arr[i]

    return arr

b = [1,2,3,4,5,6,7,8]

sorted_b = selection_descending(b)

print("Descending order :-", sorted_b)

                                                                                                                                                                                