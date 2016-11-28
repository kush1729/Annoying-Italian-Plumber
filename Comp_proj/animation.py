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
walk1 = pygame.image.load("H:/Comp_proj/Images/AIP/walk1.png")
walk2 = pygame.image.load("H:/Comp_proj/Images/AIP/walk2.png")
walk3 = pygame.image.load("H:/Comp_proj/Images/AIP/walk3.png")
jumpright = pygame.image.load("H:/Comp_proj/Images/AIP/jump.png")
standright = pygame.image.load("H:/Comp_proj/Images/AIP/stand.png")
hitlerstomp = pygame.image.load("H:/Comp_proj/Images/AIP/hitlerstomp.png")
largedialogue = pygame.image.load("H:/Comp_proj/Images/AIP/largedialogue.png")
mediumdialogue = pygame.image.load("H:/Comp_proj/Images/AIP/mediumdialogue.png")
smalldialogue = pygame.image.load("H:/Comp_proj/Images/AIP/smalldialogue.png")

dialoguedict = {"Large" : largedialogue, "Medium":mediumdialogue, "Small":smalldialogue}



walk1left = pygame.transform.flip(walk1, True, False)
walk2left = pygame.transform.flip(walk2, True, False)
walk3left = pygame.transform.flip(walk3, True, False)
standleft = pygame.transform.flip(standright, True, False)
jumpleft = pygame.transform.flip(jumpright, True, False)


walklistright = [standright, walk1, walk2, walk3, jumpright]
walklistleft = [standleft, walk1left, walk2left, walk3left, jumpleft]

# Text sizes:
smallfont = pygame.font.SysFont("comicsansms", 15)
smallmedfont = pygame.font.SysFont("comicsansms", 30)
medfont = pygame.font.SysFont("comicsansms", 35)
mediumlargefont = pygame.font.SysFont("comicsansms", 60)
largefont = pygame.font.SysFont("comicsansms", 80)



width = 900
height = 600

gameDisplay = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
gameDisplay.fill(white)





def drawhitler(xposition, yposition, angle = 0):
    theimage = pygame.transform.rotate(hitlerstomp, angle)
    gameDisplay.blit(theimage, [xposition, yposition])


def dialoguebox(size, xposition, yposition, text, colour = black):
    
    theimage = dialoguedict[size]
    length = len(text)
    
    if size == "Large":
        gameDisplay.blit(theimage, [xposition - 50 ,yposition - 300])
        textsize = "medium"

        writing(text, colour, yposition - height/2 - 250, centre = False,
                requiredwidth = xposition + 70, size = textsize, timegap = 0.05, EOL = 8)
        

    elif size == "Medium":
        gameDisplay.blit(theimage, [xposition - 50 ,yposition - 300])
        textsize = "smallmed"

        writing(text, colour, yposition - height/2 - 250, centre = False,
                requiredwidth = xposition + 30, size = textsize, timegap = 0.05, EOL = 10)

                
    elif size == "Small":
        gameDisplay.blit(theimage, [xposition - 20 ,yposition - 200])
        textsize = "small"
        writing(text[0:9], colour, yposition - height/2 - 160, centre = False, requiredwidth = xposition + 80, size = textsize, timegap = 0.05 )
        writing(text[9:], colour, yposition - height/2 + 40 - 160, centre = False, requiredwidth = xposition + 30, size = textsize, timegap = 0.05 )


def writing(text, colour, ht = -100, size = "smallmed",
            centre = False, requiredwidth = 20, timegap = 0.1, EOL = None):
    numberofspaces = ""
    count = 0
    flag = False
    for letters in text:
        if EOL <> None:
            
            msgbox(numberofspaces + letters, colour, ht, size, centre, requiredwidth)
            pygame.display.update()
            numberofspaces += "     "
            count += 1
            if count % EOL == 0:
                flag = True
                
            if flag == True:
                if letters.isspace() == True or count % EOL > EOL - 4:
                
                    ht += 40
                    numberofspaces = ""
                    flag = False
                
            
            time.sleep(timegap)  

def msgbox(text, colour, ht=50, size = "small", centre = True, requiredwidth = 10):
    textsurf, textrect = text_objects(text, colour, size)
    if centre:
        textrect.center = (width/2), (height/2)+ ht
    else:
        textrect.center = requiredwidth, (height/2) + ht
    gameDisplay.blit(textsurf, textrect)


def text_button(msg, colour, buttonx, buttony, buttonwidth, buttonheight, size = "small"):
    textsurf, textrect = text_objects(msg, colour, size)
    textrect.center = ((buttonx+ (buttonwidth/ 2)), (buttony + (buttonheight/ 2)))
    gameDisplay.blit(textsurf, textrect)   


def text_objects(text, colour, size):
    if size == "small":
        textsurface = smallfont.render(text, True, colour)
    elif size == "medium":
        textsurface = medfont.render(text, True, colour)
    elif size == "large":
        textsurface = largefont.render(text, True, colour)
    elif size == "smallmed":
        textsurface = smallmedfont.render(text, True, colour)
    elif size == "mediumlarge":
        textsurface = mediumlargefont.render(text, True, colour)

                                
    return textsurface, textsurface.get_rect()

def drawman(xposition, yposition, imagenumber, direction = "Right"):
    if direction == "Right":
        theimage = walklistright[imagenumber]
    else:
        theimage = walklistleft[imagenumber]

    gameDisplay.blit(theimage, [xposition, yposition])
    

def gameintro():
    Intro = True
    gameDisplay.fill(white)
    xposition = -10
    groundheight = height/2
    yposition = groundheight
    fps = 20
    hitlerdone = False
    dialoguedone = mariodialoguedone = False
    Mario = False
    initialwidth = -100
    imagenumber = 0
    changewidth = 10
    while Intro:
        
        while initialwidth < width/2 and not Mario:
            
            clock.tick(15)
            changewidth = 10
            initialwidth += changewidth
            if imagenumber < len(walklistright) - 2:
                imagenumber += 1
            else:
                imagenumber = 1
            drawman(initialwidth, yposition, imagenumber, direction = "Right")
            pygame.display.update()
            gameDisplay.fill(white)

            
        else:
            Mario = True
            imagenumber = 0

        if Mario and not mariodialoguedone:
            drawman(initialwidth, yposition, imagenumber)
            dialoguebox("Medium", initialwidth, yposition, "I feel like I forgot something...")
            pygame.display.update()
            time.sleep(1)
            gameDisplay.fill(white)


            while initialwidth > width/3:
                clock.tick(15)
                changewidth = -10
                initialwidth += changewidth
                if imagenumber < len(walklistright) - 2:
                    imagenumber += 1
                else:
                    imagenumber = 1
                drawman(initialwidth, yposition, imagenumber, direction = "Left")
                pygame.display.update()
                gameDisplay.fill(white)

            imagenumber = 0    
            drawman(initialwidth, yposition, imagenumber, direction = "Left")
            dialoguebox("Medium", initialwidth, yposition, "I'm sure it was nothing important...")
            pygame.display.update()
            time.sleep(1)
            gameDisplay.fill(white)
            mariodialoguedone = True

        

        if not hitlerdone:
            if xposition <= width/2 - 130:
                xposition += 5
            else:
                hitlerdone = True
        


        drawhitler(xposition, yposition)

        if hitlerdone and dialoguedone == False:
            dialoguebox("Large", xposition, yposition, "ANNOYING ITALIAN PLUMBER!!!")
            dialoguedone = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update()
##        gameDisplay.fill(white)


gameintro()
        




