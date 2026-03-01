class Solution(object):
    def twoSum(self, nums, target):
        # To solve this problem, we need to create an empty hashmap, where we store all the elements in a way that no two elements will appear in the hashmap twice.

        # Create an empty hashmap containing the values that have been seen before
        prevMap = {}

        # Go through each element in the list
        for i, n in enumerate(nums):
            # Find the difference 
            diff = target - n
            # If the difference is already in hashmap, the solution has been found
            # Return the index of the hashmap and the current index
            if diff in prevMap:
                return [prevMap[diff], i]
            
            # Else go ahead and add the current value in the hash map
            prevMap[n] = i


        # Time complexity : O(n)
        # Space complexity : O(n)
        
        