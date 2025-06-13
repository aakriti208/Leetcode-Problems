class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
            # in this case we have to check the edge case, when 3 elements could be the same
            # since the condition of checking in left or right sorted portion does not work
            if nums[l] == nums[mid] == nums[r]:
                l += 1
                r -= 1
                continue
            #left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return False

        
    # avg t.c : O(log n)
    # worst t.c : O(n/2) - since we have to shrink the input data 