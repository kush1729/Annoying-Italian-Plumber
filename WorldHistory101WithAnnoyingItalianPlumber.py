'''Look at synopsis document for intro to game
To know what the game is play it.

Define different regions by putting title in caps as a comment
End the region with another comment.
This way it is easier to figure out what shit does.

All levels in a class
Each level class object must have a function gameLoop(), in which the game loop runs if you haven't guessed already.
All other methods/attributes can be level specific.'''

import pygame
import time
import random
from math import *
pygame.init()

#COLOURS: (Refer to RGB dictionary)----------------------------------------------------------
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
darkgreen = (34, 139, 34)
yellow = (255, 255, 0)
gold = (255, 215, 0)
goldenrod = (218, 165, 32)
#--------------------------------------------------------------------------------------------
#Images:
# Right
walk1 = pygame.image.load("walk1.png")
walk2 = pygame.image.load("walk2.png")
walk3 = pygame.image.load("walk3.png")
jumpright = pygame.image.load("jump.png")
standright = pygame.image.load("stand.png")
duck = pygame.image.load("marioduck.png")


vorteximage = pygame.image.load("vortex.png")

sea = pygame.image.load("sea.png")
battleship1 = pygame.image.load("battleship.png")
boat = pygame.image.load("boat.png")
randomdude = pygame.image.load("standstraight.png")
smallstandright = pygame.image.load("smallmario.png")
smallduck = pygame.image.load("smallmarioduck.png")
smallstandleft = pygame.transform.flip(smallstandright, True, False)
battleship = pygame.transform.flip(battleship1, True, False)


opennote1 = pygame.image.load("opennote.png")
opennote2 = pygame.image.load("opennote2.png")
opennote3 = pygame.image.load("opennote3.png")
opennote4 = pygame.image.load("opennote4.png")
opennote5 = pygame.image.load("opennote5.png")
hitlerstomp = pygame.image.load("hitlerstomp.png")
fridgeclosedimage = pygame.image.load("fridgeclosed.png")
fridgeopenimage = pygame.image.load("fridgeopen.png")
largedialogue = pygame.image.load("largedialogue.png")
mediumdialogue = pygame.image.load("mediumdialogue.png")
smalldialogue = pygame.image.load("smalldialogue.png")
pipesimage = pygame.image.load("pipes.png")
hitler1 = pygame.image.load("hitler1.png")
destroyer = pygame.image.load("destroyer.png")
cave = pygame.image.load("cave.png")

# Early Man Images
earlyman = pygame.image.load("earlyman.png")
surprisedman = pygame.image.load("surprisedman.png")
evilman = pygame.image.load("evilearlyman.png")
dinowalk1 = pygame.image.load("dino1.png")
dinowalk2 = pygame.image.load("dino2.png")
dinostand = pygame.image.load("dinostand.png")
dinowalkleft1 = pygame.transform.flip(dinowalk1, True, False)
dinowalkleft2 = pygame.transform.flip(dinowalk2, True, False)
dinostandleft = pygame.transform.flip(dinostand, True, False)

# BrickBreaker images:
trump1 = pygame.image.load("trump1.png")
trumpfingerraise = pygame.image.load("trumpfingerraise.png")
podiumimage = pygame.image.load("podium.png")
trumpcheer = pygame.image.load("trumpcheer.png")
suspicioustrump = pygame.image.load("suspicioustrump.png")
trumpleft = pygame.transform.flip(trump1, True, False)





# Background images:
hitlerbackgroundimage = pygame.image.load("hitlerbackground.png")
genericbackground = pygame.image.load("genericbackground.png")
notebackground = pygame.image.load("note.png")
snowbackground = pygame.image.load("snowbackground.png")
snowholebackground = pygame.image.load("snowholebackground.png")
trumpbackground = pygame.image.load("trumpbackground.png")



# Left
walk1left = pygame.transform.flip(walk1, True, False)
walk2left = pygame.transform.flip(walk2, True, False)
walk3left = pygame.transform.flip(walk3, True, False)
standleft = pygame.transform.flip(standright, True, False)
jumpleft = pygame.transform.flip(jumpright, True, False)
leftduck = pygame.transform.flip(duck, True, False)



walklistright = [standright, walk1, walk2, walk3, jumpright, duck]
walklistleft = [standleft, walk1left, walk2left, walk3left, jumpleft, leftduck]
dinowalk = [dinowalkleft1, dinowalkleft2, dinostandleft]
dialoguedict = {"Large" : largedialogue, "Medium":mediumdialogue, "Small":smalldialogue}




#IMPORTANT CONSTANTS FOR AND DESIGN OF GAME DISPLAY------------------------------------------
display_width, display_height = 1000, 750
gameDisplay = pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)
gameDisplay.fill(white)
clock = pygame.time.Clock()
#--------------------------------------------------------------------------------------------

#TEXT AND BUTTON STUFF:  --------------------------------------------------------------------
# Font sizes:
smallfont = pygame.font.SysFont("comicsansms", 15)
smallmedfont = pygame.font.SysFont("comicsansms", 30)
medfont = pygame.font.SysFont("comicsansms", 35)
mediumlargefont = pygame.font.SysFont("comicsansms", 60)
largefont = pygame.font.SysFont("comicsansms", 80)



def button(text, x, y, width, height, inactiveColour, activeColour, action = None):
    #x, y is the coordinates of the top left corner of the button
    global lvl_no
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        if click[0] == 1 and action != None:
            #stuff the button has to do. action is a string which tells what function to run
            if action.lower() == "ready":
                return True
        pygame.draw.rect(gameDisplay, activeColour, (x, y, width, height))
    else:
        pygame.draw.rect(gameDisplay, inactiveColour, (x, y, width, height))
    text_to_button(text, black, x, y, width, height)
    
def text_objects(text, colour, size):
    font_dict = {'small':smallfont, 'medium':medfont, 'large':largefont, 'smallmed':smallmedfont, 'mediumlarge':mediumlargefont}
    #size is font size as an integer
    try:
        textSurface = font_dict[size].render(text, True, colour)
    except:
        textSurface = pygame.font.SysFont("comicsansms", size).render(text, True, colour)
    return textSurface, textSurface.get_rect()

def text_to_button(msg, color, btnx, btny, btnwidth, btnheight, size = "small"):
    textSurf , textRect = text_objects(msg, color, size)
    textRect.center = ((btnx + (btnwidth / 2)), (btny + (btnheight / 2)))
    gameDisplay.blit(textSurf, textRect)

def message_to_screen(msg, color, center_loc, size):
    textSurf , textRect = text_objects(msg, color, size)
    textRect.center = center_loc
    gameDisplay.blit(textSurf, textRect)
    return textRect

def writing(text, colour, (ht, requiredwidth), size = "smallmed", timegap = 0.1,  EOL = None):
    numberofspaces = ""
    font_dict = {'small':15, 'medium':35, 'large':80, 'smallmed':30, 'mediumlarge':60}
    try:
        textSurface = font_dict[size].render(text, True, colour)
    except:
        textSurface = pygame.font.SysFont("comicsansms", size).render(text, True, colour)
    
    count1 = count = 0
    flag = False
    length = len(text)
    
    try: h = font_dict[size] + 5
    except: h = size + 5

    for letters in range(length):
        if EOL <> None:
            count1 += 1
            if count1 % EOL == 0:
                flag = True   
            if flag == True:
                if text[letters].isspace() == True:
                    flag = False
                elif count1 % EOL >= 3:
                    theindex = letters
                    text = text[:theindex] + "- " + text[theindex:]
                    count1 = EOL + 1
                    flag = False

    

    for letters in text:
        if EOL <> None:
                        
            message_to_screen(numberofspaces + letters, colour, (requiredwidth, ht), size)
            pygame.display.update()
            numberofspaces += "     "
            count += 1
            if count % EOL == 0:
                flag = True

                
            if flag == True:
                if letters.isspace() == True:

                    ht += h
                    
                    numberofspaces = ""
                    flag = False
##                    
##                elif count % EOL == 3:
##                    

                
            
            time.sleep(timegap)


def fabulous(xposition, yposition, colourlist = [yellow, gold, goldenrod]):
    explode = True
    while explode:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        startpoint = (xposition, yposition)
        colourchoice = colourlist
        

        magnitude = 1
        while magnitude  < 300:
            explodingbitx = xposition + random.randrange(-1*magnitude,
                                                 magnitude)
            explodingbity = yposition + random.randrange(-3*magnitude, magnitude)
            pygame.draw.circle(gameDisplay, colourchoice[random.randrange(0, len(colourchoice))], (explodingbitx, explodingbity), random.randrange(5, 10))
            magnitude += 1
            pygame.display.update()
            clock.tick(100)

        explode = False


