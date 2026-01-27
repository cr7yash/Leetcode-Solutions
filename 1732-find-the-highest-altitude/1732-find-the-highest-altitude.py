class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current_altitude = 0
        max_altitude = 0  
        
        for change in gain:
            
            current_altitude += change
            
            # Check if this is a new peak
            if current_altitude > max_altitude:
                max_altitude = current_altitude
                
        return max_altitude


