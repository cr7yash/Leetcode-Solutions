class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        result = 0
        running_sum = 0
        seen= {0:1}

        for num in nums:
            running_sum += num

            remainder = running_sum % k

            if remainder in seen:
                result += seen[remainder]
            
            seen[remainder] = seen.get(remainder, 0) + 1

        return result
