class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        current = 0
        next = 0

        while current < len(s) and next < len(t):
            if s[current] == t[next]:
                current += 1
            
            next += 1
        
        return current == len(s)
        
