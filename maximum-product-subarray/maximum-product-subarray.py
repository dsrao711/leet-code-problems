class Solution(object):
    def maxProduct(self, nums):
        
        """
        :type nums: List[int]
        :rtype: int
        """
        
        curr_max = 1
        curr_min = 1
        res = max(nums)
        
        for i in range(0 , len(nums)):
            
            if(nums[i] == 0):
                # Avoid zeroes
                curr_max = 1 
                curr_min = 1
                continue
                
            # Computing temp to store the curr_max * nums[i] , so as to avoid using the                 updated value of curr_max while calculating curr_min
            temp = curr_max * nums[i]
            
            curr_max = max(curr_max * nums[i] , curr_min * nums[i] , nums[i])
            curr_min = min(temp , curr_min * nums[i] , nums[i])
            
            res = max(res , curr_max)
            
        return res
        
    
        
        