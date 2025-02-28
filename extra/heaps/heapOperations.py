import heapq

# Inserting an element into the heap : O(logn)
# Add the element at the end and bubble up to restore heap property

heap = []  # Min-Heap
heapq.heappush(heap, 10)
heapq.heappush(heap, 5)
heapq.heappush(heap, 20)
heapq.heappush(heap, 12)
heapq.heappush(heap, 55)
heapq.heappush(heap, 12)
heapq.heappush(heap, 3)
print(heap)  

# Remove/Exstract the minimum element from the list
min_element = heapq.heappop(heap)
print(min_element)

# Peek at the top or the minimum element in the list
print(heap[0])

# Build heap from an array(heapify)
# O(n) It's faster than inserting one-by-one
arr = [40,30,60,20,10]
heapq.heapify(arr)
print(arr)


# Finding the k smallest/largest elements in a heap
k = 6
print(heapq.nsmallest(k, arr))
print(heapq.nlargest(k, arr))

# Implementing max-heap 
max_heap = []
