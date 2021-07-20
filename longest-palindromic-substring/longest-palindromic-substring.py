class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        # init res
        res = ""

        for i in range(len(s)):

            # odd -> helper, update
            tmp = self.helper(i, i, s)
            if len(res) < len(tmp):
                res = tmp

            # even -> helper, update
            tmp = self.helper(i, i + 1, s)
            if len(res) < len(tmp):
                res = tmp

        # return res
        return res

    def helper(self, l, r, s):

        # if inbound and palindrome, move left left and right right
        while (l >= 0 and r < len(s) and s[l] == s[r]):
            l -= 1
            r += 1

        # return 
        return s[l + 1: r]