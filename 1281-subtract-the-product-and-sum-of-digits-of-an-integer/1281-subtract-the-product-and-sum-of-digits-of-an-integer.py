class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits =[int(d) for d in str(n)]

        total=0
        product = 1
        result = 0

        for num in digits:
            total += num

            product *= num
        
        return product - total

        