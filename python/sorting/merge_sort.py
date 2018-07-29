"""Merge sort is a divide and conquor algorithm that breaks an array into subarrays to sort.

Runtime Complexity: 
    Best: O(nlogn)
    Worst: O(nlogn)
    Average: O(nlogn)
Space Complexity: O(n)
"""
import random

def generate_array():
    return [random.randint(0, 100) for x in range(50)]

def merge_sort(array):
    # if one, the array sorted
    if len(array) == 1:
        return array

    # In an even length array, pick middle
    length = len(array) # len() returns non-zero indexed value

    if length % 2 == 0:
        middle = int(length / 2)
    else:
        middle = int((length - .5) / 2)

    # Python slice notation is end exclusive
    # Ex: arr[0:10] takes elements 0 - 9
    # To resolve this issue we simply don't subtract 1 from the length
    left = merge_sort(array[:middle])
    right = merge_sort(array[middle:])

    # build return array
    result = []

    while len(left) != 0 or len(right) != 0:
        # If the right array is empty, keep popping the left
        if len(right) == 0:
            result.append(left.pop(0))
            continue
        
        # If the left array is empty, keeping popping the right
        if len(left) == 0:
            result.append(right.pop(0))
            continue
        
        # Normal case
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    return result


def main():
    unsorted_array = generate_array()
    print(unsorted_array)

    sorted_array = merge_sort(unsorted_array)
    print(sorted_array)


if __name__ == "__main__":
    main()