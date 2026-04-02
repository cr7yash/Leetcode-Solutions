class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        start = 0
        max_length = 0
        str_set = set()    

        for char in s:
            while char in str_set:    # keep shrinking
                str_set.remove(s[start])
                start += 1
            str_set.add(char)
            max_length = max(max_length, len(str_set))

        return max_length   





        