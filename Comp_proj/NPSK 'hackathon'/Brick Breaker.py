import pygame
from math import atan, cos, degrees, radians, sin, tan
pygame.init()

red = (255, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
black = (0, 0, 0)

width = 400
height = 500

pSize = 50
pX, pY = (width-pSize)//2 + 6, height - 25
pSpeed = 15
pDir = 0

bMoving = False
bR = 10
bX, bY = width//2 + 3, pY - bR
bDir = 90  #angle between velocity vector and +ve x axis in degrees
bSpeed = 15

numBlocks = 10
gameDisplay = pygame.display.set_mode((width, height))
size = width//2
block_size = size//numBlocks
pic_loc = (width//4, 80)
blocks = [[{'loc':(x*block_size + pic_loc[0], y*block_size + pic_loc[1]), 'broken':False} for y in range(numBlocks)]
          for x in range(numBlocks)]
clock = pygame.time.Clock()

def collide(obj, size): #collide ball with obj
    global bDir
    if not ((obj[0] - size//2 <= bX <= obj[0] + 3*size//2) and (obj[1] - size//2 <= bY <= obj[1] + 3*size//2)):
        return False
    flag = False
    if obj[0] <= bX <= obj[0] + size:
        if obj[1] <= bY - bR <= obj[1] + size:    #hit from bottom
            bDir = -bDir
            flag = True
        elif obj[1] + size >= bY + bR >= obj[1]:  #hit from top
            if 0 > tan(radians(bDir)):
                bDir =  -(bDir)
            else:
                bDir -= 90
            flag = True
    elif obj[1] <= bY <= obj[1] + size:
        if obj[0] <= bX - bR <= obj[0] + size:    #hit from right
            if 90 >= bDir >= 0:
                bDir = -bDir
            else:
                bDir = 180 - bDir
            flag = True
        elif obj[0] + size >= bX + bR >= obj[0]:  #hit from left
            bDir = 180 - bDir
            flag = True
    bDir = bDir % 360
    if 180 <= bDir <= 360:
        bDir -= 360
    return flag

def collide_platform():
    global bDir
    if not ((pX - pSize//2 <= bX <= pX + 3*pSize//2) and (pY <= bY + 2*bR)):
        return
    if pX <= bX <= pX + pSize:
        if bY + bR >= pY:  
            if 0 > tan(radians(bDir)):
                bDir =  -(bDir)
            else:
                bDir -= 90
        else:
            return
    else:
        return
    s = bSpeed * sin(radians(bDir))
    if pDir == 0: bDir = 90
    elif pDir < 0: bDir = 180 + degrees(atan(float(s)/float(pDir/3)))
    else: bDir = degrees(atan(float(s)/float(pDir/3)))
    
def moveBall():
    global bX, bY, bDir
    if not bMoving: #if ball not launched at start of the game
        bX = pX + pSize//2
        return
    #physics - velocity vectors and laws of reflections and shit 
    x_proj = bSpeed * cos(radians(bDir)) 
    y_proj = bSpeed * sin(radians(bDir))
    bX += int(x_proj)
    bY -= int(y_proj)
    collide_platform()
    for i in range(numBlocks):
        for j in range(numBlocks):
            if not blocks[i][j]['broken']:
                blocks[i][j]['broken'] = collide(blocks[i][j]['loc'], block_size)
    if bY <= bR: #hit top
        bDir = -bDir
    elif bY + bR > height:  #hit bottom
        pygame.quit()
        quit()
    elif bX <= bR:  #hit left 
        if 90 >= bDir >= 0:
            bDir = -bDir
        else:
            bDir = 180 - bDir
    elif bX + bR >= width:  #hit right wall
        bDir = 180 - bDir

pause = False

def gameloop():
    Gameon = True
    global pause, pX, pDir, bX, bY, bDir, bMoving
    while Gameon:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bMoving = True
                    if pDir == 0: bDir = 90
                    elif pDir < 0: bDir = 180 + degrees(atan(float(bSpeed)/float(pDir)))
                    else: bDir = degrees(atan(float(bSpeed)/float(pDir)))
                elif event.key == pygame.K_p: pause = not pause
        if pause: continue
        keystate = pygame.key.get_pressed()
        pDir = pSpeed * (keystate[pygame.K_RIGHT] - keystate[pygame.K_LEFT])
        pX += pDir
        moveBall()
        if pX <= 0: pX = pSpeed
        elif pX >= width - pSize: pX = width - pSize - pSpeed
        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay, red, (pic_loc[0], pic_loc[1], size, size))
        for row in blocks:
            for d in row:
                if d['broken']:
                    pygame.draw.rect(gameDisplay, white, (d['loc'][0], d['loc'][1], block_size, block_size))
        pygame.draw.circle(gameDisplay, black, (bX, bY), bR)
        pygame.draw.rect(gameDisplay, blue, (pX, pY, pSize, 5))
        pygame.display.update()
        clock.tick(20)


gameloop()   
