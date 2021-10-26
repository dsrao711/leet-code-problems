class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        ans_index = 0
        counter = 0
        n = len(nums)
        
        for i in range(0 , n):
            if(nums[i] == nums[ans_index]):
                counter += 1
            else:
                counter -= 1
            
            if(counter == 0):
                ans_index = i
                counter = 1
         
        freq = 0
        res = -1
        
        for i in range(0 , n):
            if(nums[i] == nums[ans_index]):
                freq += 1 
                
        if(freq >= (n/2)):
            res = nums[ans_index]
            
        return res
            