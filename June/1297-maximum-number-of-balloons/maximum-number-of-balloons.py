
class Solution:
    def maxNumberOfBalloons(self, text) :
        b = a = l = o = n = 0

        for c in text:
            if c == 'b':
                b += 1
            elif c == 'a':
                a += 1
            elif c == 'l':
                l += 1
            elif c == 'o':
                o += 1
            elif c == 'n':
                n += 1

        return min(b, a, n, l // 2, o // 2)