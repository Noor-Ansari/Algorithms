# Normal bubblesort for ascending order

def Bubble_sort_ascending(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

array = [9,5,6,1,8,5,3]

sorted_array1 = Bubble_sort_ascending(array)

print("Ascending order :-",sorted_array1)


# optimized bubble sort for descending order

def Bubble_sort_descending(arr):
    for i in range(len(arr)):
        flag = 0
        for j in range(0,len(arr)-1-i):
            if arr[j] < arr[j+1]:
                arr[j+1],arr[j] = arr[j],arr[j+1]
                flag = 1
        if flag == 0:
            break
    return arr

array2 = [1,2,3,4,5,6,6,7,8]

sorted_array2 = Bubble_sort_descending(array2)

print("Descending order :-",sorted_array2)

'''
 Time complexities
best --> O(n)
average --> O(n2)
worst --> O(n2) 
'''