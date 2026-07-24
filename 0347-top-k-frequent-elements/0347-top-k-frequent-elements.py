class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        collection = {}
        result = []

        for num in nums:
            collection[num] = collection.get(num, 0) + 1 

        sorted_items = sorted(collection.items(),key = lambda x: x[1], reverse=True)
        print(sorted_items)

        return [count for count, value in sorted_items[:k]]
