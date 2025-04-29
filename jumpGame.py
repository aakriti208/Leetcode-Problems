class Solution:
    def canJump(self, nums):
        n = len(nums) - 1
        goal = n - 1
        for i in range((n-1), -1, -1):
             #Can I jump from index i and land on or beyond the current goal?”
             # If yes, we update the goal to be i.
            if i + nums[i] >= goal:
                goal = i
                
        return True if goal == 0 else False
  #Eventually, if the goal becomes 0, it means we have a full path from index 0 to the end.  
   



