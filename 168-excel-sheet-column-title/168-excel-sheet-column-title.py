class Solution(object):
    def convertToTitle(self, n):
        """
        :type columnNumber: int
        :rtype: str
        """
        
        s = ""
        while(n):
            ascii = 65 + ((n-1)%26)
            s = s + str(chr(ascii))
            print(s)
            n =( n - 1 )/ 26
            
        return s[::-1]

                      