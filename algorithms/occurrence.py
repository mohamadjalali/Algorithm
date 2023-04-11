def first_occurrence(array, element):
    
    low  = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2

        if low == high:
            break

        elif element > array[mid]:
            low = mid + 1

        else:
            high = mid

    if array[low] == element:
        return low

#a = [2, 2, 2, 4, 4, 4, 4, 6, 6, 6]
#print(first_occurrence(a, 4))

