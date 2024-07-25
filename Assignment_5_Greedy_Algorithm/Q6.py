def maximumUnits(boxTypes, truckSize):
    # Sort the box types by the number of units per box in descending order
    boxTypes.sort(key=lambda x: x[1], reverse=True)
    
    total_units = 0
    remaining_capacity = truckSize
    
    for numberOfBoxes, unitsPerBox in boxTypes:
        if remaining_capacity >= numberOfBoxes:
            # If the truck can take all boxes of this type
            total_units += numberOfBoxes * unitsPerBox
            remaining_capacity -= numberOfBoxes
        else:
            # If the truck can only take a part of these boxes
            total_units += remaining_capacity * unitsPerBox
            break
    
    return total_units


boxTypes1 = [[1, 3], [2, 2], [3, 1]]
truckSize1 = 4
print(maximumUnits(boxTypes1, truckSize1))  

boxTypes2 = [[5, 10], [2, 5], [4, 7], [3, 9]]
truckSize2 = 10
print(maximumUnits(boxTypes2, truckSize2)) 
