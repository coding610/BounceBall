import time
import sys
import random

from Var import *

from Classes.fallingObj import *
from Classes.obstacleLine import *
from Classes.drgBall import *

pygame.font.init()

# MAIN FUNCTION
def main():
    # Preperations
    global spaceDown
    global falling
    wn.fill(bgColor)

    # CREATE OBJ
    DragBall = dragBall(startX, startY, drgStrengthX, drgStrengthY)
    Circle = fallingObject(startPlrGravity, startPlrRadius, startPlrXPos, startPlrYPos, startPlrVX, startPlrVY, startPlrBounceEff, startPlrWidth)
    

    obstacles.append(obstaclePoly((300, 200), (370, 270), (500, 590), (100, 500)))


    # TEXT
    seconds = 0
    
    font = pygame.font.SysFont('Comic Sans MS', 30) 
    text_surface = font.render(str(seconds) + "s", False, (0, 0, 0))

    # MAIN LOOP
    while True:
        # Event
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    sys.exit()

            if DragBall.drag(event):
                Circle.gravity = 9.82
                Circle.vX = DragBall.power[0]
                Circle.vY = -DragBall.power[1]
        

        #------DRAW-------
        wn.fill(bgColor)
        # Player

        Circle.drawCircle()
        wn.blit(text_surface, (10, 10))

        # Obstacle Draw and collision
        for object in obstacles:
            obstaclePoly.drawObstacle(object)
            Circle.collideObstacle(object)


        # UPDATE
        text_surface = font.render(str(int(seconds)) + "s", False, (0, 0, 0))

        Circle.updatePos()

        pygame.display.flip()
        pygame.display.update()

        clock.tick(30)
       

        seconds += 0.03


    pygame.quit()
