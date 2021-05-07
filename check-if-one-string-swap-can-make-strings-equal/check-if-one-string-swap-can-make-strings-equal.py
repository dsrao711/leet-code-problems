class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        count=0
        for j,i in enumerate(s1):
            if i not in s2:
                return False
            if s1[j]!=s2[j]:
                count+=1
        if count==2 or count==0:
            return True
        return False