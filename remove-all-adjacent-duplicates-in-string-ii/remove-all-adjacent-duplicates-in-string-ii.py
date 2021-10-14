class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
        # Eg : stack = [['d' , 1] , ['e' , 3]]
        
        stack = []
        
        for c in s : 
            # Check if stack is not empty and top element is equal to the char
            if stack and stack[-1][0] == c :
                # If yes , increase the counter
                stack[-1][1] += 1
                # If the count of this char is equal to k , remove it 
                if(stack[-1][1] >= k):
                    stack.pop()
            # Else , add the first occurence
            else:
                stack.append([c , 1])
                
        result = ''
        
        # Return the output as string with the remaining charachters
        for arr in stack:
            result += (arr[0]*arr[1])
            
        
        return result 