class Solution:
    def productExceptSelf(self, nums):
        # First, we create a result output array, give each position an intial value of 1 and multiply it with the length of array nums.
        result = [1] * len(nums)
        # Then we will first be doing the prefix. For that, we initialize our prefix as 1 
        prefix = 1
        # and go through each position in out input array.
        for i in range(len(nums)):
            # For each position in our result output array, we're gonna take out prefix and keep it in that position. 
            result[i] = prefix
            # After we've done that, we take our input array value and multiply it with whatever prefix we have.
            prefix *= nums[i]
            # We're gonna be storing prefixes in the resulting output array.

            # After that, we'll do the exact same thing with the postfix, well almost exact.
            # We initialize the postfix as one, we then start at the end of the array, and go all the way to the beginning, like reversing an array
        postfix = 1
            # last array, starting point of the loop, decrements by 1
        for i in range(len(nums)-1, -1, -1): 
                # In this case, we're not gonna just be storing the postfix value, coz that would end up overriding whatever the result has.
                # We're gonna be multiplying it by the value that already is in result. That's multiplying the prefix and postfix together.
                result[i] *= postfix
                # Now, we know we have to continuously keep on upating the postfix. So we multiply it by the value in nums
                postfix *= nums[i]

            # Then we just return the result
        return result
                   
    # Time complexity : O(n)
    # Memory complexity : O(1)
