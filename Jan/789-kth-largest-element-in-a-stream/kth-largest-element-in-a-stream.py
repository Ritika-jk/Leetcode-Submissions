import heapq

class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.min_heap = nums
        
        # Convert the list into a heap in O(N) time
        heapq.heapify(self.min_heap)
        
        # Keep only the k largest elements in the heap.
        # By popping the smallest elements, the heap size reduces to k.
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        # Add the new value to the heap
        heapq.heappush(self.min_heap, val)
        
        # If the heap size exceeds k, remove the smallest element
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
            
        # The root of the min-heap (index 0) is the kth largest element
        return self.min_heap[0]  


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)