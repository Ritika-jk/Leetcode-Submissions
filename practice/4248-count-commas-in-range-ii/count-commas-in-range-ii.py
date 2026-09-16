class Solution:
    def countCommas(self, n: int) -> int:
        if n<= 999:
            return 0
        total =0
        rangestart = 1000
        rangeend = rangestart * 1000 - 1
        commas =1
        while rangestart <=n :
            numbers = min(n, rangeend ) - rangestart+1 
            total += commas * numbers
            if rangeend > n:
                break 
            rangestart *=  1000
            rangeend = rangestart * 1000 -1
            commas +=1
        return total