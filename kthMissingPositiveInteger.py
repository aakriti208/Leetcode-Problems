class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        low, high = 0, len(arr - 1)
        while high <= low:
            mid = (high + low) // 2
            missing = arr[high] - (high + 1)
            if missing < k:
                low = mid + 1
            else:
                high = mid - 1
        return high + k + 1 or low + k
                
    # return : arr[high] + more
    #          arr[high] + (k - missing) = arr[high] + (k - (arr[high] - high - 1))   = arr[high] + k - arr[high] + high + 1
    #                                                                                 = high + k + 1    = low + k (low = high + 1)
    
    