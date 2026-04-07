class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        current_sum = 0
        freq = {0: 1}
        count = 0

        for num in nums:
            current_sum += num

            test = current_sum % k

            if test in freq:
                count += freq[test]
            freq[test] = freq.get(test, 0) + 1

        return count


