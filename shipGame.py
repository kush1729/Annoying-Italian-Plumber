import pygame
from math import *
from random import randint
pygame.init()

black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
brown = (139, 69, 19)

width, height = 1366, 768
gameDisplay = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
clock = pygame.time.Clock()

gameDisplay.fill(white)
pygame.display.update()

time_increment = 0.4

ocean = pygame.image.load('sea.png')
oceanY = height - 50

GRAVITY = 5
MAXPOWER = 90

class Projectile:
    radius = 15
    time = 0
    colour = blue
    value_dict = {'aip': -1, 'enemy':1}
    target = ''

    def draw(self):
        pygame.draw.circle(gameDisplay, self.colour, self.centre, self.radius)

    def __init__(self, ship):
        self.centre = ship.gunTip
        self.x0, self.y0 = self.centre
        self.target = 'aip' if ship.ID == 'enemy' else 'enemy'
        self.velocity = [ship.power*cos(radians(ship.theta)), ship.power*sin(radians(ship.theta))]
        self.time = 0

    def move(self):
        self.centre[0] = int(self.x0 + self.value_dict[self.target] * self.time * self.velocity[0])
        self.centre[1] = int(self.y0 - self.velocity[1] * self.time + 0.5 * GRAVITY * self.time * self.time)
        self.draw()
        self.time += time_increment

    def collide(self, screen = False):  #to check whether collision with screen or collision with ships
        if screen and (self.centre[1] >= oceanY or self.centre[0] >= width): return True
        if screen: return
        rect1 = pygame.Rect(self.centre[0] - self.radius, self.centre[1] - self.radius, 2*self.radius, 2*self.radius)
        target_size = aip.image_size if self.target == 'aip' else enemy.image_size
        target_loc = aip.loc if self.target == 'aip' else enemy.loc
        target_rect = pygame.Rect(target_loc, target_size)
        #calculate damage
        if rect1.colliderect(target_rect): #and oceanY >= self.centre[0] >= target_loc[1] + target_size[1]//3: try to not hit the transparent part of image
            dist = min(abs(target_loc[0] - self.centre[0]), abs(target_loc[0] + target_size[0] - self.centre[0]))
            damage = 1.5 * dist
            if damage >= 50: damage = 50
            return damage
        else:
            return False
            

