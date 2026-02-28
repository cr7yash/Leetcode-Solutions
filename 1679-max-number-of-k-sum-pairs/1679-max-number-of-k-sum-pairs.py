class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        start = 0
        end = len(nums) - 1
        count = 0
        sorted_nums = sorted(nums)

        while start < end:
            index_sum = sorted_nums[start] + sorted_nums[end]
            if index_sum == k:
                count +=1 
                start += 1
                end -= 1
            elif index_sum < k:
                start += 1
            else:
                end -= 1
        return count
        