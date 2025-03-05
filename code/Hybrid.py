def hybridSuitcasePacking(size, n, c):
    # Initialize the list to keep track of suitcase capacities. Each suitcase starts with the given capacity c.
    suitcaseCapacity = [c]

    # Iterate through each item
    for i in range(n):
        placed = False  # This flag tracks whether the current item has been placed in a suitcase
        itemSize = size[i]  # Get the size of the current item

        # First, attempt to place the item in an existing suitcase using the Best Fit strategy
        for j in range(len(suitcaseCapacity)):
            if itemSize <= suitcaseCapacity[j]:  # Check if the item fits in the current suitcase
                suitcaseCapacity[j] -= itemSize  # Reduce the remaining capacity of the suitcase
                placed = True  # Mark the item as placed
                break  # Exit the loop as the item is placed

        # If the item doesn't fit in any existing suitcase, create a new one using the Next Fit strategy
        if not placed:
            suitcaseCapacity.append(c - itemSize)  # Add a new suitcase with adjusted remaining capacity

    # Return the total number of suitcases used
    return len(suitcaseCapacity)

# List of item sizes
size = [0.5, 0.7, 0.5, 0.2, 0.4, 0.2, 0.5, 0.5, 0.6]
suitcaseCapacity = 3  # Capacity of each suitcase
numItems = len(size)  # Total number of items

# Calculate the minimum number of suitcases required
minSuitcase = hybridSuitcasePacking(size, numItems, suitcaseCapacity)

# Print the result
print("Number of suitcases required:", minSuitcase)
