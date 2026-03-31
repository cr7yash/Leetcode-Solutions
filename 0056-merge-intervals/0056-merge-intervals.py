class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:


        sorted_interval = sorted(intervals)
        result = [sorted_interval[0]]

        for start, end in sorted_interval[1:]:

            if start <= result[-1][1]:
                result[-1][1] = max(end, result[-1][1])
            else:
                result.append([start,end])

        return result






        
        
