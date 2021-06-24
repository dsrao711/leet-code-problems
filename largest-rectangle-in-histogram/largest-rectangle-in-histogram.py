class Solution:
    
    def largestRectangleArea(self, h: List[int]) -> int:
        
        n = len(h)
        left_index = [0]*n
        right_index = [0]*n
        stack = []
        
        # Left index
        
        for i in range(0 , n):
          if(len(stack) == 0):
            left_index[i] = 0
          else:
            while(len(stack) != 0 and h[stack[-1]] >= h[i]):
              stack.pop()
            if(len(stack) == 0):
              left_index[i] = 0
            else:
              left_index[i] = stack[-1] + 1
          stack.append(i)
          
        while(len(stack)!= 0):
          stack.pop()
        
        # Right index
        
        for i in range(n-1 , -1 , -1):
          if(len(stack) == 0):
            right_index[i] = n - 1
          else:
            while(len(stack) != 0 and h[stack[-1]] >= h[i]):
              stack.pop()
            if(len(stack) == 0):
              right_index[i] = n - 1
            else:
              right_index[i] = stack[-1]- 1
          stack.append(i)
          
        max_area = 0
        
        for i in range(0 , n):
          
          max_area = max(max_area , (right_index[i] - left_index[i] + 1)*h[i])
          
        return max_area
        
        # Calc area using left , right and height indexs
        
            