class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        number = ""
        op_array = []
        for i in digits :
            number += str(i)
            
        int_number = int(number)
        op = str(int_number + 1)
        
        
        for i in range(0 , len(op)):
            op_array.append(op[i])
            
        return op_array
        
            
        