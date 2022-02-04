from heapq import heapify , heappush , heappop

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        
        n = len(matrix)
        l = matrix[0][0]
        h = matrix[n-1][n-1]
        
        while(l < h):
            m = (l + h) / 2
            count = 0 
            for i in range(0 , n):
                count += bisect_right(matrix[i], m)
            if(count < k):
                l = m + 1
            else:
                h = m
                
        return l
        
        