class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        letter_count = {} # track character frequencies
        left = 0 # left boundary of a window
        max_freq = 0 # Track highest freq of a single character in a window
        max_len = 0 # Track longest valid window

        # for word in s:
        #     letter_count[word] = letter_count.get(word,0) + 1

        for right in range(len(s)):
            letter_count[s[right]] = letter_count.get(s[right],0) + 1
            max_freq = max(max_freq, letter_count[s[right]])
            while (right - left + 1) - max_freq > k:
                letter_count[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)

        return max_len
        