class Solution(object):
    def getHappyString(self, n, k):
        total = 3 * (1 << (n - 1))

        if k > total:
            return ""

        k -= 1
        result = []
        prev = ""

        for pos in range(n):

            block = 1 << (n - pos - 1)

            choices = [c for c in ['a','b','c'] if c != prev]

            index = k // block

            char = choices[index]

            result.append(char)
            prev = char

            k %= block

        return "".join(result)

        """
        :type n: int
        :type k: int
        :rtype: str
        """
        