class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # edge case
        if (len(nums) == 0):
            return -1
            
        # nums = [1,1,4,2,3], x = 5
        
        total = sum(nums)
        target = total - x
        
        left = 0
        right = 0
        currentTotal = 0
        res = float('inf')
        
        while right < len(nums):
            # expand the window here
            rightNum = nums[right]
            right += 1
            
            currentTotal += rightNum
            
            # if I want to shrink the window
            while currentTotal > target and left < right:
                # shrink the window here
                leftNum = nums[left]
                left += 1
                
                currentTotal -= leftNum
            
            # collect the result
            if currentTotal == target:
                res = min(res, len(nums) - (right - left))
                
        return res if res != float('inf') else -1
"""

[1,1,4,2,3]

left = 1
right = 1 

1 + 1 - 5 = -3


        left = 0
        count = 0
        for right in range(len(nums)):
            
            while left <= right:
            # [1,1,4,2,3]
                if (nums[left] + nums[right]) == x
                    return 
                     
                else if (nums[left] + nums[right]) > x:
                    right += 1
                else if (nums[left] + nums[right]) < x:
                    left += 1
                    right += 1
                else:
                    return -1
"""            
            
            
        
        
        


"""
left = 0
right = 0
nums = [1,1,4,2,3], x = 4
remove 1 and 3
[1,4,2] -> consecutive subarray
nums = [1,1,4,2,3], x = 4
sum is every element in array's sum
target = sum - x
[1,4,2] -> 7
task: consecutive subarray

key logic of how to resolve a sliding window
1. expand the window: the sum in the window is less than target
2. shrink the window: the sum in the window is more than target
3. collect the result: the sum in the window equals the target, and find the minimal one

// Pseudocode framework of sliding window algorithm
void slidingWindow(string s) {
    // Use an appropriate data structure to record the data
    // in the window, varying with the specific scenario
    // For instance, if I want to record the frequency
    // of elements in the window, I would use a map
    // If I want to record the sum of elements in the window, I can simply use an int
    auto window = ...

    int left = 0, right = 0;
    while (right < s.size()) {
        // c is the character that will be entering the window
        char c = s[right];
        window.add(c);
        // Expand the window
        right++;

        // Perform a series of updates to the data within the window
        ...

        // *** position of debug output ***
        printf("window: [%d, %d)\n", left, right);
        // Note that printing should be avoided in the final solution code
        // Because IO operations are time-consuming and may cause timeouts

        // Determine whether the left side of the window needs to shrink
        while (window needs shrink) {
            // d is the character that will be removed from the window
            char d = s[left];
            window.remove(d);
            // Shrink the window
            left++;

            // Perform a series of updates to the data within the window
            ...
        }
    }
}
"""


