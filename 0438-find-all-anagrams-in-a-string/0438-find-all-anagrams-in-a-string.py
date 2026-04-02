class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        start = 0

        window = len(p)
        result = []

        freq = {}
        freq_w ={}

        for i in p:
            freq[i] = freq.get(i, 0) + 1

        for i, char in enumerate(s):
            freq_w[char] = freq_w.get(char, 0) + 1

            if i - start + 1 > len(p):
                left_char = s[start]
                freq_w[left_char] -= 1
                if freq_w[left_char] == 0:
                    del freq_w[left_char]    # delete key so == comparison works
                start += 1
            if freq_w == freq:
                result.append(start)

        return result








        