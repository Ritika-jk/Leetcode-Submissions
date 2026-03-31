class Solution(object):
    def generateString(self, str1, str2):
        n, m = len(str1), len(str2)
        res = ['a'] * (m + n - 1)
        fixed = [False] * (m + n - 1)
        for i, c in enumerate(str1):
            if c == 'T':
                for j in range(m):
                    if not fixed[i + j]: res[i + j] = str2[j]
                    elif res[i + j] != str2[j]: return ''
                    fixed[i + j] = True
        for i, c in enumerate(str1):
            if c == 'F' and res[i : i + m] == list(str2):
                for j in range(i + m - 1, i - 1, -1):
                    if not fixed[j]:
                        res[j] = 'b'
                        break
                else: return ''
        return ''.join(res)
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        