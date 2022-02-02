class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        stack=[]
        rst= [-1]*len(nums)
        
        for i in range(len(nums)-2,-1,-1):
            while stack and nums[i]>=stack[-1]:
                stack.pop()    
            stack.append(nums[i]) 
        
        for i in range(len(nums)-1,-1,-1):
            while stack and nums[i]>=stack[-1]:
                stack.pop()
            if stack:
                rst[i]=stack[-1]
            stack.append(nums[i])
        
        return rst