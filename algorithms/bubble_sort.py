list_1 = [4, 2, 6, 5, 1, 3]


def bubble_sort(my_list):
    # loop over the list n-1 times, where n is the length of the list
    # starting from the end and going backwards
    for i in range(len(my_list)-1, 0, -1):
        # loop over each pair of adjacent elements up to i - 1
        for j in range(i):
            # check if the current element is greater than the next element
            if my_list[j] > my_list[j+1]:
                # if so, swap the elements using a temporary variable
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    # return the sorted list
    return my_list
            

if __name__ == "__main__":
    print(bubble_sort(list_1))
