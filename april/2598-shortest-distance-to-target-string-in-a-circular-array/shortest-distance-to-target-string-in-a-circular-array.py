class Solution(object):
    def closestTarget(self, words, target, startIndex):
        n = len(words)
        min_distance = float('inf')

        for i, word in enumerate(words):
            if word == target:
                right_dist = (i - startIndex + n) % n
                left_dist  = (startIndex - i + n) % n
                min_distance = min(min_distance, right_dist, left_dist)

        return -1 if min_distance == float('inf') else min_distance
        """
        :type words: List[str]
        :type target: str
        :type startIndex: int
        :rtype: int
        """
        