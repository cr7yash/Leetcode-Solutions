class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_hurdle = float('inf')
        second_hurdle = float('inf')

        for n in nums:
            if n <= first_hurdle:
                first_hurdle = n
            elif n<= second_hurdle:
                second_hurdle = n
            else:
                return True
        return False


        