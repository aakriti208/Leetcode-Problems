def mergeSort(arr):
    n = len(arr)
    
    if n <= 1:
        return arr
    
    mid = len(arr) // 2
    L = arr[:mid]
    R = arr[mid:]
    
    L = mergeSort(L)
    R = mergeSort(R)
    l, r = 0, 0
    l_length = len(L)
    r_length = len(R)
    
    sortedArr = [0] * n
    i = 0
    
    while l < l_length and r < r_length:
        if L[l] < R[r]:
            sortedArr = L[l]
            l += 1
        else:
            sortedArr[i] = R[r]
            r += 1
        i += 1
        
    # while l < l_length:
    #     sortedArr[i] = L[l]
    #     l += 1
    #     i += 1
            
    # while r < r_length:
    #     sortedArr[i] = R[r]
    #     r += 1
    #     i += 1
            
    return sortedArr
    
    
arr = [12, 11, 13, 5, 6, 7]

mergeSort(arr)

print("\nSorted array is", arr)




# def merge(arr, left, mid, right):
#     n1 = mid - left + 1
#     n2 = right - mid

#     # Create temp arrays
#     L = [0] * n1
#     R = [0] * n2

#     # Copy data to temp arrays L[] and R[]
#     for i in range(n1):
#         L[i] = arr[left + i]
#     for j in range(n2):
#         R[j] = arr[mid + 1 + j]

#     i = 0  # Initial index of first subarray
#     j = 0  # Initial index of second subarray
#     k = left  # Initial index of merged subarray

#     # Merge the temp arrays back
#     # into arr[left..right]
#     while i < n1 and j < n2:
#         if L[i] <= R[j]:
#             arr[k] = L[i]
#             i += 1
#         else:
#             arr[k] = R[j]
#             j += 1
#         k += 1

#     # Copy the remaining elements of L[],
#     # if there are any
#     while i < n1:
#         arr[k] = L[i]
#         i += 1
#         k += 1

#     # Copy the remaining elements of R[], 
#     # if there are any
#     while j < n2:
#         arr[k] = R[j]
#         j += 1
#         k += 1

# def merge_sort(arr, left, right):
#     if left < right:
#         mid = (left + right) // 2

#         merge_sort(arr, left, mid)
#         merge_sort(arr, mid + 1, right)
#         merge(arr, left, mid, right)

# # Driver code
# if __name__ == "__main__":
#     arr = [12, 11, 13, 5, 6, 7]
#     print("Given array is",arr)

#     merge_sort(arr, 0, len(arr) - 1)

#     print("\nSorted array is", arr)
