"""
    This algorithm receives a sorted list and a target (number) and then 
    returns the indexes of two numbers whose sum is equal to the target.
"""

def two_sum(numbers, target):
    p1 = 0
    p2 = len(numbers) - 1

    while p1 < p2:
        s = numbers[p1] + numbers[p2]
        if s == target:
            return [p1, p2]

        elif s > target:
            p2 -= 1
        
        else:
            p1 += 1


print(two_sum([2, 7, 11, 15], 18))
