class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Check if all characters in t are found in the current window
        def is_all_found():
            for c in remains.keys():
                if remains[c] > 0:
                    return False
            return True

        remains = collections.Counter(t)
        min_window = ""
        l = r = 0
        while r < len(s):
            if s[r] in t:
                remains[s[r]] -= 1
            # The character s[r] is redundant
            if remains[s[r]] <= 0:
                # Move the l to the right
                while l < r:
                    if s[l] in t:
                        if remains[s[l]] >= 0:  # The character s[l] can't be removed
                            break
                        else:  # It can be removed
                            remains[s[l]] += 1
                    l += 1

            # Update the min_window
            if is_all_found():
                if min_window == "" or len(min_window) > r - l + 1:
                    min_window = s[l:r + 1]

            r += 1

        return min_window
