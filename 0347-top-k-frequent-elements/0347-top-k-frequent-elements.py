class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        

        for num in nums:
            freq[num] = freq.get(num,0) + 1

        items = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        result = [x[0] for x in items[:k]]

        return result



