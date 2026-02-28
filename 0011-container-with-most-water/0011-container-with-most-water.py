class Solution:
    def maxArea(self, height: List[int]) -> int:
        # height = [1,8,6,2,5,4,8,3,7]
        start = 0
        end = len(height) - 1
        max_area = 0

        while start < end:
            width = end - start
            container_height = min(height[start], height[end])
            current_area = width * container_height
            max_area = max(max_area, current_area)

            if height[start] < height[end]:
                start += 1

            elif height[start] > height[end]:
                end -= 1
            else:
                start += 1

        
        return max_area



         



        