class Solution(object):
    def majorityElement(self, A):
        """
        :type nums: List[int]
        :rtype: int
        """
        occ = {}
        flag = 0
        N = len(A)
        for i in A :
            if i in occ :
                occ[i] += 1
            else:
                occ[i] = 1
        count = 0
        for key in occ :
            if(occ[key] > N/2):
                flag = 1
                count = key
                break
            
        if (flag == 0):
            count = -1
            
        return count