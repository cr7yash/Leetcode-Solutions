class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if not word1 or not word2:
            return false

        n1, n2 = len(word1), len(word2)

        merged_list =[]

        for i in range(max(len(word1),len(word2))):
            if i < n1:
                merged_list.append(word1[i])

            if i < n2:
                merged_list.append(word2[i])
        return "".join(merged_list)