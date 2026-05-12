class Solution(object):
    def minimumEffort(self, tasks):
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)

        ans = 0
        energy = 0

        for actual, minimum in tasks:

            # increase energy if needed
            if energy < minimum:
                ans += minimum - energy
                energy = minimum

            # perform current task
            energy -= actual

        return ans
        """
        :type tasks: List[List[int]]
        :rtype: int
        """
        