class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # we initially keep track of two pointers
        i = 0
        n = len(nums)
        
        # We go through all the elements in nums to see if we can find the value
        while i < n:
            # in the ith index if we see if there is any number which is equal to the value, we replace it by the number at (n-1)th index
            if nums[i] == val:
                nums[i] = nums[n - 1]
                # We dont yet increment the value of i, because what if the element at n-1 th position was also equal to val?
                # Just decrement the last pointer
                n -= 1
            else:
                # if we have values other than val, we increment the ith pointer too
                i += 1
        # since n is the amount of numbers we've kept
        
        return n
    # T.C : O(n)
    # S.C : O(1)