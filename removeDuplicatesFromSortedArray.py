class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # First we initialize the left pointer, it can start from the index 1 as the first element is always gonna be unique
        l = 1
        # for the right pointer, we can iterate through each value in the input array
        for r in range(1, len(nums)):
            # the only thing we need to check is if it is a new value or a value we have already seen
            # we can determine that by comparing the value that came before that
            if nums[r] != nums[r-1]:
                # we can take this new unique value at index r and place it at index l
                nums[l] = nums[r]
                # everytime we do this operation, we increment the left pointer
                l += 1
            # r += 1 is not needed coz the for loop is gonna take care of it
        # Out left index has been handling how many unique values we have in our array so we can just return that
        return l
    
    # T.C : O(n)
    # S.C : O(1)