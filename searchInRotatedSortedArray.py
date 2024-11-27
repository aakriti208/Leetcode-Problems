class Solution:
    def search(self, nums, target):
        # Initialize the pointers first
        l, r = 0, len(nums) - 1
        # For searching we do binary search and our condition is 
        while l <= r:
            # We find the mid value for doing binary search on this
            mid = (l + r) // 2
            # It is possible for the target value to be equal to the mid value. In that case, return the mid index
            if target == nums[mid]:
                return mid
            
            # If that is not the case, we need to check which portion of the array we are in
            # Are we in the left sorted portion? We check that by checking if the middle value is greater than or equal to left value
            if nums[l] <= nums[mid]:
                # Now check if the target is greater than mid value or less than leftmost value
                if target > nums[mid] or target < nums[l]:
                    # Then we need to start searching in the rightmost postion, so update the left pointer
                    l = mid + 1
                else:
                    # Update the right pointer
                    r = mid - 1
                
            else:
                # Are we in the right sorted portion? We do a similar approach as above
                # We check if the target is less than mid value or greater than rightmost value, in that case we need to go to the leftside
                if target < nums[mid] or target > nums[r]:
                    # Update the right pointer
                    r = mid - 1
                else:
                    l = mid + 1
                # If we find result we return it in the steps above, else return - 1
            return -1



