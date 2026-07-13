class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        map1 = {}
        map2 = {}

        for ltr in s:
            map1[ltr] = map1.get(ltr, 0) + 1
        
        for ltr in t:
            map2[ltr] = map2.get(ltr, 0) + 1

        if map1 == map2:
            return True
        
        return False
