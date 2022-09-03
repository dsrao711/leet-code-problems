class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []
        
        for i in s : 
            if(len(stack) == 0):
                stack.append(i)
            else:
                if(i == ")" ):
                    if(stack[-1] == "("):
                        stack.pop()
                    else:
                        stack.append(i)
                if(i == "}" ):
                    if(stack[-1] == "{"):
                        stack.pop()
                    else:
                        stack.append(i)
                if(i == "]" ):
                    if(stack[-1] == "["):
                        stack.pop()
                    else:
                        stack.append(i)
                if(i == "(" or i == "{" or i == "["):
                    stack.append(i)
                    
        if(len(stack)):
            return False
        
        return True
                        
                    