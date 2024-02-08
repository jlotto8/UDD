"""
function that calculates, takes input parameters
parameter list of lists
4 accumulators
min x
max x
min y
max y

rectangles = [[x,y,l,w,]]
list of dictionaries 
rectangle: x,y,l,w

loop  through list of dict
each dict will complete calculation

"""

def find_minimum_bounding_rectangle(rectangles):
    min_x = float('inf')
    min_y = float('inf')
    max_x = float('-inf')
    max_y = float('-inf')

    # Loop through each rectangle dictionary in the list of rectangles
    for rect in rectangles:
        x = rect['x'] # extract the x-coordinate, y-coordinate, length, and width from the current rectangle dictionary
        y = rect['y']
        length = rect['length']
        width = rect['width']

        min_x = min(min_x, x) # updates min_x by taking the minimum value between its current value and the x-coordinate of the current rectangle- for the leftmost x-coordinate
        min_y = min(min_y, y) # bottommost y-coordinate
        max_x = max(max_x, x + length) # updates max_x by taking the maximum value between its current value and the sum of the x-coordinate and length of the current rectangle - for the rightmost x-coordinate
        max_y = max(max_y, y + width) # topmost y-coordinate

    # Calculate width and height of the bounding box
    width = max_x - min_x
    height = max_y - min_y

    # Create the minimum bounding rectangle
    bounding_rectangle = (min_x, min_y, width, height)

    return bounding_rectangle

# Example usage with a list of rectangle dictionaries
rectangles = [
    {'x': 1, 'y': 1, 'length': 4, 'width': 5},
    {'x': 2, 'y': 3, 'length': 6, 'width': 7},
    {'x': 4, 'y': 5, 'length': 4, 'width': 5}
]

result = find_minimum_bounding_rectangle(rectangles)
print(result)

# future make a class 