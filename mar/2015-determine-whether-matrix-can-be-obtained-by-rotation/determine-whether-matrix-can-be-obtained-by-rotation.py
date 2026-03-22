class Solution(object):
    def findRotation(self, mat, target):
        n = len(mat)
        def rotate90(matrix):
            rotate = [[0]*n for _ in range (n)]
            for i in range(n):
                for j in range (n):
                    rotate[j][n-i-1] = matrix [i][j] 
            return rotate
        def issame(a,b):
            for i in range (n):
                for j in range (n):
                    if a[i][j]!= b[i][j]:
                        return False
            return True
        if issame (mat, target):
            return True
        for _ in range(3):
            mat = rotate90(mat)
            if issame(mat, target):
                return True 
        return False

                    
                    
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """
        