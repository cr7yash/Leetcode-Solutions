class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        current_sum = 0
        count =0
        sub_map = {0:1}

        for num in nums:
            current_sum += num
            diff = current_sum -k

            count += sub_map.get(diff,0) 
            sub_map[current_sum] = 1 + sub_map.get(current_sum,0)


        return count


        