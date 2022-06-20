from Var import *
import time
import math
import random

class fallingObject:
    def __init__(self, gravity, radius, xPos, yPos, vX, vY, bounceEff, width):
        self.gravity = gravity
        self.radius = radius
        self.yPos = yPos
        self.xPos = xPos
        self.vX = vX
        self.vY = vY
        self.bounceEff = bounceEff
        self.width = width
        
    def updatePos(self):
        self.vX = self.vX
        self.vY += (self.gravity * mTime) 
        
        self.yPos += self.vY
        self.xPos += self.vX

        self.collision()


    def collision(self):
        self.collideWY()
        self.collideWX()

    def collideWY(self):
        if self.yPos > wH - self.radius:
            self.vY = -self.vY * self.bounceEff
            self.yPos = wH - self.radius

        elif self.yPos < self.radius:
            self.vY = -self.vY * self.bounceEff
            self.yPos = self.radius + 1

    def collideWX(self):
        # Left
        if self.xPos < self.radius: 
            self.xPos = self.radius + 1
            self.vX = -self.vX

        # Right
        elif self.xPos > wW - self.radius:
            self.xPos = (wW - self.radius) - 1
            self.vX = -self.vX * self.bounceEff


    def collideObstacle(self, object):
        # First find origo
        lenX = abs(object.p1[0] - object.p2[0])
        lenY = abs(object.p1[1] - object.p4[1])

        if object.p1[0] < object.p2[0]:
            pMidX = abs(object.p1[0] + lenX/2)
        else:
            pMidX = abs(object.p2[0] + lenX/2)

        if object.p1[1] < object.p4[1]:
            pMidY = abs(object.p1[1] + lenY/2)
        else:
            pMidY = abs(object.p4[1] + lenY/2)

        origo = (pMidX, pMidY)


        # Second find axis
        obA1 = origo[1]
        obA2 = origo[0]
        
        plA1 = self.yPos
        plA2 = self.xPos

        pygame.draw.line(wn, (0, 0, 255), (plA2, 0), (plA2, wH))
        pygame.draw.line(wn, (0, 0, 255), (0, plA1), (wW, plA1))
        
        # Player
        pX1 = self.xPos + self.radius
        pX2 = self.xPos - self.radius

        pY1 = self.yPos + self.radius
        pY2 = self.yPos - self.radius
        
        # Object
        oX1 = object.p1[0]
        oX2 = object.p2[0]
        oX3 = object.p3[0]
        oX4 = object.p4[0]

        oY1 = object.p1[1]
        oY2 = object.p2[1]
        oY3 = object.p3[1]
        oY4 = object.p4[1]


        # Because the squares are straight we can determine that it onlöy need to check to lines

        # Just checking
        if object.p1[0] < object.p2[0]:
            # Up
            print()
            if pX1 > oX1 and pX1 > oX2 and pX1 > oX3 and pX1 > oX4:
                return False
            
            # Right
            if pY1 > oY1 and pY1 > oY2 and pY1 > oY3 and pY1 > oY4:
                return False
           
            # Down
            if pX2 < oX1 and pX2 < oX2 and pX2 < oX3 and pX2 < oX4:
                return False
            
            # Left
            if pY2 < oX2 and pY2 < oY2 and pY2 < oY3 and pY2 < oY4:
                return False
            
            else:
                time.sleep(1)
                

                print("coll", random.randint(1, 10))


    def drawCircle(self):
        pygame.draw.circle(wn, (0, 0, 0), (self.xPos, self.yPos), self.radius, self.width)
