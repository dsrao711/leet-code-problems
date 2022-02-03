from heapq import heapify , heappush , heappop

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        
        heap = []
        heapify(heap)
        
        for i in range(0 , len(matrix)):
            for j in range(0 , len(matrix[0])):
                heappush(heap , matrix[i][j])
        
        print(heap)
        
                
        while(k-1 != 0):
            heappop(heap)
            k -= 1
            
        kth_smallest = heappop(heap)
        return kth_smallest
        