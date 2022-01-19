class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])
        rows_set = set()
        cols_set = set()
        
        for i in range(0 , r):
            for j in range(0 , c):
                if(matrix[i][j] == 0):
                    rows_set.add(i)
                    cols_set.add(j)
                    
        for i in range(r):
            for j in range(c):
                if(i in rows_set or j in cols_set):
                    matrix[i][j] = 0
                    
        return matrix
                