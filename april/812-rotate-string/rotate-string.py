class Solution(object):
    def rotateString(self, s, goal):
        # Basic length check: different lengths can never be rotations
        if len(s) != len(goal):
            return False
            
        # The first character of s is our anchor for finding the starting point
        target = s[0]
        
        for i, char in enumerate(goal):
            # If the current character in goal matches our anchor
            if char == target:
                # Reconstruct the rotation: [End Part] + [Beginning Part]
                if s == goal[i:] + goal[:i]:
                    return True
                    
        return False 