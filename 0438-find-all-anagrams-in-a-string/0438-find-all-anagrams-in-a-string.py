class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        if len(p) > len(s):
            return []

        p_count ={}
        s_count ={}
        result =[]
        k = len(p)

        for i in range(k):
            s_count[s[i]] = s_count.get(s[i],0) + 1
            p_count[p[i]] = p_count.get(p[i],0) + 1

        if s_count == p_count:
            result.append(0)            

        for i in range(k, len(s)):
            # 1. Add incoming character: s[i]
            s_count[s[i]] = s_count.get(s[i], 0) + 1

            # 2. Remove outgoing character: s[i - k]
            s_count[s[i - k]] -= 1
            if s_count[s[i - k]] == 0:
                del s_count[s[i - k]]

            # 3. Check match & append starting index (i - k + 1)
            if s_count == p_count:
                result.append(i - k + 1)            

        return result