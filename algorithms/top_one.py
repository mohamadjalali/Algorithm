"""
This algorithm receives an array and returns most_frequent_value
Also, sometimes it is possible to have multiple 'most_frequent_value's,
so this function returns a list. This result can be used to find a 
representative value in an array.
This algorithm gets an array, makes a dictionary of it,
finds the most frequent count, and makes the result list.
For example: top([1, 1, 2, 2, 3, 4], 2) will return ([1, 2], 2)
In other words the output of a tuple contains the value or values in
the array and the highest count of that value.

(TL:DR) Get mathematical Mode
Complexity: O(n)
"""


def top(arr):
    values = {}
    result = []
    f_val  = 0

    # To find count of each element
    for i in arr:
        if i in values:
            values[i] += 1
        else:
            values[i] = 1
    
    # Find greater value in dictionary
    f_val = max(values.values())

    for i in values.keys():
        if values[i] == f_val:
            result.append(i)
        else:
            continue

    return result, f_val
    


if __name__ == '__main__':
    a = [1, 2, 2, 3, 3, 5, 6, 3, 7, 7, 2, 9]
    b = [1, 1, 2, 2, 3, 4]
    print(top(a))
    print(top(b))

