def merge(arr, left, mid, right):
    # if len(arr) <= 1:
    #     return arr
    
    n1 = mid - left + 1
    n2 = right - mid 
    
    # create temporary subarrays
    L = [0] * n1
    R = [0] * n2
    
    # copy data to temporary subarrays L and R
    # elements from left to mid and mid+1 to right
    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]
        
    # initial index of first and second subarray
    i = 0
    j = 0
    k = left      # initial index of merged subarray
    
    
    # compare elements from both subarrays and place smaller one to original array
    
    while i < n1 and j < n2:
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
        
    # copy remaining elements of L[] and R[] if there are any
    
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
            
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
            
    
    
# Main recursive function that recursively sorts left and right half and merges the two sorted halves using merge function
def mergeSort(arr, left, right):
    if left < right:
        mid = (left+right) // 2
        mergeSort(arr, left, mid)
        mergeSort(arr, mid+1, right)
        merge(arr, left, mid, right)
        
        
          
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", arr)

    mergeSort(arr, 0, len(arr) - 1)

    print("\nSorted array is", arr)

TC : O(nlogn)
SC : O(n)



