# Instructions: 
# Quick Sort

"""
The function quick_sort_helper takes three arguments: my_list, which is the list to be sorted, left, which is the leftmost index of the sublist
to be sorted, and right, which is the rightmost index of the sublist to be sorted.

The first line of the function checks if left is less than right. If it is not, that means there is only one element or no 
element in the sublist to be sorted, and the function simply returns the list.

If there are two or more elements in the sublist, the function selects a pivot element by calling the function pivot with 
the arguments my_list, left, and right. The pivot function chooses a pivot element and partitions the list into two 
sublists: one sublist contains all elements less than the pivot, and the other contains all elements greater than or equal to the pivot.

The function then recursively calls itself twice with the updated left and right indices to sort the two sublists. Specifically, the function calls 
itself with left and pivot_index-1 to sort the left sublist, and with pivot_index+1 and right to sort the right sublist.

Finally, when the recursive calls have finished and all sublists are sorted, the function returns the sorted list.

It's worth noting that the implementation assumes that the pivot function is already defined.
"""


def swap(my_list, index1, index2):
    # a list and two indexes are received as parameters, and then the two indexes in the list are moved together.
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]


def pivot(my_list, pivot_index, end_index):
    # Initialize the swap index to the pivot index
    swap_index = pivot_index
    
    # Iterate over the list from the pivot index + 1 to the end index
    for i in range(pivot_index+1, end_index+1):
        # If the current element is less than the pivot element
        if my_list[i] < my_list[pivot_index]:
            # Increment the swap index
            swap_index += 1
            # swap the current element with the element at the swap index
            swap(my_list, swap_index, i)
    
    # swap the pivot element with the element at hte swap index
    swap(my_list, pivot_index, swap_index)
    # return the index of the pivot element after swapping
    return swap_index



def quick_sort_helper(my_list, left, right):
    # check if there is more than one element in the sublist to be sorted
    if left < right:
        # choose a pivot element and partition the list into two sublists
        pivot_index = pivot(my_list, left, right)
        
        # recursively sort the left sublist (elements less than pivot)
        quick_sort_helper(my_list, left, pivot_index-1)
        
        # recursively sort the right sublist (elements greater than or equal to pivot)
        quick_sort_helper(my_list, pivot_index+1, right)
    
    # when there is only one element or no elements left to be sorted, return the sorted list
    return my_list



def quick_sort(my_list):
    return quick_sort_helper(my_list, 0, len(my_list)-1)


if __name__ == "__main__":

    my_list = [4,6,1,7,3,2,5]

    print(quick_sort(my_list))


    """
        EXPECTED OUTPUT:
        ----------------
        [1, 2, 3, 4, 5, 6, 7]
        
    """

