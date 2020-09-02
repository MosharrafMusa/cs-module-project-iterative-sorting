def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:  # check if index matches target and return it
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    low = 0
    mid = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  # get middle of the array
        # if middle index is less than target, reassign low to above middle
        if arr[mid] < target:
            low = mid + 1
        # if middle is greater than target, reasign high to below middle
        elif arr[mid] > target:
            high = mid - 1
        # return middle if target matches
        else:
            return mid
    return -1  # not found
