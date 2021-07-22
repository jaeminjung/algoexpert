
def binarySearch(array, target):

    left = 0
    right = len(array) - 1
    # before_mid = (left + right) // 2
    while left <= right:
        
        mid = (left + right) // 2
        # if mid == before_mid:
        #     mid += 1

        if array[mid] == target:
            return mid
        if array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        # before_mid = mid
    return -1

print(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 60))