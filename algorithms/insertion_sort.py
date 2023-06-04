my_list = [1, 4, 5, 3, 2, 0]


def insertion_sort(my_list):
    # iterate over each element of the list starting from the second element
    for i in range(1, len(my_list)):
        # store the current element being sorted in a temporary variable
        temp = my_list[i]
        # iterate over the already sorted part of the list
        j = i - 1
        # while the current element is less than the previous
        # element and the index is still in bounds
        while my_list[j] > temp and j > -1:
            # print(f"{my_list[j]} > {temp}")
            # swap the current element with the previous element
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j -= 1
    # return the sorted list
    return my_list


if __name__ == "__main__":
    print(insertion_sort(my_list)) 
