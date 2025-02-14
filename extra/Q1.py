def getFinalLocations(locations, movedFrom, movedTo):
    # Convert the initial list of locations to a set
    # This allows for efficient addition and removal of elements
    location_set = set(locations)
    
    # Iterate through the moves using zip to pair movedFrom and movedTo
    for frm, to in zip(movedFrom, movedTo):
        location_set.remove(frm)  # Remove the data from the old location
        location_set.add(to)      # Add the data to the new location
    
    # Convert the set to a sorted list and return it
    # Sorting ensures the output is in ascending order as required
    return sorted(location_set)

# Example usage
locations = [1, 7, 6, 8]  # Initial locations of the data
movedFrom = [1, 7, 2]     # Locations data is moved from
movedTo = [2, 9, 5]       # Locations data is moved to

# Call the function and print the result
result = getFinalLocations(locations, movedFrom, movedTo)
print(result)  # Expected output: [5, 6, 8, 9]


# Alternative approach
def getFinalLocations(locations, movedFrom, movedTo):
    # Step 1: Initialize a dictionary to map data to its location
    location_map = {loc: loc for loc in locations}

    # Step 2: Process each move
    for frm, to in zip(movedFrom, movedTo):
        if frm in location_map:  # Only move if the source exists
            del location_map[frm]  # Remove old location
        location_map[to] = to  # Add new location

    # Step 3: Return sorted list of unique final locations
    return sorted(location_map.values())

# Example usage
locations = [1, 7, 6, 8]
movedFrom = [1, 7, 2]
movedTo = [2, 9, 5]

result = getFinalLocations(locations, movedFrom, movedTo)
print(result)  # Expected output: [5, 6, 8, 9]

