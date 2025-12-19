class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # given the candies array and an integer with number of extra candies
        # I need to add the extra candies to each integer in candies array
        # After adding I need to check whether after adding the extra candies
        # what is the greatest number of candies among kids. It can be multiple kids
        greatest = max(candies)
        result = []

        for candy in candies:
            if candy + extraCandies >= greatest:
                result.append(True)
            else:
                result.append(False)

        return result