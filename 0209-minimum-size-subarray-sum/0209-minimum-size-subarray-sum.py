class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        current_sum = 0
        min_length = float('inf')

        for right in range(len(nums)):

            current_sum += nums[right]

            while current_sum >= target:
                window_size = right - left + 1
                min_length = min(min_length,window_size)

                current_sum -= nums[left]
                left += 1
        if min_length == float('inf'):
            return 0
        
        return min_length
        