def dialoguebox(text, size, (xposition, yposition), timegap = 0.05, colour = black, textsize = None, EOL = None, imagechange = None):

    ## (text, colour, (ht, requiredwidth), size = "smallmed", timegap = 0.1,  EOL = None):
    if imagechange == None:
        theimage = dialoguedict[size]
    else:
        theimage = imagechange

    length = len(text)
    
    if size.lower() == "large":
        gameDisplay.blit(theimage, [xposition - 100 ,yposition - 350])
        if textsize == None:
            textsize = 35
        if EOL == None:
            EOL = 16
#(text, colour, (ht, requiredwidth), size = "smallmed", timegap = 0.1,  EOL = None)
        writing(text, colour, (yposition - 300, xposition - 50), size = textsize, timegap = timegap, EOL = EOL)
        

    elif size.lower() == "medium":
        gameDisplay.blit(theimage, [xposition - 90, yposition - 300])
        if textsize == None:
            textsize = 30
        if EOL == None:
            EOL = 13

        writing(text, colour, (yposition - 250, xposition - 30), size = textsize, timegap = timegap, EOL = EOL)

                
    elif size.lower() == "small":
        gameDisplay.blit(theimage, [xposition - 50 ,yposition - 140])
        if textsize == None:
            textsize = 15
        if EOL == None:
            EOL = 18
        writing(text, colour, (yposition - 90, xposition), size = textsize, timegap = timegap, EOL = EOL)
    
#---------------------------------------------------------------------------------------------

