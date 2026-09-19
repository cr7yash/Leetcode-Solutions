class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_len = 0
        running_sum = 0
        seen = {0:-1}

        for i,num in enumerate(nums):
            if num == 1:
                running_sum += 1
            else:
                running_sum -= 1
            
            if running_sum in seen:
                max_len = max(i - seen[running_sum], max_len)
            else:
                seen[running_sum] = i
        return max_len