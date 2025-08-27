class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # normalize negative values
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
                
        # Mark presence of numbers
        # Mark the position corresponding to value
        # If position has value 0, mark a sentinel number which is the number out of bound
        # if number is already negative, do nothing 
        
        for i in range(len(nums)):
            val = abs(nums[i])
            if 1 <= val <= len(nums):
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
                elif nums[val - 1] == 0:
                    nums[val - 1] = -1 * (len(nums) + 1)      

        # find the first missing positive 
        # number 'i' is the missing number
        
        for i in range(1, len(nums) + 1):
            if nums[i - 1] >= 0:
                return i
            
        # If all [1...n] are present, the number is n + 1           
        return len(nums) + 1
              
              
