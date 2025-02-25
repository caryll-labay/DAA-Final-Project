def hybridSuitcasePacking(size, n, c):
    suitcaseCapacity = [c]

    for i in range(n):
        placed = False
        itemSize = size[i]

        # First, try to fit the item in an existing suitcase using Best Fit strategy
        for j in range(len(suitcaseCapacity)):
            if itemSize <= suitcaseCapacity[j]:
                suitcaseCapacity[j] -= itemSize
                placed = True
                break

        # If the item couldn't be placed in an existing suitcase, create a new suitcase (Next Fit strategy)
        if not placed:
            suitcaseCapacity.append(c - itemSize)

    return len(suitcaseCapacity)


size = [0.5, 0.7, 0.5, 0.2, 0.4, 0.2, 0.5, 0.5, 0.6]
suitcaseCapacity = 3
numItems = len(size)

minSuitcase = hybridSuitcasePacking(size, numItems, suitcaseCapacity)

print("Number of suitcase required:", minSuitcase)
