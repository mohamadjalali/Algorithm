def merge_sort(my_list):
    # if the list contains only one element, it is already sorted
    if len(my_list) == 1:
        return my_list
    
    # find the midpoint index of the list
    mid_index = len(my_list) // 2
    
    # recursively sort the left and right halves of the list
    left = merge_sort(my_list[:mid_index])
    right = merge_sort(my_list[mid_index:])
    
    # merge the sorted left and right halves of the list
    return merge(left, right)

def merge(list1, list2):
    combined = []
    i = 0
    j = 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1

        else:
            combined.append(list2[j])
            j += 1

    while i < len(list1):
        combined.append(list1[i])
        i += 1

    while j < len(list2):
        combined.append(list2[j])
        j += 1

    return combined


if __name__ == "__main__":

    list1 = [1, 3, 4, 5, 0, 2, 6, 7]
    print(merge_sort(list1))
