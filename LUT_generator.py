#Ajidamoo movegen lookup table generator

import time as t

def generate_rookwise(square):

    #generate south rookwise positions:
    south = []
    x = square
    while x >= 0:
        x = x - 8
        south.append(x)
    south.pop() #remove the last value because it's off the board
    

    #north rookwise positions:
    north = []
    x = square
    while x <= 63: 
        x = x + 8
        north.append(x)
    north.pop()
    

    
    #east rookwise positions:
    east = []
    x = square
    lastx = 0
    while True:
        lastmodx = x%8
        x = x+1
        if x%8 < lastmodx:
            break
        east.append(x)
    
    #west rookwise positions:
    west = []
    x = square
    lastx = 0
    while True:
        lastmodx = x%8
        x = x-1
        if x%8 > lastmodx:
            break
        west.append(x)
    
    result = [north,south,east,west]
    
    #don't do these things for easier pawn stuff V
    
    #result = [ele for ele in result if ele != []] #clear empty elements
    #result.sort(key=len, reverse = True) # sort for longer moves first, this could help with move ordering
    
    return result

def generate_bishopwise(square):
    #generate southeast positions:
    southeast = []
    x = square
    lastmodx = x%8
    while True:
        lastmodx = x%8
        x = x-7
        if x%8 < lastmodx or x < 0:
            break
        southeast.append(x)
    
    #generate southwest positions:
    southwest = []
    x = square
    lastmodx = x%8
    while True:
        lastmodx = x%8
        x = x-9
        if x%8 > lastmodx or x < 0:
            break
        southwest.append(x)
    
    
    #generate northwest positions:
    northwest = []
    x = square
    lastmodx = x%8
    while True:
        lastmodx = x%8
        x = x+7
        if x%8 > lastmodx or x > 63:
            break
        northwest.append(x)
    
    #generate northeast positions:
    northeast = []
    x = square
    lastmodx = x%8
    while True:
        lastmodx = x%8
        x = x+9
        if x%8 < lastmodx or x > 63:
            break
        northeast.append(x)
    
    
    result = [southeast,southwest,northwest,northeast]
    #result = [ele for ele in result if ele != []] #clear empty elements
    #result.sort(key=len, reverse = True)
    
    return result

def generate_knightwise(square):
    #southeast positions:
    result = []
    if not ((square-6)%8 < square%8 or square-6 < 0):
        result.append([square-6])
    
    if not ((square-15)%8 < square%8 or square-15 < 0):
        result.append([square-15])
    
    
    #southwest positions:
    if not ((square-10)%8 > square%8 or square-10 < 0):
        result.append([square-10])
    
    if not ((square-17)%8 > square%8 or square-17 < 0):
        result.append([square-17])
    
    #northwest positions:
    if not ((square+6)%8 > square%8 or square+6 > 63):
        result.append([square+6])
    
    if not ((square+15)%8 > square%8 or square+15 > 63):
        result.append([square+15])
    
    
    #northeast positions:
    if not ((square+10)%8 < square%8 or square+10 > 63):
        result.append([square+10])
    
    if not ((square+17)%8 < square%8 or square+17 >63):
        result.append([square+17])
    
    #print(str(result))
    
    return result

def generate_colorchangetable(): #generate the table that inverts color for pieces
    result = []
    for i in range(120):
        if i <= 19:
            result.append((i - (i%10) - 5) * -1 + 5 + i%10)
        else:
            result.append(i)
    return result
            
    
start_time = t.perf_counter()

final_result = []

for i in range(64):
    final_result.append([generate_rookwise(i),generate_bishopwise(i),generate_knightwise(i)])

#print(str(final_result))

print(str(generate_colorchangetable()))

#print("total time elapsed: {}".format(t.perf_counter()-start_time))

#generate_bishopwise(12)

#print(str(generate_knightwise(54)))
