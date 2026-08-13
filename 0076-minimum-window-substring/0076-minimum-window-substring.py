class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        t_count = {}
        for char in t:
            t_count[char] = t_count.get(char, 0) + 1

        window_count = {}
        have = 0
        need = len(t_count)  # Now correctly equals unique chars in t
        left = 0
        min_len = float('inf')
        res = [-1, -1]

        for right in range(len(s)):
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1

            # 1. Check if char satisfies t's frequency requirement
            if char in t_count and window_count[char] == t_count[char]:
                have += 1

            # 2. Shrink window while it's valid
            while have == need:
                # Update best result if current window is smaller
                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    res = [left, right]

                # Remove left character from window
                left_char = s[left]
                window_count[left_char] -= 1
                if left_char in t_count and window_count[left_char] < t_count[left_char]:
                    have -= 1
                left += 1

        # 3. Extract substring if valid result found
        return s[res[0]:res[1] + 1] if min_len != float('inf') else ""