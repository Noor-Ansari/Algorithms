
def insertion_assending(arr):
    for i in range(1,len(arr)):
        temp = arr[i]
        j = i - 1
        while j >=0 and arr[j]>temp:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = temp
    return arr

a = [10,9,8,7,6,5,4,3,2,1]

sorted_array = insertion_assending(a)

print("Ascending order :-",sorted_array)

def insertion_desending(arr):
    for i in range(1,len(arr)):
        temp = arr[i]
        j = i - 1
        while j >=0 and arr[j]<temp:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j + 1] = temp
    return arr

b = [1,2,3,4,5,6]

sorted_a  =  insertion_desending(b)

print("Descending order :-",sorted_a)
