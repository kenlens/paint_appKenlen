bS = 30
yC = 520
# for every new xCoordinate, add 35, but keep the yCoordinate the same
def setup():
    size(800, 600)         # width, height
    rect(5, 5, 80, 505)    # xCoordinate, yCoordinate, width, height # side color selector
    rect(5, 515, 789, 80)  # bottom selector box
    rect(100, 5, 693, 505) # color space box
    fill(139, 119, 101)    # pastel dull brown
    rect(10, yC, bS, bS)   
    fill(220, 220, 220)    # soft blue snow
    rect(45, yC, bS, bS)   
    fill(193, 205, 193)    # blue ice
    rect(80, yC, bS, bS)   
    fill (230, 230, 250)   # blue lavender
    rect(115, yC, bS, bS)  
    fill(70, 130, 180)     # blue steel
    rect(150, yC, bS, bS)  
    fill(0, 255, 255)      # neon cyan
    rect(185, yC, bS, bS)  
    
    
def draw():
    if mousePressed and mouseX > 100 and mouseY > 5 and mouseX < 793 and mouseY < 510 and pmouseX > 100 and pmouseY > 5 and pmouseX < 793 and pmouseY < 510: # this keeps the drawing within the color space boundaries
        line(pmouseX, pmouseY, mouseX, mouseY)
            

def mouseClicked():
    if mouseX > :
