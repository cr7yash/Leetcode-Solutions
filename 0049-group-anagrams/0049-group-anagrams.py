class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result =[]

        collection = {}

        for item in strs:
            sorted_word = "".join(sorted(item))
            print(sorted_word)

            if sorted_word not in collection:
                collection[sorted_word] = []
            collection[sorted_word].append(item)
            
        for key,value in collection.items():
            result.append(value)
        return result