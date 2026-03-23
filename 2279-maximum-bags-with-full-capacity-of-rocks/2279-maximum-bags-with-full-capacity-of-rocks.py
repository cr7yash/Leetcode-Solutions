class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        
        gaps = [c-r for c, r in zip(capacity, rocks)]
        gaps.sort()
        count = 0

        for i in range(len(gaps)):
            if additionalRocks >= gaps[i]:
                additionalRocks -= gaps[i]
                count += 1
            else:
                break
        return count