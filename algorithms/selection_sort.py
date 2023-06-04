my_list = [4, 1, 6, 5, 2, 3]


def selection_sort(my_list):
    # loop over the list n-1 times, where n is the length of the list
    for i in range(len(my_list)-1):
        # set the current index as the index of the smallest element
        min_index = i
        # loop over each element in the unsorted part of the list
        for j in range(i+1, len(my_list)):
            # if the current element is smaller than the 
            # current minimum, update the minumum index
            if my_list[min_index] > my_list[j]:
                min_index = j
        # if the index of the minumum element is not i, swap the element 
        # at indices i and min_index
        if i != min_index:
            my_list[i], my_list[min_index] = my_list[min_index], my_list[i]
    # return the sorted list 
    return my_list


if __name__ == "__main__":
    print(selection_sort(my_list))

