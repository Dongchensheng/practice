def selection_sort(arr):
    for i in range(len(arr)):
        minimum = i

        for j in range(i + 1, len(arr)):
            #select the smallest value
            if arr[j] < arr[minimum]:
                minimum = j

        # Place it at the front of the sorted end of the array

        arr[minium], arr[i] = arr[i], arr[minimum]


    return arr
