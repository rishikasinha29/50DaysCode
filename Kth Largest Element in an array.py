import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Create a min-heap
        min_heap = []

        for num in nums:
            # Push the current number onto the heap
            heapq.heappush(min_heap, num)
            # If the heap size exceeds k, remove the smallest element
            # This ensures the heap always contains the k largest elements encountered so far
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # The root of the min-heap (smallest element in the heap)
        # will be the kth largest element in the original array.
        return min_heap[0]
