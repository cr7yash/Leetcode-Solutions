class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}

        for char in s:
            freq[char] = freq.get(char, 0) + 1 
        # {'l': 1, 'e': 3, 't': 1, 'c': 1, 'o': 1, 'd': 1}
        for index, char in enumerate(s):
            if freq[char] == 1:
                return index
                break
        return -1
            