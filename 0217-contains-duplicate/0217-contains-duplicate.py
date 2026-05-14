class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        freq = {}

        for num in nums:
            # Get current count (default to 0 if not found) and add 1
            freq[num] = freq.get(num, 0) + 1
            
            # Check immediately if this number has appeared more than once
            if freq[num] > 1:
                return True

        return False
        