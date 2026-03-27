class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []

        word_freq ={}

        for word in strs:
            sorted_word = "".join(sorted(word))
            
            if sorted_word not in word_freq:
                word_freq[sorted_word] = [word]
            else:
                word_freq[sorted_word].append(word)
        
        for key,value in word_freq.items():
            result.append(value)

        return result
                




        