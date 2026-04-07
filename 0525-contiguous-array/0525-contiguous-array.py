class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        max_length = 0
        balance = 0
        freq = {0: -1}

        for i, num in enumerate(nums):
            if num == 1:
                balance += 1
            else:
                balance -= 1
            
            if balance in freq:
                max_length = max(max_length, i - freq[balance])
            else:
                freq[balance] = i
        return max_length








        