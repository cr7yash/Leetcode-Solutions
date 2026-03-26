class Solution:
    def singleNumber(self, nums: List[int]) -> int:        

        freq={}

        # go through every element and find the occurence of elements
        # check which element occurs only once and return that element

        n = len(nums)

        for i in range(n):
            freq[nums[i]] = freq.get(nums[i], 0) + 1

        for key,value in freq.items():
            if value == 1:
                return key
                

        
 


        