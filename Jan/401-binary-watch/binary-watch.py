class Solution(object):
    def countBits(self, n):
        c = 0
        while n:
            c += n % 2
            n //= 2
        return c

    def readBinaryWatch(self, turnedOn):
        ans = []
        for h in range(12):
            for m in range(60):
                if self.countBits(h) + self.countBits(m) == turnedOn:
                    time = str(h) + ":"
                    if m < 10:
                        time += "0"
                    time += str(m)
                    ans.append(time)
        return ans
        