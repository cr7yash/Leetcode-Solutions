class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [0] * length
        
        # 1. Fill answer with Left products
        answer[0] = 1
        for i in range(1, length):
            answer[i] = answer[i-1] * nums[i-1]
        
        # 2. Multiply by Right products on the fly
        R = 1
        for i in range(length - 1, -1, -1):
            # Multiply the Left product (already in answer) by the current Right product
            answer[i] = answer[i] * R
            
            # Update the Right product for the next step
            R = R * nums[i]
            
        return answer