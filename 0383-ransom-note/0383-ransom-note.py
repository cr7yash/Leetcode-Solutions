class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        if len(ransomNote) > len(magazine):
            return False
        map1 ={}
        map2 = {}

        for i in ransomNote:
            map1[i] = map1.get(i,0) + 1

        for j in magazine:
            map2[j] = map2.get(j,0) + 1

        for c in map1:
            if c not in map2 or map1[c] > map2[c]:
                return False
            
        return True
