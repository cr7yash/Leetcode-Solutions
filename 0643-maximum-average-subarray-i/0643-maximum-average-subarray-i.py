class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        current_state = 0
        best_avg = float('-inf')

        for right in range(len(nums)):
            current_state += nums[right]

            if right >= k - 1:
                best_avg = max(best_avg, current_state/k)
                current_state -= nums[right - k +1] 

        return best_avg

        