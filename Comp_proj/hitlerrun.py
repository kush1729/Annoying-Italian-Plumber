import pygame
import time
import random
pygame.init()



# Colours:
yellow = (234, 228, 34)
lightyellow = (255, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (155, 0, 0)
lightred = (255, 0, 0)
Darkblue = (0, 0, 155)
DarkGreen = (34, 177, 76)
brown = (118, 85, 73)
grey = (178, 178, 178)


#Images:
walk1 = pygame.image.load("C:/PythonX/Images/AIP/walk1.png")
walk2 = pygame.image.load("C:/PythonX/Images/AIP/walk2.png")
walk3 = pygame.image.load("C:/PythonX/Images/AIP/walk3.png")
jumpright = pygame.image.load("C:/PythonX/Images/AIP/jump.png")
standright = pygame.image.load("C:/PythonX/Images/AIP/stand.png")


walk1left = pygame.transform.flip(walk1, True, False)
walk2left = pygame.transform.flip(walk2, True, False)
walk3left = pygame.transform.flip(walk3, True, False)
standleft = pygame.transform.flip(standright, True, False)
jumpleft = pygame.transform.flip(jumpright, True, False)


walklistright = [standright, walk1, walk2, walk3, jumpright]
walklistleft = [standleft, walk1left, walk2left, walk3left, jumpleft]



width = 900
height = 600

gameDisplay = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
gameDisplay.fill(white)


def healthbar(phealth, xposition, yposition):
    if phealth > 75:
        phealth_colour = DarkGreen
    elif phealth > 50:
        phealth_colour = yellow
    else:
        phealth_colour = red


    pygame.draw.rect(gameDisplay, phealth_colour, (xposition + (phealth/4), yposition - 10, phealth/2, 10))



def drawman(xposition, yposition, imagenumber, direction = "Right"):
    if direction == "Right":
        theimage = walklistright[imagenumber]
    else:
        theimage = walklistleft[imagenumber]

    gameDisplay.blit(theimage, [xposition, yposition])


def randomobstacles():
    obstacleheight = random.randint(50, 100)
    obstaclewidth = random.randint(40, 100)
    return obstaclewidth, obstacleheight


def obstacles(xposition, yposition, obstaclewidth, obstacleheight, colour = black):
    pygame.draw.rect(gameDisplay, colour, [xposition, yposition, obstaclewidth, obstacleheight])
    
    


def gameloop():
    gameon = True
    imagenumber = 0
    xposition = 20
    yposition = height/2
    lastimage = len(walklistright) - 1
    direction = "Right"
    fps = 10
    goingup = True
    jumpheight = 100
    obstaclex = width
    groundheight = height/2
    newobstacle = True
    collisioncount = 0
    phealth = 100
    while gameon:
        clock.tick(fps)

        movement = pygame.key.get_pressed()



        
        if movement[pygame.K_RIGHT] and movement[pygame.K_UP]:
            xposition += 5
            direction = "Right"
            if obstaclex > 0:
                obstaclex -= 5
            else:
                newobstacle = True
                obstaclex = width

            
            

                
            if yposition <> groundheight:
                imagenumber = -1
            else:
                if imagenumber < lastimage - 1:
                    imagenumber += 1
                else:
                    imagenumber = 1
                
            if yposition <= groundheight - jumpheight or goingup == False:

                
                if yposition < groundheight - 10:
                    yposition += 20


                    
                else:
                    yposition = groundheight

                        
                goingup = False

                
            elif yposition > groundheight - jumpheight and goingup:
                yposition -= 20





        elif movement[pygame.K_LEFT] and movement[pygame.K_UP]:
            xposition -= 20

            
            if obstaclex > 0:
                obstaclex -= 1
            else:
                newobstacle = True
                obstaclex = width

            
            direction = "Left"
            if yposition <> groundheight:
                imagenumber = -1
            else:
                if imagenumber < lastimage - 1:
                    imagenumber += 1
                else:
                    imagenumber = 1
                
            if yposition <= groundheight - jumpheight or goingup == False:

                
                if yposition < groundheight - 10:
                    yposition += 20


                    
                else:
                    yposition = groundheight

                        
                goingup = False

                
            elif yposition > groundheight - jumpheight and goingup:
                yposition -= 20





            
        elif movement[pygame.K_RIGHT]:
            xposition += 5

            
            if obstaclex > 0:
                obstaclex -= 5
            else:
                newobstacle = True
                obstaclex = width

                
            if yposition <> groundheight:
                yposition = groundheight

                
            direction = "Right"
            if imagenumber < lastimage - 1:
                imagenumber += 1
            else:
                imagenumber = 1


                

        elif movement[pygame.K_LEFT]:

            xposition -= 20

            
            if obstaclex > 0:
                obstaclex -= 1
            else:
                newobstacle = True
                obstaclex = width
    
            direction = "Left"
            if yposition <> groundheight:
                yposition = groundheight

                
            if imagenumber < lastimage - 1:
                imagenumber += 1
            else:
                imagenumber = 1





                
        elif movement[pygame.K_UP]:
            if yposition <> groundheight:
                imagenumber = -1
            else:
                imagenumber = 0
##            goingup = True

            if yposition <= groundheight - jumpheight or goingup == False:

                
                if yposition < groundheight - 10:
                    yposition += 20


                    
                else:
                    yposition = groundheight

                        
                goingup = False
                
            elif yposition > groundheight - jumpheight and goingup:
                yposition -= 20

        

        else:
            imagenumber = 0
            yposition = groundheight
            xposition -= 10
            goingup = True
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            


                    
                    


                
        if newobstacle:
            obstaclewidth, obstacleheight = randomobstacles()
            print obstaclewidth, obstacleheight
            newobstacle = False

            
        obstacles(obstaclex, height/2 + 150 - obstacleheight, obstaclewidth, obstacleheight, black)


        if xposition + 75 >= obstaclex and xposition <= obstaclex + obstaclewidth - 20:
            groundheight = height/2 - obstacleheight
            if yposition <= groundheight:
                
                yposition = groundheight
        

                
            else:
                groundheight = height/2
                if phealth >= 5:
                    phealth -= 5
                else:
                    phealth = 0

        else:
            groundheight = height/2

        
        if obstaclex > 0:
            obstaclex -= 10
        else:
            newobstacle = True
            obstaclex = width

            
        drawman(xposition, yposition, imagenumber, direction)
        healthbar(phealth, xposition, yposition)
        gameDisplay.fill(black, rect = [0, height/2 + 148, width, height-(height/2 + 148)])

        pygame.display.update()
        gameDisplay.fill(white)

        if xposition < -100 or phealth <= 0:
            gameDisplay.fill(white)
            print "Game Over!"
            gameon = False
        
        

   
    
    
    


gameloop()
