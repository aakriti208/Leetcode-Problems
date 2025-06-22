class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)


    # find the length of n1 and n2....we also try to make sure that we are working with the shorter array to minimize the search space.
    # left is gonna the number of elements that should be on the left side of the merged array when we partition it. We do +1 to handle odd cases too
    # now out low is gonna be the first element of the left half and high is gonna be the last element of the left half
    # we perform binary search 
    # mid1 is how many elements to take from nums1 for the left partition and mid2 is how many to take from nums2 for left partition
    # total elements in the left partition is : left = mid1 + mid2 
    # arbitrary values for l1,l2,r1,r2
    # r1 is the first element in the right half of nums1 and r2 is the first element in the right half of nums2
    # l1 is the last element in the left half of nums1 and l2 is the last element in the left half of nums2
    # we make a comparision to see if l1 <= r2 and l2 <= r1, that is if we have the correct partition...Also if the total length is odd, we return the maximimum of l1 and l2, which is our median
    # if the length is even, its gonna be the average of the max of the left half and min of the right half
    # If l1 > r2, we took too many elements from nums1, reduce the range.
    # else take more elements from nums1
        n = n1 + n2 
        left = (n1 + n2 + 1) // 2 
        low, high = 0, n1
        while low <= high:
            mid1 = (low + high) // 2
            mid2 = left - mid1
            l1, l2, r1, r2 = float('-inf'), float('-inf'), float('inf'), float('inf')
            if mid1 < n1:
                r1 = nums1[mid1]
            if mid2 < n2:
                r2 = nums2[mid2]
            if mid1 - 1 >= 0:
                l1 = nums1[mid1 - 1]
            if mid2 - 1 >= 0:
                l2 = nums2[mid2 - 1]

            if l1 <= r2 and l2 <= r1:
                if n % 2 == 1:
                    return max(l1, l2)
                else:
                    return ((max(l1, l2)) + (min(r1, r2))) / 2.0

            elif l1 > r2:
                high = mid1 - 1
            else:
                low = mid1 + 1
        return 0  




