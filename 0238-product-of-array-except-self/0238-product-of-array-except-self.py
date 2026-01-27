class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        
        # 1. Build Left Product Array
        L = [0] * length
        L[0] = 1
        for i in range(1, length):
            L[i] = L[i-1] * nums[i-1]
            
        # 2. Build Right Product Array
        R = [0] * length
        R[-1] = 1
        for i in range(length - 2, -1, -1):
            R[i] = R[i+1] * nums[i+1]
            
        # 3. Combine them
        answer = []
        for i in range(length):
            answer.append(L[i] * R[i])
            
        return answer