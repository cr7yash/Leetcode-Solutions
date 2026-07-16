class Solution:
    def firstUniqChar(self, s: str) -> int:

        count ={}
        for char in s:
            count[char] = count.get(char, 0) + 1

        for key,val in enumerate(s):

            if count[val] == 1:
                return key
        return -1