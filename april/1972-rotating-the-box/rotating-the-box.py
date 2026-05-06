class Solution(object):
    def rotateTheBox(self, box):
        m, n = len(box), len(box[0])
        res = [['.'] * m for _ in range(n)]

        # gravity
        for i in range(m):
            e = n - 1
            for j in range(n - 1, -1, -1):
                if box[i][j] == '*':
                    e = j - 1
                elif box[i][j] == '#':
                    box[i][j] = '.'
                    box[i][e] = '#'
                    e -= 1

        # rotate
        for i in range(m):
            for j in range(n):
                res[j][m - i - 1] = box[i][j]

        return res
        """
        :type boxGrid: List[List[str]]
        :rtype: List[List[str]]
        """
        