from Var import *
import math


class dragBall:
    def __init__(self, ballX, ballY, strengthX, strengthY):
        self.ballX = ballX
        self.ballY = ballY
        self.strengthX = strengthX
        self.strengthY = strengthY
        
        self.power = 0
        self.maxPower = 20


    def drag(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.ballX, self.ballY = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]

        if event.type == pygame.MOUSEBUTTONUP:
            mousePos = (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
            self.power = self.getPower(mousePos)
            return True

    def getPower(self, mousePos):
        pointA = mousePos
        pointB = (self.ballX, self.ballY)

        # First get length of kat
        lenKat1 = pointA[1] - pointB[1]
        lenKat2 = pointB[0] - pointA[0]
        
        powerX = lenKat2 / self.strengthX
        powerY = lenKat1 / self.strengthY
        if powerX > self.maxPower:
            powerX = self.maxPower
        if powerY > self.maxPower:
            powerY = self.maxPower
        if powerX < -self.maxPower:
            powerX = -self.maxPower
        if powerY < -self.maxPower:
            powerY = -self.maxPower

        return (powerX, powerY)

    '''
    def drawCircles(self, kat1, kat2):
        hyp = math.sqrt((kat1*kat1) + (kat2*kat2))
    
        numCircles = 20

        distanceCircl = hyp/numCircles

        for i in range(numCircles):
            center = i*distanceCircl 
            pygame.draw(wn, (0, 0, 0), ())
    '''
