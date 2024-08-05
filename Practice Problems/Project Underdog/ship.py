"""
Write a function that counts of the number of ships in a 2D grid.

- Input: an array of arrays of strings, representing a 2D grid. The strings are either a `"."` for open water, or an `"S"` for part of a ship. Connected `"S"`es are part of the same ship.
- Output: an integer that is the count of the number of ships in the grid.

Facts about ships:
- Ships are only horizontal or vertical, not diagonal.
- Ships have a width of one or more and a height of one or more.
- Ships never touch each other.
The input will always be a well-formed grid (all rows are the same length).
Example function calls

    let ships = [
        [".", "S", ".", "S"],
        [".", ".", ".", "S"],
        ["S", "S", ".", "S"],
        [".", ".", ".", "S"]
    ]
    
    countShips(ships) -> 
    let ships = [
        ["S", "S", ".", "S", "S", "S", ".", "."],
        ["S", "S", ".", "S", "S", "S", ".", "."],
        ["S", "S", ".", ".", ".", ".", "S", "S"]
    ]
    countShips(ships) -> 3

plan

create a counter to keep track of the ships
loop through the array
	loop through inner array
		if element in list is 'S' and if there are no 'S' ships above or next to it:
			increase ship counter
return counter
"""
def count_ships(grid):
    # Check if the grid is empty or invalid
    if not grid or not grid[0]:
        return 0
    
    count = 0  # Initialize the ship count to 0
    
    for r in range(len(grid)): # num of rows
        for c in range(len(grid[0])): # num of columns
            if grid[r][c] == "S":  # found part of a ship
                # Check if it's the start of a new ship
                if (r == 0 or grid[r-1][c] == ".") and (c == 0 or grid[r][c-1] == "."):
                    count += 1  # Increment the ship count
    
    return count  

# Example calls
ships1 = [
    [".", "S", ".", "S"],
    [".", ".", ".", "S"],
    ["S", "S", ".", "S"],
    [".", ".", ".", "S"]
]
print(count_ships(ships1))  # Output: 3

ships2 = [
    ["S", "S", ".", "S", "S", "S", ".", "."],
    ["S", "S", ".", "S", "S", "S", ".", "."],
    ["S", "S", ".", ".", ".", ".", "S", "S"]
]
print(count_ships(ships2))  # Output: 3
