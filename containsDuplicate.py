class Solution:
    def containsDuplicate(self, nums):
        # First we create a hash set to store all the values
        hashset = set()
        # We not iterate through each value in the input array 
        for n in nums:
        # We then add each value to the hashset
            # But before doing this, we need to know if there is a duplicate, if there is, out array contains duplicate and we dont have to go through the rest of the array
            # and we can return True
            if n in hashset:
                return True
            # If not, we add the rest of the vallue to the set and iterate through the rest of the values
            hashset.add(n)
        # If we dont find any duplicates, we just return False
        return False
    
    # Space complexity : O(n)
    # Time complexity : O(n)