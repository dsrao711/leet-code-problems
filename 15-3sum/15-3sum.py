class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        n = len(nums)
        op = set()
        # Impossible in this case
        if(n < 3):
            return op
        nums.sort()
        
        for i in range(n - 2):
            
            if(i != 0 and nums[i] == nums[i - 1]):
                continue 
                
            target = - nums[i]  
            lo = i + 1
            hi = n - 1
            
            while(lo < hi):
                pair = nums[lo] + nums[hi]
                if(pair == target) :
                    op.add((nums[lo] , nums[hi] , nums[i]))
                if(pair < target):
                    lo += 1
                else:
                    hi -= 1
                    
        return list(op)[::-1]
                    
                    
            
                
            