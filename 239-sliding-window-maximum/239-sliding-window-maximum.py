from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        
        n = len(nums)
        deq = deque()
        op = []
        j = 0 

        # Deque
        for i in range(0 , k):
            j = i 
            while(deq and nums[deq[-1]] <= nums[i]):
                deq.pop()
            deq.append(i)
            

        for i in range(j , n):
            while(deq and deq[0] <= i - k):
                deq.popleft()
            
            while(deq and nums[deq[-1]] <= nums[i]):
                deq.pop()
            
            deq.append(i)
            op.append(nums[deq[0]])
            
        return op
        