import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        # We start with an empty heap, which is just an empty list
        min_heap = []
        # We loop through the numbers, and just ask a simple question: Hey, does the heap have less than k elements?
        for num in nums:
            if len(min_heap) < k:
                #if the length of our heap is less than k, we want to push into the heap
                heapq.heappush(min_heap, num)
            else:
                # otherwise, we want to do a push pop operation. We push an element into the heap and pop one element off after that
                heapq.heappushpop(min_heap, num)
            # After we have gone through all the elements, the heap will have the k largest things
            # The top of the heap is gonna be the kth largest thing, which is gonna be the smallest of those
        return min_heap[0]
        # this is actually the top of the heap in min-heap
        
    # T.C: O(nlogk) - we're doing a pushpop operation which is gonna take logk, and doing it n times
    # S.C: O(k) - we're storing it in k space
                
         
    