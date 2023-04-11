
def last_occurrence(array, element):
    low  = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        
        if ( array[mid] == element and mid == len(array) - 1 ) or \
                ( array[mid] == element and array[mid+1] > element ):
            return mid
        
        elif (array[mid] <= element):
            low = mid + 1
        
        else:
            high = mid - 1



# a = [2, 2, 2, 3, 3, 4, 4, 4, 5, 5] 
# print(last_occurrence(a, 4))