def powerBars(obj):
    length = 100
    if obj.ID == 'aip': location = (5, 5)
    else: location = (width - length - 5, 5)
    if obj.hp >= 66: colour = green
    elif 66 > obj.hp >= 33: colour = yellow
    elif 33 > obj.hp: colour = red
    pygame.draw.rect(gameDisplay, black, (location[0], location[1], length, 10))
    if obj.sunk: return
    pygame.draw.rect(gameDisplay, colour, (location[0], location[1], obj.hp*length//100, 10))
    

class AIP_Boat:
    image = pygame.image.load('boat.png')
    mario_loc = [0, 0]
    mario_size = (50, 50)
    image_size = 0, 0
    gunWidth = 15
    gunLength = 75
    gunTip = [0, 0]
    ID = 'aip'
    hp = 100
    sunk = False

    def draw(self):
        #blit pic of mario, currently using ugly square (same thing)
        self.gunBase = [self.loc[0] + self.image_size[0]//2, self.loc[1] + self.image_size[1]//2]
        self.mario_loc = [self.loc[0] + self.mario_size[0]//2 + 15, self.loc[1] - self.mario_size[1]//2 + 15]
        self.gunTip[0] = int(self.gunBase[0] + self.gunLength * cos(radians(self.theta)))
        self.gunTip[1] = int(self.gunBase[1] - self.gunLength * sin(radians(self.theta)))
        x = int(self.gunBase[0] + self.gunLength * cos(radians(self.theta)) * self.power / float(MAXPOWER))
        y = int(self.gunBase[1] - self.gunLength * sin(radians(self.theta)) * self.power / float(MAXPOWER))
        pygame.draw.rect(gameDisplay, red,
                         (self.mario_loc[0] - self.mario_size[0]/2,
                          self.mario_loc[1] - self.mario_size[1]/2, self.mario_size[0], self.mario_size[1]))
        pygame.draw.line(gameDisplay, black, self.gunTip, self.gunBase, self.gunWidth)
        pygame.draw.line(gameDisplay, green, (x, y), self.gunBase, self.gunWidth)
        gameDisplay.blit(self.image, self.loc)

    def __init__(self):
        #initialize all important constants
        self.image_size = self.image.get_size()
        self.theta = 45
        self.power = 50
        self.loc = [50, oceanY - self.image_size[1]//2 + 10]
        self.gunBase = [self.loc[0] + self.image_size[0]//2, self.loc[1] + self.image_size[1]//2]
        self.gunTip[0] = int(self.gunBase[0] + self.gunLength * cos(radians(self.theta)))
        self.gunTip[1] = int(self.gunBase[1] - self.gunLength * sin(radians(self.theta)))

class EnemyShip:
    image = pygame.image.load('battleship.png')
    image_size = 0, 0
    gunWidth = 15
    gunLength = 75
    gunTip = [0, 0]
    power = 50
    ID = 'enemy'
    hp = 100
    sunk = False

    def draw(self):
        if self.sunk: return
        self.gunBase = [self.loc[0] + 50, self.loc[1] + 4*self.image_size[1]//5 + 10]
        self.gunTip[0] = int(self.gunBase[0] - self.gunLength * cos(radians(self.theta)))
        self.gunTip[1] = int(self.gunBase[1] - self.gunLength * sin(radians(self.theta)))
        pygame.draw.line(gameDisplay, black, self.gunTip, self.gunBase, self.gunWidth)
        gameDisplay.blit(self.image, self.loc)

    def __init__(self):
        #initialize all important constants
        self.image = pygame.transform.flip(self.image, True, False)
        self.image_size = self.image.get_size()
        self.theta = 45
        self.loc = [width - 50 - self.image_size[0], oceanY - self.image_size[1] + 15]
        self.gunBase = [self.loc[0] + 50, self.loc[1] + 4*self.image_size[1]//5 + 10]
        self.gunTip[0] = int(self.gunBase[0] - self.gunLength * cos(radians(self.theta)))
        self.gunTip[1] = int(self.gunBase[1] - self.gunLength * sin(radians(self.theta)))

    def shoot(self):
        global projectile
        if projectile == None: return
        vel_tot = randint(MAXPOWER//2, MAXPOWER - 15)
        distance = abs(aip.loc[0] + aip.image_size[0]//2 - self.gunTip[0]) + randint(-aip.image_size[0]//2, aip.image_size[0]//2)
        if distance >= (vel_tot ** 2)/float(GRAVITY):
            angle = 45
        else:
            angle = int(degrees(0.5 * asin(abs(float(distance) * float(GRAVITY) / float(vel_tot**2)))))
        while self.theta != angle:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and (event.key == pygame.K_q or event.key == pygame.K_ESCAPE):
                        pygame.quit()
                        quit()
            if angle > self.theta: self.theta += 1
            elif angle < self.theta: self.theta -= 1
            else: break
            drawAll(self)
            clock.tick(25)
        self.power = vel_tot
        projectile[1] = Projectile(self)

aip = AIP_Boat()
enemy = EnemyShip()
projectile = [None, None]  #[aip's projectile, enemy projectile]

def drawAll(self = None):
    gameDisplay.fill(white)
    aip.draw()
    powerBars(aip)
    if self == None: powerBars(enemy)
    else: powerBars(self)
    enemy.draw()
    for i in (0, 1):
        if projectile[i] != None: projectile[i].move()
    gameDisplay.blit(ocean, (-10, oceanY))
    pygame.display.update()

def gameLoop():
    global aip, projectile
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_SPACE:
                    if projectile[0] == None:
                        projectile[0] = Projectile(aip)
                    enemy.shoot()
        keystate = pygame.key.get_pressed()
        aip.power += keystate[pygame.K_RIGHT] - keystate[pygame.K_LEFT]
        if aip.power >= MAXPOWER: aip.power = MAXPOWER
        elif aip.power <= 20: aip.power = 20
        aip.theta += keystate[pygame.K_UP] - keystate[pygame.K_DOWN]
        if aip.theta >= 80: aip.theta = 80
        elif aip.theta <= 20: aip.theta = 20

        for i in (0, 1):
            if projectile[i] != None:
                damage = projectile[i].collide(screen = False)
                if damage != False and i == 0:
                    enemy.loc[0] += projectile[0].velocity[0]/MAXPOWER
                    enemy.hp -= damage
                    if enemy.hp <= 0: enemy.sunk = True
                    projectile[0] = None
                elif damage != False and i == 1:
                    aip.loc[0] -= projectile[1].velocity[0]/MAXPOWER
                    aip.hp -= damage
                    if aip.hp <= 0:
                        aip.sunk = True
                        print 'LOL YOU DEAD'
                        pygame.quit()
                        quit()
                    projectile[1] = None
                elif projectile[i].collide(screen = True):
                    projectile[i] = None
    
        drawAll()
        
        clock.tick(25)

gameLoop()
                
