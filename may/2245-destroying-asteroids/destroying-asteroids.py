class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        asteroids.sort()

        curr_mass = mass

        for asteroid in asteroids:
            if curr_mass < asteroid:
                return False
            curr_mass += asteroid

        return True
        """
        :type mass: int
        :type asteroids: List[int]
        :rtype: bool
        """
        