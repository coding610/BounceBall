from Var import *

class obstaclePoly:
    def __init__(self, p1, p2, p3, p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4

    def drawObstacle(object):
        pygame.draw.polygon(wn, (0, 0, 0), [object.p1, object.p2, object.p3, object.p4])
