import pygame
pygame.init()


# WN
wW, wH = 1000, 1000
wn = pygame.display.set_mode((wW, wH))

# Constants
mTime = 0.1
loopRange = 500
state = "normal"
spaceDown = False

# COLOR
playerColor = (10, 10, 0)
bgColor = (150, 170, 130)

# Positions
startX = wW/5
startY = wH/3

falling = False


# Lists
obstacles = []


# Pygame Vars
clock = pygame.time.Clock()


# Player Vars
startPlrXPos = 100
startPlrYPos = 400

startPlrRadius = 5
startPlrWidth = 3
startPlrColor = (50, 0, 0)

startPlrGravity = 0
startPlrVY = 0
startPlrVX = 0

startPlrBounceEff = 0.8


# Dragball
drgStrengthX = 10
drgStrengthY = drgStrengthX
