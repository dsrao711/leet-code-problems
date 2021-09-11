class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def build(S):
        
          stack = []

          for i in S : 
            if i != "#":
              stack.append(i)
            elif stack : 
              stack.pop()
              
          return "".join(stack)
        
        return build(s) == build(t)
            
        
            
            
        