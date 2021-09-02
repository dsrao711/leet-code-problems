from collections import Counter

class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        S = collections.Counter(s)
    
        count= 0

        unique = set()

        for char, freq in S.items():
            while freq >0 and freq in unique:
                freq-=1
                count+=1

            unique.add(freq)

        return count