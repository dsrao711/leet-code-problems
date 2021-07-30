class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        # Get the index of Nums1[i] in nums2[j]  
        # Check if the 
        stack = []
        d = {}
        
        for num in nums2 :
          while stack and stack[-1] < num:
            top = stack.pop()
            d[top] = num
          
          if not stack or stack[-1] > num:
            stack.append(num)
            
        while(stack):
          rest = stack.pop()
          d[rest] = -1
        
        return [d[i] for i in nums1]