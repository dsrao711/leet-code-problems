class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        a_pointer = 0 
        b_pointer = len(s) - 1
        
        while(a_pointer <= b_pointer):
          
          if(s[a_pointer] != s[b_pointer]):
            
            s1 = s[ : a_pointer] + s[a_pointer + 1 : ]
            s2 = s[ : b_pointer] + s[b_pointer + 1 : ]
            
            return (s1 == s1[ : :-1] or s2 == s2[ : :-1])
          
          a_pointer += 1
          b_pointer -= 1
          
        return True
            
            