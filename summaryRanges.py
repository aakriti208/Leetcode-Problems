class Solution():
    def summaryRanges(self, nums):
        output = []
        if not nums:
            return output
        start = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                if start == nums[i - 1]:
                    output.append(str(start))
                else:
                    output.append(str(start) + "->" + str(nums[i - 1]))
                start = nums[i]
        
        if start == nums[-1]:
            output.append(str(nums[-1]))
        else:
            output.append(str(start) + "->" + str(nums[-1]))
        return output