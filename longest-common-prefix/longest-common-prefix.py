class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        n = len(strs)
        prefix = strs[0]
        
        for word in strs:
          for i in range(0 , len(prefix)):
            if(i >= len(word)):
              prefix = word
              break
              
            elif(prefix[i] != word[i]):
              prefix = prefix[:i]
              break
              
        return prefix
            