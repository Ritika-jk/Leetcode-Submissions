class Solution(object):
    def processStr(self, s):
        res = []
        n = len(s)

        for i in range(n):
            ch = s[i]

            if ch == '*':
                if len(res) != 0:
                    res.pop()
            elif ch == '#':
                res.extend(res)
            elif ch == '%':
                res.reverse()
            elif 'a' <= ch <= 'z':
                res.append(ch)

        return ''.join(res)
        """
        :type s: str
        :rtype: str
        """
        