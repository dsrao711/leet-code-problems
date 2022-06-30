class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)  # create a min-heap whose size is k 
        for num in nums[k:]:
            if num > heap[0]:
               heapq.heapreplace(heap, num)
            # or use:
            # heapq.heappushpop(heap, num)
        return heap[0]