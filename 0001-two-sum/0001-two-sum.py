class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for key,val in enumerate(nums):
            compliment = target - val
            if compliment in seen:
                return [seen[compliment], key]
            seen[val] = key

        