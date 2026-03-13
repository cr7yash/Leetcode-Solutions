class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        total_units = 0
        number_of_units = 0
        boxTypes.sort(key= lambda x: x[1],reverse=True)
    

        for number_of_boxes, units_per_box in boxTypes:

            if truckSize >= number_of_boxes:
                total_units += number_of_boxes * units_per_box
                truckSize -= number_of_boxes
            else:
                total_units += truckSize * units_per_box
                break
        
        return total_units