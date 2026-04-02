class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        nums.sort()

        result = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            fix = nums[i]
            start = i + 1
            end = len(nums) - 1

            if i > 0 and nums[i] == nums[i-1]:
                continue


            while start < end:

                if nums[start] + nums[end] == -fix:
                    result.append([nums[i],nums[start],nums[end]])
                    start += 1
                    end -= 1
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1
                    while start < end and nums[end] == nums[end + 1]:
                        end -= 1

                elif nums[start] + nums[end] > -fix:
                    end -= 1
                else:
                    start += 1

        return result

        




        