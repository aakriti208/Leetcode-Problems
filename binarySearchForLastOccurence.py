def last_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    result = -1  # if not found

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            result = mid  # record index
            left = mid + 1  # keep searching to the right
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result
