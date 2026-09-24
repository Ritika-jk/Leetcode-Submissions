class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []
        temp = []
        n = len(nums)

        def findall(i: int):
            if i == n:
                ans.append(temp.copy())
                return

            # Choose
            temp.append(nums[i])
            findall(i + 1)
            temp.pop()

            # Not choose (skip all identical elements)
            next_idx = i + 1
            while next_idx < n and nums[next_idx] == nums[next_idx - 1]:
                next_idx += 1
            findall(next_idx)

        findall(0)
        return ans