#DIFFERENT MENU SCREENS: ---------------------------------------------------------------------
def pause_screen():
    while True:
        gameDisplay.fill(white)
        message_to_screen('PAUSED', red, (display_width//2, display_height//5 + 25), display_height//5)
        message_to_screen('PRESS P TO CONTINUE', black, (display_width//2, 2*display_height//5), display_height//10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    return

        
def vortex(xwidth = 1500, yheight = 1500):
    
    
    for i in range(180):
        clock.tick(90)
        
        theimage = pygame.transform.rotate(vorteximage, i)
##        theimage.center = display_width/2, display_height/2
        secondimage = pygame.transform.rotate(walklistright[0], 2 * i)
        background([theimage, secondimage], [display_width/2 - 1500/2, display_width/2], [display_height/2 - 1500/2, display_height/2])
        pygame.display.update() 
                
#------------------------------------------------------------------------------------------
# INTRO ANIMATIONS:

def firstintro(stage = 1):
    # Changeables:
    backx = 0
    backy = 0
    global initmariox
    initmariox  = display_width/2
    
    
    floorheight = display_height/2 + 150
    notex = display_width/2 + 300
    notey = display_height/2 + 300
    
    

    if stage == 1:
        initmariox = -10
        finalmariox = display_width /2
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
    
        walk(initmariox, finalmariox, floorheight, walklistright, "Right", backgroundimagelist = [genericbackground, notebackground], backgroundx = [backx, notex], backgroundy = [backy, notey])
        pygame.display.update()
        initmariox = finalmariox
        dialoguebox("What a beautiful day!", "Medium", (initmariox, floorheight))
        pygame.display.update()
        time.sleep(0.5)
        gameDisplay.fill(white)
        
        walk(initmariox, notex - 100, floorheight, walklistright, "Right", backgroundimagelist = [genericbackground, notebackground], backgroundx = [backx, notex], backgroundy = [backy, notey])
        initmariox = notex - 100
        dialoguebox("Oh look, a note!", "Small", (initmariox, floorheight))
        pygame.display.update()
        time.sleep(0.5)
        gameDisplay.fill(white)

        background([genericbackground, walklistleft[0], opennote1], [backx, initmariox, 50], [backy, floorheight, 50])
        pygame.display.update()
        time.sleep(3)
        gameDisplay.fill(white)

        walk(initmariox, display_width/2, floorheight, walklistleft, "Left", backgroundimagelist = [genericbackground], backgroundx = [backx], backgroundy = [backy])
        initmariox = display_width/2
        pygame.display.update()
        time.sleep(0.3)
        
        background([genericbackground, walklistright[0]], [backx, initmariox], [backy, floorheight])
        dialoguebox("OK, first of all I'm not annoying...", "Medium", [initmariox, floorheight])
        time.sleep(1)
        gameDisplay.fill(white)
        background([genericbackground, walklistright[0]], [backx, initmariox], [backy, floorheight])
        dialoguebox("Second- NO ONE can control me!! Go ahead and do your worst", "Medium", [initmariox, floorheight])
        
        pygame.display.update()
        time.sleep(1)
        
        return

    
    elif stage == 2:
        background([genericbackground, walklistright[0], notebackground], [backx, initmariox, notex], [backy, floorheight, notey])
        dialoguebox("...", "Small", [initmariox, floorheight], timegap = 0.5, textsize = 30)
        pygame.display.update()
        time.sleep(0.5)
        gameDisplay.fill(white)
        time.sleep(0.5)
        background([genericbackground, walklistleft[0], notebackground], [backx, initmariox, notex], [backy, floorheight, notey])
        time.sleep(0.5)
        background([genericbackground, walklistright[0], notebackground], [backx, initmariox, notex], [backy, floorheight, notey])
        
        dialoguebox("I walked here on my own free will", "Small", [initmariox, floorheight])
        pygame.display.update()
        time.sleep(0.5)
        gameDisplay.fill(white)

        walk(initmariox, notex - 100, floorheight, walklistright, "Right", backgroundimagelist = [genericbackground, notebackground], backgroundx = [backx, notex], backgroundy = [backy, notey])
        initmariox = notex - 100
        
        dialoguebox("Oh look, there's another note!", "Small", (initmariox, floorheight))
        time.sleep(0.5)

        background([genericbackground, walklistleft[0], opennote2], [backx, initmariox, 50], [backy, floorheight, 50])
        pygame.display.update()
        time.sleep(3)
        gameDisplay.fill(white)

        background([genericbackground, walklistleft[0]], [backx, initmariox], [backy, floorheight])
        dialoguebox("Whoever writes these notes has some issues", "Small", [initmariox, floorheight])
        time.sleep(0.3)
        background([genericbackground, walklistright[0]], [backx, initmariox], [backy, floorheight])
        dialoguebox("There's no way in Bowser's Shell I'm jumping", "Small", [initmariox, floorheight])

        time.sleep(0.1)
        
        
        walk(initmariox, display_width/2, floorheight, walklistleft, direction = "Left", backgroundimagelist = [genericbackground], backgroundx = [backx], backgroundy = [backy])
        background([genericbackground, walklistright[0]], [0, display_width/2], [0, floorheight])
        
        return

    elif stage == 3:
        stage3 = True
        initmariox = display_width/2
        background([genericbackground, walklistright[0], notebackground], [backx, initmariox, notex], [backy, floorheight, notey])
        dialoguebox("PLEASE STOP! Stop controlling my bodily functions!", "Large", [initmariox, floorheight])
        time.sleep(0.5)
        background([genericbackground, walklistleft[0], notebackground], [backx, initmariox, notex], [backy, floorheight, notey])
        time.sleep(0.5)
        background([genericbackground, walklistright[0], notebackground], [backx, initmariox, notex], [backy, floorheight, notey])
        time.sleep(0.5)
        dialoguebox("No more notes please... what if this one asks you to press P?", "Large", [initmariox, floorheight], textsize = 35)
        time.sleep(0.5)
        background([genericbackground, walklistright[0], notebackground], [backx, initmariox, notex], [backy, floorheight, notey])
        time.sleep(0.5)
        dialoguebox("These are new pants...", "Small", [initmariox, floorheight])
        time.sleep(0.5)
        background([genericbackground, walklistright[0], notebackground], [backx, initmariox, notex], [backy, floorheight, notey])
        time.sleep(0.5)
        dialoguebox("Anyway the notes don't open unless I walk near them... and I'm NOT moving!", "Large", [initmariox, floorheight], textsize = 30)
        pygame.display.update()
        time.sleep(0.5)
        gameDisplay.fill(white)
        
        background([genericbackground, walklistright[0], notebackground], [backx, initmariox, notex], [backy, floorheight, notey])
        pygame.display.update()
        
        while stage3:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        stage3 = False


        walk(initmariox, notex - 100, floorheight, walklistright, "Right", backgroundimagelist = [genericbackground, notebackground], backgroundx = [backx, notex], backgroundy = [backy, notey])
        initmariox = notex - 100
        dialoguebox("NOOOOO!", "Small", [initmariox, floorheight])
        pygame.display.update()
        time.sleep(0.5)
        
        background([genericbackground, walklistleft[0], opennote3], [backx, initmariox, 50], [backy, floorheight, 50])
        
        pygame.display.update()
        time.sleep(3)

        walk(initmariox, display_width/2, floorheight, walklistleft, direction = "Left", backgroundimagelist = [genericbackground], backgroundx = [backx], backgroundy = [backy])
        pygame.display.update()
        return
    
    elif stage == 4:
        background([cave, walklistright[0], notebackground], [backx, initmariox, notex], [backy, floorheight, notey])
        dialoguebox("That cave looks too creepy, let's go the other way", "Medium", [initmariox, floorheight])
        pygame.display.update()
        time.sleep(0.1)
        walk(initmariox, 0, floorheight, walklistleft, "LEft", backgroundimagelist = [cave, notebackground], backgroundx = [backx, notex], backgroundy = [backy, notey])
        time.sleep(0.1)
        initmariox = 0
        background([cave, walklistright[0], notebackground], [backx, initmariox, notex], [backy, floorheight, notey])
        time.sleep(0.5)
        walk(initmariox, display_width/2, floorheight, walklistright, "Right", backgroundimagelist = [cave, notebackground], backgroundx = [backx, notex], backgroundy = [backy, notey])
        initmariox = display_width/2
        time.sleep(0.1)
        dialoguebox("Great work! We're stuck here now...", "Small", [initmariox, floorheight])
        pygame.display.update()
        time.sleep(1)
        dialoguebox("Ah what the heck...", "Small", [initmariox, floorheight])
 
        walk(initmariox, notex - 150, floorheight, walklistright, "RIght", backgroundimagelist = [cave, notebackground], backgroundx = [backx, notex], backgroundy = [backy, notey])
        pygame.display.update()
        time.sleep(0.8)
        initmariox = notex - 150
        background([cave, walklistleft[0], opennote4], [backx, initmariox, 50], [backy, floorheight, 50])
        pygame.display.update()
        time.sleep(3)
        background([cave, walklistright[0], notebackground], [backx, initmariox, notex], [backy, floorheight, notey])
        
        dialoguebox("Nu-uh, we aren't doing that... It's too dangerous!", "Medium", [initmariox, floorheight])
        background([cave, walklistleft[0], opennote4], [backx, initmariox, notex], [backy, floorheight, notey])
        backx, backy = 50, 50
        while backy + display_height - 100 > 0:
            clock.tick(20)
            
            background([cave, opennote4], [0, backx], [0, backy])
            pygame.display.update()
            background([cave, opennote5], [0, backx], [0 + display_height, backy + display_height - 100])
            backy -= 50
            pygame.display.update()
        time.sleep(3)
        
        walk(initmariox, display_width - 110, floorheight, walklistright, "Right", fps = 30, backgroundimagelist = [cave], backgroundx = [0], backgroundy = [0])
        background([cave], [0], [0])
        dialoguebox("Yikes it's slippery!", "Small", [display_width - 120, floorheight])
        pygame.display.update()
        time.sleep(1)
        gameDisplay.fill(white)
        background([cave], [0], [0])
        dialoguebox("AAAAAARRRRGGGGH!", "Medium", [display_width - 120, floorheight])
        pygame.display.update()
        time.sleep(0.5)
        vortex()
        launchgame()
   

def hitlerrun():
    # Changeables:
    floorheight = display_height/2 + 100
    fridgex, fridgey, pipex, pipey = 250, floorheight - 100, display_width - 230, floorheight - 200
    # -----------------------------

    
    walk(0, pipex - 160, floorheight, walklistright, "right", backgroundimagelist = [hitlerbackgroundimage, fridgeclosedimage, pipesimage], backgroundx = [0, fridgex, pipex], backgroundy = [0, fridgey, pipey])
    dialoguebox("There... all done with these pipes", "Medium", (display_width/2, floorheight))
    time.sleep(1)
    gameDisplay.fill(white)

    walk(pipex - 160, fridgex + 150, floorheight, walklistleft, "left", backgroundimagelist = [hitlerbackgroundimage, fridgeclosedimage, pipesimage], backgroundx = [0, fridgex, pipex], backgroundy = [0, fridgey, pipey])
    
    pygame.display.update()
    time.sleep(0.2)
    gameDisplay.blit(walklistleft[0], [fridgex + 150, floorheight])
    dialoguebox("!!!", "Small", (fridgex + 150, floorheight - 50), textsize = 30)
##            dialoguebox("!!", "Small", (200, display_height/2), textsize = 35)
    pygame.display.update()
    time.sleep(1)
    # Reached Fridge
    gameDisplay.fill(white)
    background([hitlerbackgroundimage, fridgeclosedimage, pipesimage, walklistleft[0]], [0, fridgex, pipex, fridgex + 150], [0, fridgey, pipey, floorheight])
##            gameDisplay.blit(walklistleft[0], [200, floorheight])
    # Looked Left
    pygame.display.update()
    time.sleep(1)
    gameDisplay.fill(white)
    background([hitlerbackgroundimage, fridgeclosedimage, pipesimage, walklistright[0]], [0, fridgex, pipex, fridgex + 150], [0, fridgey, pipey, floorheight])
##            gameDisplay.blit(walklistright[0], [200, floorheight])
    pygame.display.update()
    # Looked Right
    time.sleep(1)
    # Looked left again
    gameDisplay.fill(white)
    background([hitlerbackgroundimage, fridgeclosedimage, pipesimage, walklistleft[0]], [0, fridgex, pipex, fridgex + 150], [0, fridgey, pipey, floorheight])
##            gameDisplay.blit(walklistleft[0], [200, floorheight])
    pygame.display.update()
    time.sleep(1)
    
    gameDisplay.fill(white)
    background([hitlerbackgroundimage, fridgeopenimage, pipesimage, walklistleft[0]], [0, fridgex, pipex, fridgex + 150], [0, fridgey, pipey, floorheight])
##            gameDisplay.blit(walklistleft[0], [200, floorheight])
    pygame.display.update()
    time.sleep(1)

    walk(-(fridgex - 150), fridgex - 150, floorheight - 50, [None, hitlerstomp, None], "Right", backgroundimagelist = [hitlerbackgroundimage, fridgeopenimage, pipesimage, walklistleft[0]], backgroundx = [0, fridgex, pipex, fridgex + 150], backgroundy = [0, fridgey, pipey, floorheight])

    background([hitlerbackgroundimage, fridgeopenimage, pipesimage, walklistleft[0], hitlerstomp], [0, fridgex, pipex, fridgex + 150, fridgex - 150], [0, fridgey, pipey, floorheight, floorheight-50])
    pygame.display.update()
    time.sleep(0.5)
    gameDisplay.fill(white)
    

    background([hitlerbackgroundimage, fridgeopenimage, pipesimage, walklistleft[0], hitlerstomp], [0, fridgex, pipex, fridgex + 150, fridgex - 150], [0, fridgey, pipey, floorheight, floorheight - 50])
    dialoguebox("Oh... shi-", "Small", (fridgex + 150, floorheight))
    time.sleep(0.01)
    gameDisplay.fill(white)
    
    background([hitlerbackgroundimage, fridgeopenimage, pipesimage, walklistleft[0], hitlerstomp], [0, fridgex, pipex, fridgex + 150, fridgex - 150], [0, fridgey, pipey, floorheight, floorheight - 50])
    dialoguebox("VOT DOO YOO ZINK YOO ARE DOINK?!", "Medium", (fridgex - 150, floorheight - 50))
    
    pygame.display.update()
    time.sleep(0.5)
    gameDisplay.fill(white)

    background([hitlerbackgroundimage, fridgeopenimage, pipesimage, walklistleft[0], hitlerstomp], [0, fridgex, pipex, fridgex + 150, fridgex - 150], [0, fridgey, pipey, floorheight, floorheight - 50])

    dialoguebox("I- I -I just wanted some juice...", "Small", (fridgex + 150, floorheight))
    
    pygame.display.update()
    time.sleep(0.01)
    gameDisplay.fill(white)
    


    
    background([hitlerbackgroundimage, fridgeopenimage, pipesimage, walklistleft[0], hitlerstomp], [0, fridgex, pipex, fridgex + 150, fridgex - 150], [0, fridgey, pipey, floorheight, floorheight - 50])

    dialoguebox("YOO VANTED SOME VOT?!?!", "Medium", (fridgex - 150, floorheight - 50))
    
    pygame.display.update()
    time.sleep(1)
    gameDisplay.fill(white)
    

    background([hitlerbackgroundimage, fridgeopenimage, pipesimage, walklistleft[0], hitlerstomp], [0, fridgex, pipex, fridgex + 150, fridgex - 150], [0, fridgey, pipey, floorheight, floorheight- 50])

    dialoguebox("I'm sorry... I just really like juice!", "Small", (fridgex + 150, floorheight))

    pygame.display.update()
    time.sleep(1)
    gameDisplay.fill(white)
    

    background([hitlerbackgroundimage, fridgeopenimage, pipesimage, walklistleft[0], hitlerstomp], [0, fridgex, pipex, fridgex + 150, fridgex - 150], [0, fridgey, pipey, floorheight, floorheight - 50])

    dialoguebox("YOO LIKE JOOS?!?!", "Small", (fridgex - 150, floorheight - 50))
    
    pygame.display.update()
    time.sleep(1)
    gameDisplay.fill(white)
    

    
    
    background([hitlerbackgroundimage, fridgeopenimage, pipesimage, walklistright[0], hitlerstomp], [0, fridgex, pipex, fridgex + 150, fridgex - 150], [0, fridgey, pipey, floorheight, floorheight - 50])

    dialoguebox("Uh-Oh", "Small", (fridgex + 150, floorheight))
    pygame.display.update()
    time.sleep(0.01)
    gameDisplay.fill(white)
    

    
   # background([hitlerbackgroundimage, fridgeopenimage, pipesimage, walklistright[0], hitlerstomp], [0, fridgex, pipex, fridgex + 150, fridgex - 150], [0, fridgey, pipey, floorheight, floorheight])
    # walk(initx, finx, yposition, imagelist, direction, changewidth = 10, fps = 15, backgroundimagelist = None, backgroundx = None, backgroundy = None)
    
    walk(fridgex + 150, pipex - 160, floorheight, walklistright, "Right", fps = 20, backgroundimagelist = [hitlerbackgroundimage, fridgeopenimage, pipesimage, hitlerstomp], backgroundx = [0, fridgex, pipex, fridgex - 150], backgroundy = [0, fridgey, pipey, floorheight - 50])
    gameDisplay.fill(white)
    
    walk(fridgex - 150, fridgex, floorheight - 50, [None, hitlerstomp, None], "Right", backgroundimagelist = [hitlerbackgroundimage, fridgeopenimage, pipesimage, walklistleft[0]], backgroundx = [0, fridgex, pipex, pipex - 160], backgroundy = [0, fridgey, pipey, floorheight])
    
    pygame.display.update()
    gameDisplay.fill(white)
    

    background([hitlerbackgroundimage, fridgeopenimage, pipesimage, walklistleft[0], hitler1], [0, fridgex, pipex, pipex-160, fridgex], [0, fridgey, pipey, floorheight, floorheight - 75])
    dialoguebox("HITLER TRANSFORM! Unhhhh!", "Medium", (fridgex + 150, floorheight - 75))
    fabulous(fridgex + 130, floorheight - 75)
    pygame.display.update()
    time.sleep(1)
    gameDisplay.fill(white)
    
    
    background([hitlerbackgroundimage, fridgeopenimage, pipesimage, walklistright[0], destroyer], [0, fridgex, pipex, pipex-160, fridgex - 50], [0, fridgey, pipey, floorheight, floorheight - 400])         
    pygame.display.update()
    time.sleep(1)
    gameDisplay.fill(white)
    background([hitlerbackgroundimage, fridgeopenimage, pipesimage, walklistright[0], destroyer], [0, fridgex, pipex, pipex-160, fridgex - 50], [0, fridgey, pipey, floorheight, floorheight - 400])
    dialoguebox("Let's a GOOOO!", "Medium", (pipex - 160, floorheight))
    
    pygame.display.update()
    time.sleep(1)
    gameDisplay.fill(white)

    walk(pipex - 160, display_width + 50, floorheight, walklistright, "Right", changewidth = 10, fps = 30, backgroundimagelist = [hitlerbackgroundimage, fridgeopenimage, pipesimage, destroyer], backgroundx = [0, fridgex, pipex, fridgex - 50], backgroundy = [0, fridgey, pipey, floorheight - 400])
    
    pygame.display.update()
    gameDisplay.fill(white)

    walk(fridgex - 50, display_width + 300, floorheight - 400, [None, destroyer, None], "Right", changewidth = 20, fps = 30, backgroundimagelist = [hitlerbackgroundimage, fridgeopenimage, pipesimage], backgroundx = [0, fridgex, pipex], backgroundy = [0, fridgey, pipey])
    pygame.display.update()
    time.sleep(1)

    
    gameDisplay.fill(white)
    hitlerrun()

def launchgame():
    # Changeables:
    seayposition = display_height - 50
    seaxposition = 0
    boatx = 100
    battleshipx = display_width - 300

    boatsize = boat.get_size()
    battleshipsize = battleship.get_size()
    boaty = seayposition - boatsize[1] + 25
    battleshipy = seayposition - battleshipsize[1] + 15
    


    # --------------------------------
    background([randomdude, boat, sea], [boatx + 10, boatx, seaxposition], [boaty - 50, boaty, seayposition])
    pygame.display.update()
    time.sleep(0.5)
    walk(display_width + 30, battleshipx, battleshipy, [None, battleship, None, None], direction = "Left", changewidth = 5, backgroundimagelist = [randomdude, boat, sea], backgroundx = [boatx + 10, boatx, seaxposition], backgroundy = [boaty - 50, boaty, seayposition]) 
    pygame.display.update()
    background([randomdude, boat, battleship, sea], [boatx + 10, boatx, battleshipx, seaxposition], [boaty - 50, boaty, battleshipy, seayposition])
    pygame.display.update()
    time.sleep(0.5)
    
    dialoguebox("El Draco, we, the Spanish, WILL invade England!", "Medium", [battleshipx - 130, battleshipy])
    pygame.display.update()
    gameDisplay.fill(white)
    time.sleep(1)
    background([randomdude, boat, battleship, sea], [boatx + 10, boatx, battleshipx, seaxposition], [boaty - 50, boaty, battleshipy, seayposition])
    dialoguebox("Surrender if you value your life!!", "Medium", [battleshipx - 130, battleshipy])
    pygame.display.update()
    gameDisplay.fill(white)
    time.sleep(2)
    background([randomdude, boat, battleship, sea], [boatx + 10, boatx, battleshipx, seaxposition], [boaty - 50, boaty, battleshipy, seayposition])
    dialoguebox("NEVER! You will have to kill me!!", "Medium", [boatx + 10, boaty - 50])
    pygame.display.update()
    gameDisplay.fill(white)
    time.sleep(0.5)
    background([randomdude, boat, battleship, sea], [boatx + 10, boatx, battleshipx, seaxposition], [boaty - 50, boaty, battleshipy, seayposition])
    dialoguebox("I will never surrender!!", "Medium", [boatx + 10, boaty - 50])
    pygame.display.update()
    gameDisplay.fill(white)
    time.sleep(0.5)
    background([randomdude, boat, battleship, sea], [boatx + 10, boatx, battleshipx, seaxposition], [boaty - 50, boaty, battleshipy, seayposition])
    dialoguebox("I fight for freedom and justice and no one can ever crush me!!", "Large", [boatx + 10, boaty - 50], textsize = 30, EOL = 16)
    pygame.display.update()
    gameDisplay.fill(white)
    time.sleep(0.5)
    marioheight = 0
    while marioheight < boaty:
        clock.tick(20)
        
        
        theimage = pygame.transform.rotate(smallduck, marioheight)
        if marioheight <= boaty-50:
            background([randomdude, theimage, boat, battleship, sea], [boatx + 10, boatx + 10, boatx, battleshipx, seaxposition], [boaty - 50, marioheight, boaty, battleshipy, seayposition])
        else:
            background([theimage, boat, battleship, sea], [boatx + 10, boatx, battleshipx, seaxposition], [marioheight, boaty, battleshipy, seayposition])

        pygame.display.update()
##        time.sleep(1)
        gameDisplay.fill(white)
        if marioheight + 20 <= boaty:
            marioheight += 20
        else:
            marioheight = boaty

    theimage = pygame.transform.rotate(smallduck, 270)
    background([theimage, boat, battleship, sea], [boatx + 10, boatx, battleshipx, seaxposition], [boaty - 5, boaty, battleshipy, seayposition])
    pygame.display.update()
    gameDisplay.fill(white)
    time.sleep(1.5)

    background([smallstandright, boat, battleship, sea], [boatx + 10, boatx, battleshipx, seaxposition], [boaty - 50, boaty, battleshipy, seayposition])
    pygame.display.update()
    gameDisplay.fill(white)
    time.sleep(0.5)
    
    background([smallstandleft, boat, battleship, sea], [boatx + 10, boatx, battleshipx, seaxposition], [boaty - 50, boaty, battleshipy, seayposition])
    dialoguebox("It's a me a Ma-", "Small", [boatx + 10, boaty - 50 ])
    pygame.display.update()
    gameDisplay.fill(white)
    time.sleep(0.1)
          
    background([smallstandright, boat, battleship, sea], [boatx + 10, boatx, battleshipx, seaxposition], [boaty - 50, boaty, battleshipy, seayposition])
    dialoguebox("Uhhh, where am I?", "Small", [boatx + 10, boaty - 50 ])
    pygame.display.update()
    gameDisplay.fill(white)
    time.sleep(0.5)
    background([smallstandleft, boat, battleship, sea], [boatx + 10, boatx, battleshipx, seaxposition], [boaty - 50, boaty, battleshipy, seayposition])
    pygame.display.update()
    gameDisplay.fill(white)
    time.sleep(1)
    background([smallstandright, boat, battleship, sea], [boatx + 10, boatx, battleshipx, seaxposition], [boaty - 50, boaty, battleshipy, seayposition])
    pygame.display.update()
    gameDisplay.fill(white)
    time.sleep(0.5)
    background([smallstandright, boat, battleship, sea], [boatx + 10, boatx, battleshipx, seaxposition], [boaty - 50, boaty, battleshipy, seayposition])

    dialoguebox("OH NOOO!", "Medium", [boatx + 10, boaty])
    pygame.display.update()
    time.sleep(3)


    hitlerrun()



def iceage():
    # Changeables:
    backx, backy = 0, 0
    earlymanx = 100
    floorheight = display_height/2 + 100
    mariox = display_width/2 + 100
    jumpheight = 80
    


    
    background([snowbackground, earlyman], [backx, earlymanx], [backy, floorheight])
    dialoguebox("GRRAAAHHH! Hurk cold!", "Medium", [earlymanx, floorheight])
    pygame.display.update()
    time.sleep(1)
    gameDisplay.fill(white)
    background([snowbackground, earlyman], [backx, earlymanx], [backy, floorheight])
    dialoguebox("Hurk want FIRE !!!", "Medium", [earlymanx, floorheight])
    pygame.display.update()
    time.sleep(1)
    gameDisplay.fill(white)
    marioheight = 0



    while marioheight < floorheight:
        clock.tick(20)
        
        
        theimage = pygame.transform.rotate(duck, marioheight)
        if marioheight <= floorheight-50:
            background([snowbackground, earlyman, theimage], [backx, earlymanx, mariox], [backy, floorheight, marioheight])
        else:
            background([snowholebackground, surprisedman], [backx, earlymanx], [backy, floorheight])
        pygame.display.update()

        gameDisplay.fill(white)
        if marioheight + 20 <= floorheight:
            marioheight += 20
        else:
            marioheight = floorheight

    background([snowholebackground, surprisedman], [backx, earlymanx], [backy, floorheight])
    pygame.display.update()
    time.sleep(2.5)

    marioheight = floorheight + 30
    while marioheight > floorheight - jumpheight:
        clock.tick(20)
        theimage = walklistleft[len(walklistleft) - 2]
        if marioheight > floorheight:
            background([snowholebackground, surprisedman], [backx, earlymanx], [backy, floorheight])
        else:
            background([snowholebackground, surprisedman, theimage], [backx, earlymanx, mariox], [backy, floorheight, marioheight])
        pygame.display.update()
        gameDisplay.fill(white)
        marioheight -= 10

    time.sleep(0.3)

    while marioheight < floorheight + 40:
        clock.tick(20)
        theimage = walklistleft[len(walklistleft) - 2]
        
        background([snowholebackground, surprisedman, theimage], [backx, earlymanx, mariox], [backy, floorheight, marioheight])
        pygame.display.update()
        gameDisplay.fill(white)
        if marioheight + 10 <= floorheight + 40:
            marioheight += 10
        else:
            marioheight = floorheight + 40
    
    background([snowholebackground, surprisedman, walklistleft[0]], [backx, earlymanx, mariox], [backy, floorheight, marioheight])
    pygame.display.update()
    time.sleep(1)
    dialoguebox("It's a me a Ma-... sorry force of habit...", "Medium", [mariox, marioheight])
    pygame.display.update()
    gameDisplay.fill(white)
    time.sleep(0.1)
    background([snowholebackground, surprisedman, walklistleft[0]], [backx, earlymanx, mariox], [backy, floorheight, marioheight])
    dialoguebox("Who- No what the hell are you?", "Medium", [mariox, floorheight])
    pygame.display.update()
    gameDisplay.fill(white)
    time.sleep(0.5)
    background([snowholebackground, surprisedman, walklistleft[0]], [backx, earlymanx, mariox], [backy, floorheight, marioheight])
    dialoguebox("Huuurrrkkkk....", "Medium", [earlymanx, floorheight])
    pygame.display.update()
    gameDisplay.fill(white)
    time.sleep(0.5)
    background([snowholebackground, surprisedman, walklistleft[0]], [backx, earlymanx, mariox], [backy, floorheight, marioheight])
    dialoguebox("Hi Hurk, nice to meet you, I'm Ma-", "Medium", [mariox, marioheight])
    pygame.display.update()
    gameDisplay.fill(white)
    time.sleep(0.1)
    background([snowholebackground, evilman, walklistleft[0]], [backx, earlymanx, mariox], [backy, floorheight, marioheight])
    dialoguebox("....hungry", "Medium", [earlymanx, floorheight])
    pygame.display.update()
    gameDisplay.fill(white)
    time.sleep(0.2)
    background([snowholebackground, evilman, walklistleft[0]], [backx, earlymanx, mariox], [backy, floorheight, marioheight])
    dialoguebox("Okay not nice to meet you...", "Medium", [mariox, marioheight])
    pygame.display.update()
    gameDisplay.fill(white)
    time.sleep(0.5)

    walk(mariox, mariox + 75, marioheight, walklistright, "Right", backgroundimagelist = [snowholebackground, evilman], backgroundx = [backx, earlymanx], backgroundy = [backy, floorheight])
    pygame.display.update()
    mariox += 75
    background([snowholebackground, evilman, walklistleft[0]], [backx, earlymanx, mariox], [backy, floorheight, marioheight])
    pygame.display.update()
    gameDisplay.fill(white)
    walk(earlymanx, earlymanx + 50, floorheight, [None, evilman, None, None], "Right", changewidth = 25, backgroundimagelist = [snowholebackground, walklistleft[0]], backgroundx = [backx, mariox], backgroundy = [backy, marioheight])
    earlymanx += 50
    background([snowholebackground, evilman, walklistleft[0]], [backx, earlymanx, mariox], [backy, floorheight, marioheight])
    pygame.display.update()
    gameDisplay.fill(white)
    time.sleep(1)
    background([snowholebackground, evilman, walklistleft[0]], [backx, earlymanx, mariox], [backy, floorheight, marioheight])
    dialoguebox("C'mon old boy he's a neanderthal, you can outsmart him...", "Small", [mariox, marioheight])
    pygame.display.update()
    gameDisplay.fill(white)
    time.sleep(0.2)

    background([snowholebackground, evilman, walklistleft[0]], [backx, earlymanx, mariox], [backy, floorheight, marioheight])
    dialoguebox("Ah! I know! He'll fall for the easiest trick in the book... coz the book's not been written yet!", "Large", [mariox - 60, marioheight])
    pygame.display.update()
    gameDisplay.fill(white)
    time.sleep(0.2)

    background([snowholebackground, evilman, walklistleft[0]], [backx, earlymanx, mariox], [backy, floorheight, marioheight])
    dialoguebox("Oh Hurk look behind me!", "Medium", [mariox, marioheight])
    pygame.display.update()
    gameDisplay.fill(white)
    time.sleep(0.2)

    background([snowholebackground, evilman, walklistright[0]], [backx, earlymanx, mariox], [backy, floorheight, marioheight])
    pygame.display.update()
    time.sleep(0.5)
    walk(earlymanx, mariox - 200, floorheight, [None, evilman, None, None], 'Right', changewidth = 30,  backgroundimagelist = [snowholebackground, walklistright[0]], backgroundx = [backx, mariox], backgroundy = [backy, marioheight]) 
    earlymanx = mariox - 200
    background([snowholebackground, evilman, walklistleft[0]], [backx, earlymanx, mariox], [backy, floorheight, marioheight])
    pygame.display.update()
    gameDisplay.fill(white)
    
    
    background([snowholebackground, evilman, walklistleft[0]], [backx, earlymanx, mariox], [backy, floorheight, marioheight])
    dialoguebox("Damn it!", "Small", [mariox, marioheight])
    pygame.display.update()
    gameDisplay.fill(white)
    time.sleep(0.5)

    background([snowholebackground, evilman, walklistleft[0]], [backx, earlymanx, mariox], [backy, floorheight, marioheight])
    dialoguebox("Awesome... I've fallen from the pan to the fire...", "Medium", [mariox, marioheight])
    pygame.display.update()
    gameDisplay.fill(white)
    time.sleep(0.1)

    background([snowholebackground, surprisedman, walklistleft[0]], [backx, earlymanx, mariox], [backy, floorheight, marioheight])
    dialoguebox("F-f-fire?", "Small", [earlymanx, floorheight])
    pygame.display.update()
    gameDisplay.fill(white)
    time.sleep(0.5)

    background([snowholebackground, surprisedman, walklistleft[0]], [backx, earlymanx, mariox], [backy, floorheight, marioheight])
    dialoguebox("YES! FIRE! YES! I can get you fire!", "Medium", [mariox, marioheight])
    pygame.display.update()
    gameDisplay.fill(white)
    time.sleep(0.5)

    background([snowholebackground, earlyman, walklistleft[0]], [backx, earlymanx, mariox], [backy, floorheight, marioheight])
    dialoguebox("Hmph.....", "Medium", [earlymanx, floorheight])
    pygame.display.update()
    gameDisplay.fill(white)
    time.sleep(1)

    background([snowholebackground, evilman, walklistleft[0]], [backx, earlymanx, mariox], [backy, floorheight, marioheight])
    dialoguebox("GO!!!!", "Medium", [earlymanx, floorheight])
    pygame.display.update()
    gameDisplay.fill(white)
    time.sleep(0.5)

    walk(mariox, display_width + 10, marioheight, walklistright, "Right", changewidth = 30, backgroundimagelist = [snowholebackground, evilman], backgroundx = [backx, earlymanx], backgroundy = [backy, floorheight])
    pygame.display.update()
    gameDisplay.fill(white)
    time.sleep(0.5)
    iceagegameloop()

def brickbreakerintro():
    # Changeables:
    backx, backy = 0, 0
    mariosize = walk1.get_size()
    trumpfingerheight = trumpfingerraise.get_size() 
    podiumdimensions = podiumimage.get_size()
    podiumx = display_width/2 - podiumdimensions[0]/2
    podiumy = display_height - podiumdimensions[1]
    groundheight = podiumy - trumpfingerheight[1]
    backgroundsize = trumpbackground.get_size()
    trumpx, trumpy = backgroundsize[0]/2 - trumpfingerheight[0]/2, groundheight + 20
    trumpdialoguex, trumpdialoguey = trumpx - trumpfingerheight[0]/2, trumpy + 70
    mariox = trumpx + 300
    marioheight = 0
    # ---------------------------------------------------------------------
    
    gameDisplay.fill(white)
    background([trumpbackground, trumpfingerraise, podiumimage], [backx, trumpx, podiumx], [backy, trumpy, podiumy])
    pygame.display.update()
    time.sleep(0.5)
    dialoguebox("Can't you see? I have huge hands!", "Medium", [trumpdialoguex, trumpdialoguey])
    time.sleep(0.5)
    gameDisplay.fill(white)
    
    
    while marioheight < display_height:
        clock.tick(50)
        theimage = pygame.transform.rotate(duck, marioheight)
        if marioheight > trumpy:
        
            background([trumpbackground, trump1, podiumimage, theimage], [backx, trumpx, podiumx, mariox], [backy, trumpy, podiumy, marioheight])
        else:
            background([trumpbackground, trumpfingerraise, podiumimage, theimage], [backx, trumpx, podiumx, mariox], [backy, trumpy, podiumy, marioheight])

        pygame.display.update()

        gameDisplay.fill(white)
        if marioheight + 30 <= display_height:
            marioheight += 30
        else:
            marioheight = display_height

    time.sleep(1)



    
    while marioheight > display_height - mariosize[1] - 40:
        clock.tick(20)
        theimage = walklistleft[len(walklistleft) - 2]
        
        background([trumpbackground, trump1, podiumimage, theimage], [backx, trumpx, podiumx, mariox], [backy, trumpy, podiumy, marioheight])

        pygame.display.update()
        gameDisplay.fill(white)
        marioheight -= 10

    time.sleep(0.3)

    while marioheight < display_height - mariosize[1]:
        clock.tick(20)
        theimage = walklistleft[len(walklistleft) - 2]
        background([trumpbackground, trump1, podiumimage, theimage], [backx, trumpx, podiumx, mariox], [backy, trumpy, podiumy, marioheight])
        pygame.display.update()
        gameDisplay.fill(white)
        if marioheight + 10 <= display_height - mariosize[1]:
            marioheight += 10
        else:
            marioheight = display_height - mariosize[1]

    
    background([trumpbackground, trump1, podiumimage, walklistleft[0]], [backx, trumpx, podiumx, mariox], [backy, trumpy, podiumy, marioheight])
    pygame.display.update()
    dialoguebox("It's a me a Ma-", "Medium", [mariox, marioheight])
    pygame.display.update()
    gameDisplay.fill(white)
    
    
    background([trumpbackground, trump1, podiumimage, walklistleft[0]], [backx, trumpx, podiumx, mariox], [backy, trumpy, podiumy, marioheight])
    dialoguebox("What is that caterpillar on your face?!", "Medium", [trumpdialoguex, trumpdialoguey])
    pygame.display.update()
    gameDisplay.fill(white)
    time.sleep(0.5)
    

    background([trumpbackground, trump1, podiumimage, walklistleft[0]], [backx, trumpx, podiumx, mariox], [backy, trumpy, podiumy, marioheight])
    dialoguebox("What died on your head?", "Medium", [mariox, marioheight])
    pygame.display.update()
    gameDisplay.fill(white)
    time.sleep(0.5)

    background([trumpbackground, trumpfingerraise, podiumimage, walklistleft[0]], [backx, trumpx, podiumx, mariox], [backy, trumpy, podiumy, marioheight])
    dialoguebox("I have the best hair...", "Medium", [trumpdialoguex, trumpdialoguey])
    pygame.display.update()
    gameDisplay.fill(white)
    time.sleep(0.5)


    background([trumpbackground, trumpfingerraise, podiumimage, walklistleft[0]], [backx, trumpx, podiumx, mariox], [backy, trumpy, podiumy, marioheight])
    dialoguebox("My supporters LOVE me", "Medium", [trumpdialoguex, trumpdialoguey])
    pygame.display.update()
    gameDisplay.fill(white)
    time.sleep(0.5)

    background([trumpbackground, trumpleft, podiumimage, walklistleft[0]], [backx, trumpx, podiumx, mariox], [backy, trumpy, podiumy, marioheight])
    theimage = pygame.transform.rotate(dialoguedict["Medium"], 270)
    dialoguebox("BOO ! YOU STINK! And your hair looks like something died in there!", "Medium", [100, display_height/2], EOL = 4, imagechange = theimage)
    pygame.display.update()
    time.sleep(0.5)

    background([trumpbackground, suspicioustrump, podiumimage, walklistleft[0]], [backx, trumpx, podiumx, mariox], [backy, trumpy, podiumy, marioheight])
    dialoguebox("Can someone take this Mexican out!!", "Medium", [trumpdialoguex, trumpdialoguey])
    pygame.display.update()
    time.sleep(0.5)

    background([trumpbackground, trumpleft, podiumimage, walklistleft[0]], [backx, trumpx, podiumx, mariox], [backy, trumpy, podiumy, marioheight])
    theimage = pygame.transform.rotate(dialoguedict["Large"], 270)
    dialoguebox("You take him out coz you like him so much!", "Large", [190, display_height/2 + 50], EOL = 10, imagechange = theimage)
    pygame.display.update()
    time.sleep(0.5)

    background([trumpbackground, trumpleft, podiumimage, walklistleft[0]], [backx, trumpx, podiumx, mariox], [backy, trumpy, podiumy, marioheight])
    theimage = pygame.transform.rotate(dialoguedict["Large"], 270)
    dialoguebox("YEAH! We're voting for Hillary Clinton you fat pumpkin with a terrible wig!", "Medium", [150, display_height/2], EOL = 10, imagechange = theimage)
    pygame.display.update()
    time.sleep(0.5)

    background([trumpbackground, suspicioustrump, podiumimage, walklistleft[0]], [backx, trumpx, podiumx, mariox], [backy, trumpy, podiumy, marioheight])
    dialoguebox("First of all I'm Italian... and maybe I can help you with your hillary-ous problem", "Large", [mariox - 100, marioheight])
    pygame.display.update()
    time.sleep(0.5)

    background([trumpbackground, suspicioustrump, podiumimage, walklistleft[0]], [backx, trumpx, podiumx, mariox], [backy, trumpy, podiumy, marioheight])
    dialoguebox("I wish you could help your sense of humour", "Medium", [trumpdialoguex, trumpdialoguey])
    pygame.display.update()
    time.sleep(0.5)

    background([trumpbackground, trumpfingerraise, podiumimage, walklistleft[0]], [backx, trumpx, podiumx, mariox], [backy, trumpy, podiumy, marioheight])
    dialoguebox("If you could just show me Hillary's E-mails that's all I need!", "Medium", [trumpdialoguex, trumpdialoguey])
    pygame.display.update()
    time.sleep(0.5)

    background([trumpbackground, trumpcheer, podiumimage, walklistleft[0]], [backx, trumpx, podiumx, mariox], [backy, trumpy, podiumy, marioheight])
    dialoguebox("Then I would become President!", "Medium", [trumpdialoguex, trumpdialoguey])
    pygame.display.update()
    time.sleep(0.5)

    background([trumpbackground, trumpcheer, podiumimage, walklistleft[0]], [backx, trumpx, podiumx, mariox], [backy, trumpy, podiumy, marioheight])
    dialoguebox("I'll do it but on one condition...", "Medium", [mariox, marioheight])
    pygame.display.update()
    time.sleep(0.5)

    background([trumpbackground, suspicioustrump, podiumimage, walklistleft[0]], [backx, trumpx, podiumx, mariox], [backy, trumpy, podiumy, marioheight])
    dialoguebox("What?", "Small", [trumpdialoguex, trumpdialoguey - 100])
    pygame.display.update()
    time.sleep(0.5)

    background([trumpbackground, suspicioustrump, podiumimage, walklistleft[0]], [backx, trumpx, podiumx, mariox], [backy, trumpy, podiumy, marioheight])
    dialoguebox("Your campaign must be the worst one anyone has EVER seen!", "Medium", [mariox, marioheight])
    pygame.display.update()
    time.sleep(0.5)

    background([trumpbackground, trumpfingerraise, podiumimage, walklistleft[0]], [backx, trumpx, podiumx, mariox], [backy, trumpy, podiumy, marioheight])
    dialoguebox("Done.", "Small", [trumpdialoguex, trumpdialoguey - 100])
    pygame.display.update()
    time.sleep(0.5)

    background([trumpbackground, trumpfingerraise, podiumimage, walklistleft[0]], [backx, trumpx, podiumx, mariox], [backy, trumpy, podiumy, marioheight])
    dialoguebox("I mean absolutely terrible!", "Medium", [mariox, marioheight])
    pygame.display.update()
    time.sleep(0.5)

    background([trumpbackground, trumpfingerraise, podiumimage, walklistleft[0]], [backx, trumpx, podiumx, mariox], [backy, trumpy, podiumy, marioheight])
    dialoguebox("Yes...", "Small", [trumpdialoguex, trumpdialoguey - 100])
    pygame.display.update()
    time.sleep(0.5)

    background([trumpbackground, trumpfingerraise, podiumimage, walklistleft[0]], [backx, trumpx, podiumx, mariox], [backy, trumpy, podiumy, marioheight])
    dialoguebox("You'll have to say THE absolutely most ridiculous things ever...", "Medium", [mariox, marioheight])
    pygame.display.update()
    time.sleep(0.5)

    background([trumpbackground, suspicioustrump, podiumimage, walklistleft[0]], [backx, trumpx, podiumx, mariox], [backy, trumpy, podiumy, marioheight])
    dialoguebox("Sure. Why though?", "Small", [trumpdialoguex, trumpdialoguey - 100])
    pygame.display.update()
    time.sleep(0.5)

    background([trumpbackground, suspicioustrump, podiumimage, walklistleft[0]], [backx, trumpx, podiumx, mariox], [backy, trumpy, podiumy, marioheight])
    dialoguebox("So that I can tell my kids that if YOU became president then so can they...", "Large", [mariox - 100, marioheight])
    pygame.display.update()
    time.sleep(0.5)

    background([trumpbackground, trumpfingerraise, podiumimage, walklistleft[0]], [backx, trumpx, podiumx, mariox], [backy, trumpy, podiumy, marioheight])
    dialoguebox("I can assure you this will be the worst campaign you've ever seen", "Medium", [trumpdialoguex, trumpdialoguey])
    pygame.display.update()
    time.sleep(0.5)

    background([trumpbackground, trumpfingerraise, podiumimage, walklistleft[0]], [backx, trumpx, podiumx, mariox], [backy, trumpy, podiumy, marioheight])
    dialoguebox("Okay then....", "Small", [mariox, marioheight])
    pygame.display.update()
    gameDisplay.fill(white)
    time.sleep(0.5)    
    
    walk(mariox, display_width + 100, marioheight, walklistright, "Right", fps = 40, backgroundimagelist = [trumpbackground, trumpfingerraise, podiumimage], backgroundx = [backx, trumpx, podiumx], backgroundy = [backy, trumpy, podiumy])
    pygame.display.update()
    gameDisplay.fill(white)
    time.sleep(0.5)

    background([trumpbackground, suspicioustrump, podiumimage], [backx, trumpx, podiumx], [backy, trumpy, podiumy])
    dialoguebox("Phew...I thought the Mexican was going to ask me to shave my head...", "Medium", [trumpdialoguex, trumpdialoguey])
    pygame.display.update()
    gameDisplay.fill(white)
    time.sleep(0.5)

    
    pygame.quit()
    quit()
    
    


    
    

# ----------------Animations done done done--------------------------
                
# CHARACTER FUNCTIONS:
def walk(initx, finx, yposition, imagelist, direction, changewidth = 10, fps = 15, backgroundimagelist = None, backgroundx = None, backgroundy = None):


    imagenumber = 0
    while initx < finx and direction.lower() == "right":
 
        clock.tick(fps)
        
        initx += changewidth
        
        if imagenumber < len(imagelist) - 3:
            imagenumber += 1
        else:
            imagenumber = 1
        background(backgroundimagelist, backgroundx, backgroundy)
        gameDisplay.blit(imagelist[imagenumber], [initx, yposition])
        
        
        pygame.display.update()
        gameDisplay.fill(white)
        
    while initx > finx and direction.lower() == "left":

        clock.tick(fps)

        initx -= changewidth
        if imagenumber < len(imagelist) - 3:
            imagenumber += 1
        else:
            imagenumber = 1
        background(backgroundimagelist, backgroundx, backgroundy)
        gameDisplay.blit(imagelist[imagenumber], [initx, yposition])
        
        pygame.display.update()
        gameDisplay.fill(white)
        
    
    background(backgroundimagelist, backgroundx, backgroundy)
    try:
        gameDisplay.blit(imagelist[0], [initx, yposition])
    except:
        pass


def background(imagelist, xposition, yposition):
    for i in range(len(imagelist)):
        gameDisplay.blit(imagelist[i], [xposition[i], yposition[i]])
        


    
    


# ACTUAL GAME:
def gameintro():
    intro = True
    Ready = False
    while True:
        
        gameDisplay.fill(white)

        
        while not Ready:
            message_to_screen("Adjust the Screen and then click Start", red, (display_width/2, 100), size = "medium")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                    pygame.quit()
                    
            Ready = button("Start", display_width/2 - 50, display_height/2 - 50, 100, 100, green, darkgreen, action = "Ready")

            pygame.display.update()
            gameDisplay.fill(white)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        if intro:
            iceage()           
            intro = False



        


def iceagegameloop():
    gameon = True
    groundheight = display_height/2 + 100
    backx, back1x, back2x = -display_width, 0, display_width
    backy, back1y, back2y = 0, 0, 0
    fps = 10    
    walk(-100, display_width/2, groundheight, walklistright, "Right", backgroundimagelist = [snowbackground, snowbackground, snowbackground], backgroundx = [backx, back1x, back2x], backgroundy = [backy, back1y, back2y])
    pygame.display.update()
    jumpheight = 120
    xposition = display_width/2
    imagenumber = 0
    yposition = groundheight
    lastimage = len(walklistright) - 1
    direction = "Right"
    backgroundlock = leftlock = False
    dinodirection = "Left"
    dinox = display_width + 10
    mariosize = walk1.get_size()
    dinosize = dinowalk1.get_size()
    dinoy = groundheight + mariosize[1] - dinosize[1]
    dinoimagelist = [dinowalk]
    dinoimagenumber = 0
    dinoonscreen = False
    while gameon:
        if not dinoonscreen:
            whichdino = random.randint(0, len(dinoimagelist) - 1)

            dinox = display_width + 10
            dinoy = groundheight + mariosize[1] - dinosize[1]
            dinoonscreen = True
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

        movement = pygame.key.get_pressed()
        if movement[pygame.K_RIGHT] and movement[pygame.K_UP]:
            direction = "Right"
            if not backgroundlock:
                backx -= 15
                back1x -= 15
                back2x -= 15
            else:
                xposition += 15
            if yposition <> groundheight:
                imagenumber = -2
            else:
                if imagenumber < lastimage - 2:
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
            
            direction = "Left"
            if not backgroundlock and not leftlock:
                backx += 15
                back1x += 15
                back2x += 15
            else:
                xposition -= 15
            if yposition <> groundheight:
                imagenumber = -2
            else:
                if leftlock:
                    if xposition <= 15:
                        dialoguebox("Apparently I can't go that way", "Small", [xposition + 10, yposition])
                        xposition = xposition
                    else:
                        xposition -= 15
                if imagenumber < lastimage - 2:
                    imagenumber += 1
                else:
                    imagenumber = 1
##                else:
##                    xposition -= 15


            if yposition <= groundheight - jumpheight or goingup == False:
                if yposition < groundheight - 10:
                    yposition += 20
                else:
                    yposition = groundheight
                goingup = False    
            elif yposition > groundheight - jumpheight and goingup:
                yposition -= 20

                
        
        elif movement[pygame.K_RIGHT]:
            direction = "Right"

            if not backgroundlock:
                
                backx -= 15
                back1x -= 15
                back2x -= 15
            else:
                xposition += 15
            if yposition <> groundheight:
                yposition = groundheight
            if imagenumber < lastimage - 2:
                imagenumber += 1
            else:
                imagenumber = 1
            goingup = True

        elif movement[pygame.K_LEFT]:

            direction = "Left"
            if not backgroundlock and not leftlock:
                backx += 15
                back1x += 15
                back2x += 15
            else:
                if leftlock:
                    if xposition <= 15:
                        dialoguebox("Apparently I can't go that way", "Small", [xposition + 10, yposition])
                        xposition = xposition
                    else:
                        xposition -= 15
                else:
                    xposition -= 15
            if yposition <> groundheight:
                yposition = groundheight
                
            if imagenumber < lastimage - 2:
                imagenumber += 1
            else:
                imagenumber = 1
            goingup = True
            
        elif movement[pygame.K_DOWN]:
            yposition = groundheight + 40
            imagenumber = -1
            
                

        elif movement[pygame.K_UP]:                
            if yposition <> groundheight:
                imagenumber = -2
            else:
                imagenumber = 0
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
            goingup = True

        if direction.lower() == "right":
            imagelist = walklistright
        else:
            imagelist = walklistleft

        if backx + display_width <= 0:
            backx, back1x, back2x = back1x, back2x, back2x + display_width
        if back2x - display_width >= display_width:
            back2x, back1x, backx = back1x, backx, backx - display_width

        
        if dinoonscreen:
            dinox -= 30
            if dinoimagenumber < len(dinoimagelist[whichdino]) - 1:
                dinoimagenumber += 1
            else:
                dinoimagenumber = 0
            dinoimage = dinoimagelist[whichdino][dinoimagenumber]

##        print dinox, dinox < -90

        if dinox < -90:
            dinoonscreen = False
            

        
        
        background([snowbackground, snowbackground, snowbackground], [backx, back1x, back2x], [backy, back1y, back2y])

        gameDisplay.blit(imagelist[imagenumber], [xposition, yposition])
        if dinoonscreen:          
            gameDisplay.blit(dinoimage, [dinox, dinoy])
        pygame.display.update()
        gameDisplay.fill(white)

            
            
        

def firstgameloop():
    # ALL VARIABLES INITIALIZED HERE:
    gameon = True
    fps = 10
    backgroundx, backgroundy = 0, 0
    imagenumber = 0
    groundheight = display_height/2 + 150
    jumpheight = 75
    xposition = display_width/2
    yposition = groundheight
    goingup = True
    lastimage = len(walklistright) -1
    direction = "Right"
    backx = backgroundx
    back1x, back2x = backx - display_width, backx + display_width
    stageonedone = stage2done = stage3done = stage4done = checkjump = False
    countcave = 0
    backgroundlock = caveon = leftlock = False
    
    # -------------------------
    firstintro()
    
    while gameon:
        clock.tick(fps)
        movement = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

        # UP AND RIGHT:
        if movement[pygame.K_RIGHT] and movement[pygame.K_UP]:
            
            direction = "Right"
            if not backgroundlock:
                backx -= 15
                back1x -= 15
                back2x -= 15
            else:
                xposition += 15
            if yposition <> groundheight:
                imagenumber = -2
            else:
                if imagenumber < lastimage - 2:
                    imagenumber += 1
                else:
                    imagenumber = 1
            if yposition <= groundheight - jumpheight or goingup == False:
                if yposition < groundheight - 10:
                    yposition += 20    
                else:
                    yposition = groundheight
                    if stageonedone and not stage2done and checkjump:
                        stage2done = True
                goingup = False    
            elif yposition > groundheight - jumpheight and goingup:
                yposition -= 20
            if stageonedone and not stage2done and checkjump:
                stage2done = True

        
        elif movement[pygame.K_LEFT] and movement[pygame.K_UP]:
            
            direction = "Left"
            if not backgroundlock and not leftlock:
                backx += 15
                back1x += 15
                back2x += 15
            else:
                xposition -= 15
            if yposition <> groundheight:
                imagenumber = -2
            else:
                if leftlock:
                    if xposition <= 15:
                        dialoguebox("Apparently I can't go that way", "Small", [xposition + 10, yposition])
                        xposition = xposition
                    else:
                        xposition -= 15
                else:
                    xposition -= 15


            if yposition <= groundheight - jumpheight or goingup == False:
                if yposition < groundheight - 10:
                    yposition += 20
                else:
                    yposition = groundheight
                    if stageonedone and not stage2done and checkjump:
                        stage2done = True
                goingup = False    
            elif yposition > groundheight - jumpheight and goingup:
                yposition -= 20

        elif movement[pygame.K_DOWN]:
            imagenumber = lastimage
            yposition = groundheight + 40
            

        elif movement[pygame.K_RIGHT]:
            direction = "Right"
            if not stageonedone:
                stageonedone = True
            if not backgroundlock:
                
                backx -= 15
                back1x -= 15
                back2x -= 15
            else:
                xposition += 15
            if yposition <> groundheight:
                yposition = groundheight
            if imagenumber < lastimage - 2:
                imagenumber += 1
            else:
                imagenumber = 1
            goingup = True

        elif movement[pygame.K_LEFT]:
            if not stageonedone:
                stageonedone = True
            direction = "Left"
            if not backgroundlock and not leftlock:
                backx += 15
                back1x += 15
                back2x += 15
            else:
                if leftlock:
                    if xposition <= 15:
                        dialoguebox("Apparently I can't go that way", "Small", [xposition + 10, yposition])
                        xposition = xposition
                    else:
                        xposition -= 15
                else:
                    xposition -= 15

            
                    
            if yposition <> groundheight:
                yposition = groundheight
            goingup = True
            if imagenumber < lastimage - 2:
                imagenumber += 1
            else:
                imagenumber = 1
            

                
            
           
            

        elif movement[pygame.K_UP]:
            if stageonedone and not stage2done:
                stage2done = True
                
            if yposition <> groundheight:
                imagenumber = -2
            else:
                imagenumber = 0
            if yposition <= groundheight - jumpheight or goingup == False:                    
                if yposition < groundheight - 10:
                    yposition += 20     
                else:
                    yposition = groundheight
                    if stageonedone and not stage2done and checkjump:
                        stage2done = True
                goingup = False
            elif yposition > groundheight - jumpheight and goingup:
                yposition -= 20

        else:
            imagenumber = 0
            yposition = groundheight
            goingup = True

        if direction.lower() == "right":
            imagelist = walklistright
        else:
            imagelist = walklistleft

        if back1x + display_width <= 0:
            back1x, backx, back2x = backx, back2x, back2x + display_width
            if stage3done:
                countcave += 1
                

            
        if back2x - display_width >= display_width:
            back2x, backx, back1x = backx, back1x, back1x - display_width
##            stageonedone = True

        if countcave < 2: 
            background([genericbackground, genericbackground, genericbackground], [back1x, backx, back2x], [backgroundy, backgroundy, backgroundy])
        elif countcave >= 2:
            caveon = True
            background([genericbackground, cave, genericbackground], [back1x, backx, back2x], [backgroundy, backgroundy, backgroundy])
        
        if backx == 0 and caveon:
                backgroundlock = True    
            
                
        if backgroundlock and xposition > display_width - 310:
            pass
        else:
            if backgroundlock and xposition >= display_width/2 and not stage4done:
                firstintro(4)
                stage4done = True
            if stage4done:
                background([cave], [0], [0])
            else:
                gameDisplay.blit(imagelist[imagenumber], [xposition, yposition])


        pygame.display.update()
        gameDisplay.fill(white)

        if stageonedone and not stage2done and checkjump == False:

            if back1x == 0 or back2x == 0 or backx == 0:
                firstintro(2)
                checkjump = True

        if stageonedone and stage2done and not stage3done and yposition == groundheight and checkjump:
            
##            if initmariox > display_width/2:
##                imagelist = walklistleft
##                direct = "Left"
##            else:
##                direct = "Right"
##                imagelist = walklistright
##            gameDisplay.blit(imagelist[0], [initmariox, display_height/2 + 150]) 
##            
##            walk(initmariox, display_width/2, display_height/2 + 150,  imagelist, direction = direct, backgroundimagelist = [genericbackground], backgroundx = [0], backgroundy = [0]) 
            
            firstintro(3)
            stage3done = True
            leftlock = True
            countcave = 0
            background([genericbackground, walklistright[0]], [0, display_width/2 + 3], [0, groundheight])




brickbreakerintro()





