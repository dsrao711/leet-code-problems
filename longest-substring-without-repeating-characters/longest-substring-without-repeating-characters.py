class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Sliding window method 
        
        left_pointer = 0
        res = 0 
        char_set = set()
        
        for right_pointer in range(len(s)):
            
            while(s[right_pointer] in char_set):
                char_set.remove(s[left_pointer])
                left_pointer += 1 
                
            char_set.add(s[right_pointer]) 
            res = max(res , right_pointer - left_pointer + 1)
    
        return res