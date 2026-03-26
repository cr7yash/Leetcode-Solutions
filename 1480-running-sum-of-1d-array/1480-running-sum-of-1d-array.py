class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefix = [0] * (n+1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
            

        return prefix[1:]
        