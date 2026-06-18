class Solution(object):
    def angleClock(self, hour, minutes):
        minute = minutes * 6
        hourHand = (hour % 12) * 30 + (minutes * 0.5)

        diff = abs(hourHand - minute)

        return min(diff, 360 - diff)
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        