from math import isqrt

class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        res = 1
        fac = []

        # Find all divisors of n
        for i in range(1, isqrt(n) + 1):
            if n % i == 0:
                fac.append(i)
                if n // i != i:
                    fac.append(n // i)

        sorted_nums = sorted(nums)

        def check(k):
            # Check every block of size k
            for left in range(0, n, k):
                right = left + k

                # Already matches the required sorted block
                if nums[left:right] == sorted_nums[left:right]:
                    continue

                # Find the first decrease and try rotating there
                for i in range(left, right - 1):
                    if nums[i] > nums[i + 1]:
                        if not nums[i+1:right] + nums[left:i+1] == sorted_nums[left:right]:
                            return False
                        else:
                            break
                else:
                    # No decrease, but the block doesn't match
                    return False

            return True

        # k = 1 works only when the array is already sorted
        res = 1 if sorted_nums == nums else 0

        # Check the remaining divisors
        for f in fac[1:]:
            if check(f):
                res += f

        return res