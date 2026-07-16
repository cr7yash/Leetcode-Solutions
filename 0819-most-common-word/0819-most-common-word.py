class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for p in "!?',;.":
            paragraph = paragraph.replace(p, " ")

        count = {}
        banned_set = set(banned)

        for word in paragraph.lower().split():
            if word not in banned_set:
                count[word] = count.get(word, 0) + 1
                
        max_count = 0
        best_word = ""
        
        for word in count:
            if count[word] > max_count:
                max_count = count[word]
                best_word = word

        return best_word        