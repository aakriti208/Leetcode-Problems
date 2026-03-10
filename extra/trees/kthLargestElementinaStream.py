import heapq

class KthLargest(object):

    def __init__(self, k, nums):
        # first, lets store nums as a min_heap and remember k
        # we then heapify that min_heap....and until the length of the > k: we pop the smallest value 
        self.min_heap, self.k = nums, k
        heapq.heapify(self.min_heap)
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)

        # For adding, we push the value to the heap....then pop the smallest one until they dont undersized

    def add(self, val):
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]