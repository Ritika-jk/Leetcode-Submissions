class Solution(object):
    def targetIndices(self, nums, target):
        lt = eq =0
        for x in nums:
            if x < target:
                lt +=1
            elif x == target:
                eq += 1
        return list (range(lt , lt+eq))
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        