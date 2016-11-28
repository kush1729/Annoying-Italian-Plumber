import pygame
pygame.init()

black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)

width, height = 600, 400
gameDisplay = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

tX, tY = width - 160, height//4
tWidth, tHeight = 150, 3*height//4
gameDisplay.fill(white)
pygame.draw.rect(gameDisplay, red, (tX, tY, tWidth, tHeight)) #tower
pygame.display.update()

gTurPos = 1

turretWidth = 15
x, y = 0, height 
possibleTurrets = [(x - 10*i + 100, y - 10*i - 10) for i in range(2, 9)]
print possibleTurrets

def tank(turPos):
    pygame.draw.line(gameDisplay, black, (0, height), possibleTurrets[turPos],
                     turretWidth)
    #return possibleTurrets[turPos]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                quit()
            elif event.key == pygame.K_DOWN:
                gTurPos -= 1
                if gTurPos <= 0: gTurPos = 0
                print gTurPos, ':', possibleTurrets[gTurPos]
            elif event.key == pygame.K_UP:
                gTurPos += 1
                if gTurPos >= len(possibleTurrets) - 1: gTurPos = len(possibleTurrets) - 1
                print gTurPos, ':', possibleTurrets[gTurPos]
    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, red, (tX, tY, tWidth, tHeight)) #tower
    tank(gTurPos)
    pygame.display.update()
    clock.tick(20)
