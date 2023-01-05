shape1, shape2 = tuple(input())

shapes = {
    "F":[(1,0), (1,-1), (0, -1), (1,-2), (2,-2)], 
    "G": [(1,0), (1,-1), (2,-1), (1,-2), (0,-2)], 
    "I":[(0,0), (0,-1), (0,-2), (0,-3), (0,-4)], 
    "L": [(0, 0), (0, -1), (0, -2), (0, -3), (1,0)], 
    "J":[(0, 0), (1,0), (1,-1), (1,-2), (1,-3)], 
    "N":[(0,0), (0,-1), (0,-2), (1,-2), (1,-3)], 
    "M":[(0 ,-2), (0,-3), (1,-2), (1,-1), (1,0)], 
    "P": [(0,0), (0,-1), (0,-2), (1,-1), (1,-2)], 
    "Q": [(0,-1), (0,-2), (1,0), (1,-1), (1,-2)], 
    "T": [(0,-2), (1,0), (1,-1), (1,-2), (2,-2)],
    "U": [(0,0), (0,-1), (1,0), (2,0), (2,-1)],
    "V": [(0,0), (0,-1), (0,-2), (1,0), (2,0)],
    "W": [(0,-2), (0,-1), (1,-1), (1,0), (2,0)],
    "X":[(1,0), (1,-1), (1,-2), (0,-1), (2,-1)], 
    "Z": [(0,-2), (1,-2), (1,-1), (1,0), (2,0)],
    "S": [(0,0), (1,0), (1,-1), (1,-2), (2,-2)],
    "Y": [(0,-2), (1,0), (1,-1), (1,-2), (1,-3)],
    "A": [(0,0), (0,-1), (0,-2), (0,-3), (1,-2)]
}

shape1 = shapes[shape1]
shape2 = shapes[shape2]

gridStart = set()
x,y = (7,7)
for dx, dy in shape1:
    gridStart.add((x+dx, y+dy))

shape1BL = [x,y]
check = []
dist = 0
visited = set()
for y in range(0, 14):
    for x in range(0, 14):
        grid = gridStart.copy()
        join = False
        for dx, dy in shape2:
            grid.add((x+dx, y+dy))
            if not join:
                for changeX, changeY in [(0,1), (1,0), (0,-1), (-1,0)]:
                    if (x+dx+changeX, y+dy+changeY) in gridStart:
                        join = True
                        break
        if not join:
            #print("not touching")
            continue
        if len(grid) < 10:
            #print("overlap")
            continue


        refPoint = (x,y)            
        if shape1BL[0] < x:
            refPoint = tuple(shape1BL)
        if shape1BL[0] == x:
            if shape1BL[1] > y:
                refPoint = tuple(shape1BL)

        rX, rY = refPoint

        relation = []

        for xPos,yPos in grid:
            relation.append((xPos-rX, yPos-rY))
        if tuple(sorted(relation)) in visited:
            """print("not discinct")
            for i in range(0, 14):
                row = ""
                for j in range(0,14):
                    if (j,i) in gridStart:
                        row += "A"
                    elif (j,i) in grid:
                        row += "B"
                    else:
                        row += "."
                print(row)"""
            pass
        else:
            dist += 1
            #print(x,y)
            #print(shape1BL[0]-x, shape1BL[1]-y)
            visited.add(tuple(sorted(relation)))
            """for i in range(0, 14):
                row = ""
                for j in range(0,14):
                    if (j,i) in gridStart:
                        row += "A"
                    elif (j,i) in grid:
                        row += "B"
                    else:
                        row += "."
                print(row)"""

print(dist)