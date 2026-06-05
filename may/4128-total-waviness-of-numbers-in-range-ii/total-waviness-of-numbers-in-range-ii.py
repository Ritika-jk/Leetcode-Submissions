class Solution(object):
    def totalWaviness(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        def solve(N_str):
            n = len(N_str)
            memo = {}

            def dp(idx, prev, direction, is_less, is_started):
                if idx == n:
                    return 1, 0

                state = (idx, prev, direction, is_less, is_started)
                if state in memo:
                    return memo[state]

                limit = int(N_str[idx]) if not is_less else 9
                total_count = 0
                total_waviness = 0

                for digit in range(limit + 1):
                    new_less = is_less or (digit < limit)
                    new_started = is_started or (digit > 0)

                    if not new_started:
                        c, w = dp(idx + 1, -1, 0, new_less, False)
                        total_count += c
                        total_waviness += w
                    else:
                        add = 0
                        new_dir = 0
                        if prev != -1:
                            if digit > prev:
                                new_dir = 1
                                if direction == 2:
                                    add = 1
                            elif digit < prev:
                                new_dir = 2
                                if direction == 1:
                                    add = 1
                        c, w = dp(idx + 1, digit, new_dir, new_less, True)
                        total_count += c
                        total_waviness += w + add * c

                memo[state] = (total_count, total_waviness)
                return memo[state]

            return dp(0, -1, 0, False, False)[1]

        return solve(str(num2)) - solve(str(num1 - 1))