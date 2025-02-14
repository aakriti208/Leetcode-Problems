class Solution:
    def merge_sorted_arrays(nums1, m, nums2, n):
        """
        Merge nums2 into nums1 as one sorted array using a two-pointer approach
        nums1 has enough space (length m + n) to hold additional elements from nums2
        
        Args:
            nums1: List[int], first array with extra space at end
            m: int, number of elements in nums1
            nums2: List[int], second array
            n: int, number of elements in nums2
        """
        # Initialize pointers for nums1, nums2, and the merged result
        p1 = m - 1  # pointer for nums1
        p2 = n - 1  # pointer for nums2
        p = m + n - 1  # pointer for the merged array
        
        # While there are elements to compare in both arrays
        while p2 >= 0 and p1 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        
        # If there are remaining elements in nums2, copy them
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1


if __name__ == "__main__":
    nums1 = [1, 2, 2, 0, 0, 0]
    nums2 = [1, 2, 3]
    solution = Solution()
    solution.merge_sorted_arrays()