def containsNearbyDuplicate(self, nums, k):
    window = set()
    l = 0
    for r in range(len(nums)):
        if r - l > k:
            window.remove(nums[l])
            l += 1
        if nums[r] in window:
            return True
        window.add(nums[r])
    return False
        
        
# Here k is the maximum allowed distance between duplicate elements
# Set is used to store the elements within the current window. They are ideal as they provide O(1 lookup time
# l is the left boundary of the sliding window and r is the right boundary
# the condition checks if the current window size exceeds the allowed distance. If it does, we need to shrink the window from the left side
# check is the current element is already in the window set
# If it is we've found a duplicate within the window
# if no duplicate is found, add the current element to the window
# if loop completes without finding any duplicate, return False

# TC : O(n), where n is the length of nums. We iterate through each element once. O(1) is the lookup time
# SC : O(m), since window set stores at most m+1 elements

