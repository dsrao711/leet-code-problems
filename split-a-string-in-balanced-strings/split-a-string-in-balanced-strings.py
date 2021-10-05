class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        count_r = 0
        count_l = 0
        balanced_strings = 0
        for i in s :
            if i == "R":
                count_r += 1
            if i == "L":
                count_l += 1
            if(count_r == count_l):
                balanced_strings += 1
                count_r = 0
                count_l = 0         
        return balanced_strings