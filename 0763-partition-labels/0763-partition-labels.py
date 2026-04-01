class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        result = []
        freq={}

        start = 0
        end = 0

        for index, char in enumerate(s):
            freq[char] = index

        for index, char in enumerate(s):
            end = max(end, freq[char])
            if index == end:
                result.append(end - start + 1)
                start = index + 1

        return result

            



        