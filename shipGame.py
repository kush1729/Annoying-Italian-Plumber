import pygame
from math import *
pygame.init()

black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
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

class AIP_Boat:
    image = pygame.image.load('boat.png')
    mario_loc = [0, 0]
    mario_size = (50, 50)
    image_size = 0, 0
    gunWidth = 15
    gunLength = 75
    gunTip = [0, 0]
    ID = 'aip'

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

    def draw(self):
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
projectile = None

def gameLoop():
    global aip, projectile
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_SPACE:
                    if projectile == None:
                        projectile = Projectile(aip)
        keystate = pygame.key.get_pressed()
        aip.power += keystate[pygame.K_RIGHT] - keystate[pygame.K_LEFT]
        if aip.power >= MAXPOWER: aip.power = MAXPOWER
        elif aip.power <= 20: aip.power = 20
        aip.theta += keystate[pygame.K_UP] - keystate[pygame.K_DOWN]
        if aip.theta >= 80: aip.theta = 80
        elif aip.theta <= 20: aip.theta = 20
        
        gameDisplay.fill(white)
        
        if projectile != None:
            projectile.move()
            if projectile.collide(): projectile = None
    
        aip.draw()
        enemy.draw()
        gameDisplay.blit(ocean, (-10, oceanY))
        pygame.display.update()
        clock.tick(25)

gameLoop()
                
