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
    

a = [1, 2, 2, 3, 3, 5, 6, 3, 7, 7, 2, 9]

if __name__ == '__main__':
    print(top(a))
