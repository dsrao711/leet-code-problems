class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        if(needle == ""):
          return 0
        if(haystack == ""):
          return -1
        
        return haystack.find(needle)