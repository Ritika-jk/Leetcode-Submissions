class Solution(object):
    def lexGreaterPermutation(self, s, target):
        n = len(s)

        count = [0] * 26
        for ch in s:
            count[ord(ch) - 97] += 1

        matched_len = n
        for i in range(n):
            idx = ord(target[i]) - 97
            if count[idx] > 0:
                count[idx] -= 1
            else:
                matched_len = i
                break

        start_index = n - 1 if matched_len == n else matched_len

        if matched_len == n:
            count[ord(target[start_index]) - 97] += 1

        for i in range(start_index, -1, -1):
            target_idx = ord(target[i]) - 97

            chosen = -1
            for c in range(target_idx + 1, 26):
                if count[c] > 0:
                    chosen = c
                    break

            if chosen != -1:
                count[chosen] -= 1

                result = list(target[:i])
                result.append(chr(97 + chosen))
                for c in range(26):
                    result.append(chr(97 + c) * count[c])
                return ''.join(result)

            if i > 0:
                count[ord(target[i - 1]) - 97] += 1

        return ""
        """
        :type s: str
        :type target: str
        :rtype: str
        """
        