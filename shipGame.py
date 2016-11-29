import pygame
from math import *
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
        self.centre[0] = int(self.time * self.velocity[0] + self.x0)
        self.centre[1] = int(self.y0 - self.velocity[1] * self.time + 0.5 * GRAVITY * self.time * self.time)
        self.draw()
        self.time += time_increment

    def collide(self, screen = False):  #to check whether collision with screen or collision with ships
        if self.centre[1] >= oceanY or self.centre[0] >= width: return True
        if screen: return
        rect1 = pygame.Rect(self.centre[0] - self.radius, self.centre[1] - self.radius, 2*self.radius, 2*self.radius)
        target_size = aip.image_size if self.target == 'aip' else enemy.image_size
        target_loc = aip.loc if self.target == 'aip' else enemy.loc
        target_rect = pygame.Rect(target_loc, target_size)
        return rect1.colliderect(target_rect)
            

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
    ID = 'enemy'
    hp = 100
    sunk = False

    def draw(self):
        if self.sunk: return
        self.gunTip[0] = int(self.gunBase[0] - self.gunLength * cos(radians(self.theta)))
        self.gunTip[1] = int(self.gunBase[1] - self.gunLength * sin(radians(self.theta)))
        pygame.draw.line(gameDisplay, black, self.gunTip, self.gunBase, self.gunWidth)
        gameDisplay.blit(self.image, self.loc)

    def __init__(self):
        #initialize all important constants
        self.image = pygame.transform.flip(self.image, True, False)
        self.image_size = self.image.get_size()
        self.theta = 45
        self.power = 50
        self.loc = [width - 50 - self.image_size[0], oceanY - self.image_size[1] + 15]
        self.gunBase = [self.loc[0] + 50, self.loc[1] + 4*self.image_size[1]//5 + 10]
        self.gunTip[0] = int(self.gunBase[0] - self.gunLength * cos(radians(self.theta)))
        self.gunTip[1] = int(self.gunBase[1] - self.gunLength * sin(radians(self.theta)))

aip = AIP_Boat()
enemy = EnemyShip()
projectile = [None, None]  #[aip's projectile, enemy projectile]

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
        keystate = pygame.key.get_pressed()
        aip.power += keystate[pygame.K_RIGHT] - keystate[pygame.K_LEFT]
        if aip.power >= MAXPOWER: aip.power = MAXPOWER
        elif aip.power <= 20: aip.power = 20
        aip.theta += keystate[pygame.K_UP] - keystate[pygame.K_DOWN]
        if aip.theta >= 80: aip.theta = 80
        elif aip.theta <= 20: aip.theta = 20
        
        gameDisplay.fill(white)
        
        if projectile[0] != None:
            projectile[0].move()
            if projectile[0].collide(screen = False):
                if enemy.loc[0] - projectile[0].radius <= projectile[0].centre[0] <= enemy.loc[0] + enemy.image_size[0]//3 + projectile[0].radius or \
                   enemy.loc[0] + 2*enemy.image_size[0]//3 - projectile[0].radius <= projectile[0].centre[0] <= enemy.loc[0] + enemy.image_size[0] + projectile[0].radius:
                    enemy.hp -= 20
                else:
                    enemy.hp -= 50
                if enemy.hp <= 0: enemy.sunk = True
                projectile[0] = None
            elif projectile[0].collide(screen = True):
                projectile[0] = None
    
        aip.draw()
        powerBars(aip)
        powerBars(enemy)
        enemy.draw()
        gameDisplay.blit(ocean, (-10, oceanY))
        pygame.display.update()
        clock.tick(25)

gameLoop()
                
