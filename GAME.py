'''Look at synopsis document for intro to game
To know what the game is play it.

Define different regions by putting title in caps as a comment
End the region with another comment.
This way it is easier to figure out what shit does.

All levels in a class
Each level class object must have a function gameLoop(), in which the game loop runs if you haven't guessed already.
All other methods/attributes can be level specific.'''
#from dialoguebox import *
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
blue = (0, 0, 255)
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
heart = pygame.image.load("heart.png")

# Early Man Images
earlyman = pygame.image.load("earlyman.png")
surprisedman = pygame.image.load("surprisedman.png")
evilman = pygame.image.load("evilearlyman.png")
dinowalk1 = pygame.image.load("dino1.png")
dinowalk2 = pygame.image.load("dino2.png")
dinostand = pygame.image.load("dinostand.png")
flyingdino = pygame.image.load("flyingdino.png")
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

charredleft1 = pygame.image.load("charredleftwalk.png")
charredleft2 = pygame.image.load("charredleftwalk2.png")
charredleft3 = pygame.image.load("charredleftwalk3.png")
charredstand = pygame.image.load("charredstand.png")

charredlistleft = [charredstand, charredleft1, charredleft2, charredleft3]

audi = pygame.image.load('audi.jpg')

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
largedialogue = pygame.image.load("largedialogue.png")
mediumdialogue = pygame.image.load("mediumdialogue.png")
smalldialogue = pygame.image.load("smalldialogue.png")
dialoguedict = {"Large" : largedialogue, "Medium":mediumdialogue, "Small":smalldialogue}



walklistright = [standright, walk1, walk2, walk3, jumpright, duck]
walklistleft = [standleft, walk1left, walk2left, walk3left, jumpleft, leftduck]
dinowalk = [dinowalkleft1, dinowalkleft2, dinostandleft]
dinofly = [flyingdino]
dialoguedict = {"Large" : largedialogue, "Medium":mediumdialogue, "Small":smalldialogue}

flame = pygame.image.load("flames.png")

#MUSIC!
pygame.mixer.music.load('AIP theme.wav')
pygame.mixer.music.play(-1)

#IMPORTANT CONSTANTS FOR AND DESIGN OF GAME DISPLAY------------------------------------------
display_width, display_height = 1000, 750
gameDisplay = pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)
gameDisplay.fill(white)
clock = pygame.time.Clock()
MAXLEVELS = 3
'''The levels are (not counting pure animation levels):
1. Ice Age - Dino Run
2. Sir Francis Drake - Ship Game
3. Trump - Brick Breaker'''
CURRENTLEVEL = 3 #Keeps track of the current level no.

settingsfile = open('GAME settings.txt')
for line in settingsfile:
    UNLOCKEDLEVEL = int(line.rstrip()) #Keeps track of the unlocked level. This is the only thing saved on the text file.
settingsfile.close()
#--------------------------------------------------------------------------------------------

#TEXT AND BUTTON STUFF:  --------------------------------------------------------------------
# Font sizes:
smallfont = pygame.font.SysFont("comicsansms", 15)
smallmedfont = pygame.font.SysFont("comicsansms", 30)
medfont = pygame.font.SysFont("comicsansms", 35)
mediumlargefont = pygame.font.SysFont("comicsansms", 60)
largefont = pygame.font.SysFont("comicsansms", 80)



def button(text, x, y, width, height, inactiveColour, activeColour, action = None):
    levelno = action
    #x, y is the coordinates of the top left corner of the button
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        if click[0] == 1 and levelno != None:
            #stuff the button has to do. level is the level no of button which was clicked. It tells which function to run
            if levelno in range(1, MAXLEVELS + 1):
                return levelno
        pygame.draw.rect(gameDisplay, activeColour, (x, y, width, height))
    else:
        pygame.draw.rect(gameDisplay, inactiveColour, (x, y, width, height))
    text_to_button(text, black, x, y, width, height)
    return None
    
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

def fabulous(xposition, yposition, colourlist = [yellow, gold, goldenrod]):
    explode = True
    while explode:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_function()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause_screen()
                        
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
                    #count1 = EOL + 1
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
##                elif count % EOL == 3:
            time.sleep(timegap)

#---------------------------------------------------------------------------------------------

#DIFFERENT MENU SCREENS: ---------------------------------------------------------------------
def pause_screen():
    pygame.mixer.music.pause()
    text = []
    while True:
        gameDisplay.fill(white)
        message_to_screen('GONE FOR', red, (display_width//2, display_height//5), display_height//5)
        message_to_screen('TOILET BREAK', red, (display_width//2, 2.5*display_height//5), display_height//5 - 20)
        message_to_screen('PRESS P TO CONTINUE', black, (display_width//2, 4*display_height//5), display_height//20)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_function()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit_function()
                if event.key == pygame.K_p:
                    pygame.mixer.music.unpause()
                    return False 
                if event.key in (pygame.K_c, pygame.K_h, pygame.K_e, pygame.K_a, pygame.K_t):
                    text.append(event.key)
                else:
                    text = []
        if text == [pygame.K_c, pygame.K_h, pygame.K_e, pygame.K_a, pygame.K_t]:
            gameDisplay.fill(white)
            pygame.mixer.music.unpause()
            writing('WE\'RE PROUD OF YOU!', black, (display_width//2 - 250, 100), 150, 0.1, 6) 
            return True
                
def quit_function():
    pygame.mixer.music.stop()
    gameDisplay.fill(white)
    walk(0, display_width/2, display_height/2 + 50, walklistright, 'Right', backgroundimagelist = [snowbackground], backgroundx = [0], backgroundy = [0])
    pygame.display.update()
    dialoguebox('WHY DO YOU DO THIS?!', 'Medium', (display_width/2, display_height/2 + 50))
    pygame.display.update()
    time.sleep(1)
    pygame.quit()
    quit()
        
def vortex(xwidth = 1500, yheight = 1500):
    
    
    for i in range(90):
        clock.tick(90)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                quit_function()
        theimage = pygame.transform.rotate(vorteximage, 2*i)
        imagexwidth, imageyheight = theimage.get_size()
        imagex = display_width//2 - imagexwidth//2
        imagey = display_height//2 - imageyheight//2
        secondimage = pygame.transform.rotate(walklistright[0], 4 * i)
        secondimage_size = secondimage.get_size()
        background([theimage, secondimage], [imagex, display_width/2 - secondimage_size[0]/2], [imagey, display_height/2 - secondimage_size[1]/2])
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
    
    cheat = False

    if stage == 1:
        initmariox = -10
        finalmariox = display_width /2
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_function()
            if event.type == pygame.K_p:
                cheat = pause_screen()                
        
    
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
        gameDisplay.fill(white)
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
                    quit_function()
                
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        pause_screen()
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
        return 'done'
   
def hitlerrun():
    # Changeables:
    floorheight = display_height/2 + 100
    fridgex, fridgey, pipex, pipey = 250, floorheight - 100, display_width - 230, floorheight - 200
    # -----------------------------

    
    walk(0, pipex - 160, floorheight, walklistright, "right", backgroundimagelist = [hitlerbackgroundimage, fridgeclosedimage, pipesimage], backgroundx = [0, fridgex, pipex], backgroundy = [0, fridgey, pipey])
    dialoguebox("Hello pipes my old friend...", "Medium", (display_width/2, floorheight))
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
    vortex()
    brickbreakerintro()

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
    
    shipGameLoop()

def iceage(stage = 1):
    # Changeables:
    backx, backy = 0, 0
    earlymanx = 100
    floorheight = display_height/2 + 100
    mariox = display_width/2 + 100
    jumpheight = 80
    


    if stage == 1:
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
        dialoguebox("Ah! I know! He'll fall for the easiest trick in the book...", "Large", [mariox - 60, marioheight])
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

    elif stage == 2:
        mariox =  -20
        marioy = display_height/2 + 150
        backx = backy = 0


        gameDisplay.fill(white)
        walk(mariox, display_width/2, marioy, walklistright, "Right", backgroundimagelist = [snowbackground], backgroundx = [backx], backgroundy = [backy])
        pygame.display.update()
        time.sleep(0.5)
        mariox = display_width/2
        
        dialoguebox("Phew... Good thing I'm experienced at that...", "Medium", [mariox, marioy])
        pygame.display.update()
        gameDisplay.fill(white)
        time.sleep(0.5)
        
        background([snowbackground, walklistleft[0]], [backx, mariox], [backy, marioy])
        dialoguebox("HA! Dinosaurs! You got nothing on old boy Ma-", "Medium", [mariox, marioy])
        pygame.display.update()
        gameDisplay.fill(white)
        time.sleep(0.1)
        
    
        background([snowbackground, walklistright[0]], [backx, mariox], [backy, marioy])
        theimage = pygame.transform.rotate(dialoguedict["Large"], 90)
        dialoguebox("RAAAAAAAAAAAAAAAAAAAAAAAAAAAAWWWWWWWWWWWWWWWWWWWWWWRRRRRR! !!!!!", "Medium", [display_width - 250, display_height/2 - 50], imagechange = theimage, EOL = 4)
        pygame.display.update()
        gameDisplay.fill(white)
        time.sleep(0.5)


        flamey = display_height/2 - 300
        flamex = display_width + 10
        hypotenuse = 20
        slope = abs((display_height - (flamey + 150))//(display_width - (mariox + 300)))
        angle = degrees(atan(slope))
        theimage = pygame.transform.rotate(flame, 90 - angle)
        
        while flamex >= mariox or flamey <= 0:
            clock.tick(10)
            background([snowbackground, walklistright[0]], [backx, mariox], [backy, marioy])
            gameDisplay.blit(theimage, [flamex, flamey])
            flamex -= hypotenuse * sin(radians(angle))
            flamey += hypotenuse * cos(radians(angle))
            pygame.display.update()
            gameDisplay.fill(white)


        background([snowbackground, charredlistleft[0]], [backx, mariox], [backy, marioy])

        dialoguebox("... F-f-ire", "Medium", [mariox, marioy])
        pygame.display.update()
        gameDisplay.fill(white)
        time.sleep(1)
        
        marioheight = marioy
        while marioheight > -100:
            
            clock.tick(20)
            theimage = pygame.transform.rotate(charredlistleft[0], marioheight)
            background([snowbackground, theimage], [backx, mariox], [backy, marioheight])
            pygame.display.update()
            gameDisplay.fill(white)
            if marioheight - 20 >= -100:
                marioheight -= 20
            else:
                marioheight = -100

        background([snowbackground], [backx], [backy])

class BrickBreaker:
    GAMEOVER = False
    bricksize = pygame.image.load('brick.png').get_size()

    class Block:
        emailImg = pygame.image.load('email.png')
        brickImg = pygame.image.load('brick.png')
        specialbrickImg = pygame.image.load('specialbrick.png')
        bricksize = specialbrickImg.get_size()
        emailsize = emailImg.get_size()
        broken = False

        def __init__(self, loc, special = False):
            self.xpos, self.ypos = loc
            self.special = special

        def get_rect(self):
            return pygame.Rect((self.xpos, self.ypos), self.bricksize)

        def draw(self):
            if self.broken and self.special:
                self.xpos += 4
                self.ypos += 4
                gameDisplay.blit(self.emailImg, (self.xpos, self.ypos))
            elif not self.broken:
                if self.special: gameDisplay.blit(self.specialbrickImg, (self.xpos, self.ypos))
                else: gameDisplay.blit(self.brickImg, (self.xpos, self.ypos))
    
    class Projectile:
        colour = blue
        velocity = [0, 0]
        maxVelocity = 8
        moving = False
        image = pygame.image.load('mariohead.png')
        image_size = image.get_size()

        def __init__(self, centre):
            self.centre = list(centre)
            self.radius = self.image_size[0]//2

        def draw(self):
            #pygame.draw.circle(gameDisplay, self.colour, self.centre, self.radius)
            gameDisplay.blit(self.image, (self.centre[0] - self.radius, self.centre[1] - self.radius))

        def get_rect(self):
            rectx, recty = self.centre[0] - self.radius, self.centre[1] - self.radius
            rectwidth = rectheight = 2*self.radius
            r = pygame.Rect(rectx, recty, rectwidth, rectheight)
            return r

        def collision(self, obj = 'walls', theobject = None):
            if not self.moving: return
            if obj == 'walls':
                if self.centre[0] - self.radius <= 0 or self.centre[0] + self.radius >= display_width: self.velocity[0] = - self.velocity[0]
                elif self.centre[1] - self.radius <= 0: self.velocity[1] = - self.velocity[1]
                elif self.centre [1] >= display_height: return True
                else: return False
            elif obj == 'paddle':
                if self.get_rect().colliderect(theobject.get_rect()):
                    distance = min(abs(self.centre[0] - theobject.x), abs(self.centre[0] - theobject.x - theobject.length))
                    self.velocity[1] = - max(abs(self.velocity[1] - (self.velocity[1] * distance / (theobject.length/2))), abs((self.velocity[1] * distance / (theobject.length/2))))
                    if abs(self.velocity[1]) <= 5: self.velocity[1] = - int(float(self.maxVelocity) * sin(radians(45.0)))
                    sign = -1 if self.velocity[0] < 0 else 1
                    self.velocity[0] = sign * int(((self.maxVelocity**2) - (self.velocity[1]**2))**0.5)
            elif obj == 'blocks':
                for i in range(len(theobject)):
                    for j in range(len(theobject[0])):
                        if theobject[i][j].broken == False and self.get_rect().colliderect(theobject[i][j].get_rect()):
                            if theobject[i][j].xpos <= self.centre[0] <= theobject[i][j].xpos + theobject[i][j].bricksize[0]:
                                self.velocity[1] = -self.velocity[1]
                            elif theobject[i][j].ypos <= self.centre[1] <= theobject[i][j].xpos + theobject[i][j].bricksize[1]:
                                self.velocity[0] = -self.velocity[0]
                            return (i, j)
                else:
                    return None       

        def move(self, paddle):
            if not self.moving:
                self.centre[0] = paddle.x + paddle.length//2
                self.centre[1] = paddle.y - self.radius
                return
            self.centre[0] += self.velocity[0]
            self.centre[1] += self.velocity[1]

    class Paddle:
        width = 20
        length = 100
        speed = 10
        colour = green
        movement = 0
        
        def __init__(self):
            self.x, self.y = (display_width/2 - self.length/2), display_height - 30

        def get_rect(self):
            return pygame.Rect(self.x, self.y, self.length, self.width)

        def draw(self):
            pygame.draw.rect(gameDisplay, self.colour, self.get_rect())

    numRows, numCols = 5, 7

    def __init__(level):
        level.GAMEOVER = False
        level.count = 0
        level.numEmails = 0
        level.totalarraywidth = level.bricksize[0]*level.numCols
        level.topleftarrayx = display_width/2 - level.totalarraywidth/2
        level.topleftarrayy = 50
        level.blocks = [[None for x in range(level.numRows)] for y in range(level.numCols)]
        for i in range(level.numRows):
            for j in range(level.numCols):
                if i in range(level.numRows//2 - 1, level.numRows//2 + 2) and j in range(level.numCols//2 - 1, level.numCols//2 + 2):
                    flag = True
                    level.numEmails += 1
                else: flag = False
                x = level.topleftarrayx + j * level.bricksize[0]
                y = level.topleftarrayy + i * level.bricksize[1]
                level.blocks[j][i] = level.Block((x, y), flag)
        level.paddle = level.Paddle()
        level.ball = level.Projectile((display_width//2, level.paddle.y))

    def gameLoop(level):
        cheat = False
        while not level.GAMEOVER:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        quit_function()
                    elif event.key == pygame.K_p:
                        cheat = pause_screen()
                    elif event.key == pygame.K_SPACE:
                        if not level.ball.moving:
                            level.ball.moving = True
                            if level.paddle.movement == 0:
                                level.ball.velocity[0] = 0
                                level.ball.velocity[1] = - (level.ball.maxVelocity)
                            else:
                                if level.paddle.movement < 0:
                                    level.ball.velocity[0] = - int(float(level.ball.maxVelocity) * sin(radians(45.0)))
                                else:
                                    level.ball.velocity[0] = int(float(level.ball.maxVelocity) * sin(radians(45.0)))
                                level.ball.velocity[1] = - int(float(level.ball.maxVelocity) * sin(radians(45.0)))
            if cheat:
                level.GAMEOVER = True
            level.ball.move(level.paddle)
            flagLose = level.ball.collision('walls')
            if flagLose:
                level.__init__()
                level.gameLoop()
            level.ball.collision('paddle', level.paddle)
            loc = level.ball.collision('blocks', level.blocks)
            if loc != None:
                level.blocks[loc[0]][loc[1]].broken = True
                if level.blocks[loc[0]][loc[1]].special: level.count += 1
            if level.count == level.numEmails:
                level.exitlevel()
            keystate = pygame.key.get_pressed()
            level.paddle.movement = - level.paddle.speed * (keystate[pygame.K_LEFT] - keystate[pygame.K_RIGHT])
            if (level.paddle.speed <= level.paddle.x + level.paddle.movement <= display_width - level.paddle.speed - level.paddle.length):
                level.paddle.x += level.paddle.movement
            else:
                level.paddle.movement = 0
            #Draw all
            gameDisplay.fill(white)
            for i in range(level.numRows):
                for j in range(level.numCols):
                    level.blocks[j][i].draw()
            level.paddle.draw()
            level.ball.draw()
            pygame.display.update()
      

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
    theimage = pygame.transform.rotate(dialoguedict["Large"], 270)
    dialoguebox("BOO ! YOU STINK! And your hair looks like something died in there!", "Medium", [150, display_height/2], EOL = 6, imagechange = theimage)
    pygame.display.update()
    time.sleep(0.5)

    background([trumpbackground, suspicioustrump, podiumimage, walklistleft[0]], [backx, trumpx, podiumx, mariox], [backy, trumpy, podiumy, marioheight])
    dialoguebox("Can someone take this Mexican out!!", "Medium", [trumpdialoguex, trumpdialoguey])
    pygame.display.update()
    time.sleep(0.5)

    background([trumpbackground, trumpleft, podiumimage, walklistleft[0]], [backx, trumpx, podiumx, mariox], [backy, trumpy, podiumy, marioheight])
    theimage = pygame.transform.rotate(dialoguedict["Large"], 270)
    dialoguebox("You take him out coz you like him so much!", "Medium", [150, display_height/2 + 50], EOL = 8, imagechange = theimage)
    pygame.display.update()
    time.sleep(0.5)

    background([trumpbackground, trumpleft, podiumimage, walklistleft[0]], [backx, trumpx, podiumx, mariox], [backy, trumpy, podiumy, marioheight])
    theimage = pygame.transform.rotate(dialoguedict["Large"], 270)
    dialoguebox("YEAH! We're voting for Hillary Clinton you fat pumpkin with a terrible wig!", "Medium", [150, display_height/2], EOL = 8, imagechange = theimage)
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
    dialoguebox("Your campaign must be the worst one anyone has EVER seen!", "Medium", [mariox - 100, marioheight])
    pygame.display.update()
    time.sleep(0.5)

    background([trumpbackground, trumpfingerraise, podiumimage, walklistleft[0]], [backx, trumpx, podiumx, mariox], [backy, trumpy, podiumy, marioheight])
    dialoguebox("Done.", "Small", [trumpdialoguex, trumpdialoguey - 100])
    pygame.display.update()
    time.sleep(0.5)

    background([trumpbackground, trumpfingerraise, podiumimage, walklistleft[0]], [backx, trumpx, podiumx, mariox], [backy, trumpy, podiumy, marioheight])
    dialoguebox("I mean absolutely terrible!", "Medium", [mariox - 50, marioheight])
    pygame.display.update()
    time.sleep(0.5)

    background([trumpbackground, trumpfingerraise, podiumimage, walklistleft[0]], [backx, trumpx, podiumx, mariox], [backy, trumpy, podiumy, marioheight])
    dialoguebox("Yes...", "Small", [trumpdialoguex, trumpdialoguey - 100])
    pygame.display.update()
    time.sleep(0.5)

    background([trumpbackground, trumpfingerraise, podiumimage, walklistleft[0]], [backx, trumpx, podiumx, mariox], [backy, trumpy, podiumy, marioheight])
    dialoguebox("You'll have to say THE absolutely most ridiculous things ever...", "Medium", [mariox - 75, marioheight])
    pygame.display.update()
    time.sleep(0.5)

    background([trumpbackground, suspicioustrump, podiumimage, walklistleft[0]], [backx, trumpx, podiumx, mariox], [backy, trumpy, podiumy, marioheight])
    dialoguebox("Sure. Why though?", "Small", [trumpdialoguex, trumpdialoguey - 100])
    pygame.display.update()
    time.sleep(0.5)

    background([trumpbackground, suspicioustrump, podiumimage, walklistleft[0]], [backx, trumpx, podiumx, mariox], [backy, trumpy, podiumy, marioheight])
    dialoguebox("So that I can tell my kids that if YOU became president then so can they...", "Large", [mariox - 150, marioheight])
    pygame.display.update()
    time.sleep(0.5)

    background([trumpbackground, trumpfingerraise, podiumimage, walklistleft[0]], [backx, trumpx, podiumx, mariox], [backy, trumpy, podiumy, marioheight])
    dialoguebox("I can assure you this will be the worst campaign you've ever seen", "Medium", [trumpdialoguex, trumpdialoguey], textsize = 25)
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
    dialoguebox("Phew...that Mexican is gone...", "Medium", [trumpdialoguex, trumpdialoguey])
    pygame.display.update()
    gameDisplay.fill(white)
    time.sleep(0.5)
    
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
    level = None
    while level == None: #level not chosen yet
        message_to_screen("Adjust the Screen and then click Start", red, (display_width/2, 100), size = "medium")
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit_function()
        #Stuff for placing the level buttons
        btngap = 15
        btnwidth, btnheight = 100, 100
        btnx = 2*btngap
        btny = display_height//2
        for i in range(UNLOCKEDLEVEL):
            level = button("LEVEL " + str(i+1), btnx, btny, btnwidth, btnheight, green, darkgreen, action = (i+1))
            if level != None: break
            btnx += (btngap + btnwidth)
            if btnx > display_width - btnwidth:
                btnx = 2*btngap
                btny += (btnheight + btngap)
        pygame.display.update()
        gameDisplay.fill(white)
    else:
        return level

def lives(numberoflives, xposition, yposition):
    initialwidth = xposition
    heartsize = heart.get_size()
    for number in range(numberoflives):
        initialwidth += heartsize[0] + 10
        gameDisplay.blit(heart, [initialwidth, yposition])
    pygame.display.update()
    return
    
def iceagegameloop():
    gameon = True
    groundheight = display_height/2 + 100
    backx, back1x, back2x = -display_width, 0, display_width
    backy, back1y, back2y = 0, 0, 0
    fps = 15    
    xposition = display_width/2
    yposition = groundheight
    walk(-100, display_width/2, groundheight, walklistright, "Right", backgroundimagelist = [snowbackground, snowbackground, snowbackground], backgroundx = [backx, back1x, back2x], backgroundy = [backy, back1y, back2y])
    pygame.display.update()
    dialoguebox('AAHHHH DINOS!', 'Medium', [xposition, yposition])
    pygame.display.update()
    time.sleep(0.5)
    dialoguebox('I better run', 'Medium', [xposition, yposition])
    pygame.display.update()
    time.sleep(0.5)
    jumpheight = 120
    imagenumber = 0
    lastimage = len(walklistright) - 1
    direction = "Right"
    backgroundlock = leftlock = False
    dinodirection = "Left"
    dinox = display_width + 10
    mariosize = walk1.get_size()
    dinosize = dinowalk1.get_size()
    flysize = flyingdino.get_size()
    dinoimagelist = [dinowalk]
    dinoimagenumber = 0
    dinoonscreen = False
    numberoflives = 4
    heartcheck = True
    currentxposition = 0
    dinocount = 0
    cheat = False
    while gameon:
        
        
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_function
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit_function()
                
                if event.key == pygame.K_p:
                    cheat = pause_screen()
        if cheat:
            gameon = False

        movement = pygame.key.get_pressed()
        
        if movement[pygame.K_RIGHT] and movement[pygame.K_UP]:
            direction = "Right"
            if not backgroundlock:
                if xposition <> display_width/2:
                    xposition += 1
                backx -= 10
                back1x -= 10
                back2x -= 10
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

##        elif movement[pygame.K_LEFT] and movement[pygame.K_UP]:
##            
##            direction = "Left"
##            if not backgroundlock and not leftlock:
##                if xposition <> display_width/2:
##                    xposition += 1
##                backx -= 2
##                back1x -= 2
##                back2x -= 2
##            else:
##                xposition -= 15
##            if yposition <> groundheight:
##                imagenumber = -2
##            else:
##                if leftlock:
##                    if xposition <= 15:
##                        dialoguebox("Apparently I can't go that way", "Small", [xposition + 10, yposition])
##                        xposition = xposition
##                    else:
##                        xposition -= 15
##                if imagenumber < lastimage - 2:
##                    imagenumber += 1
##                else:
##                    imagenumber = 1
####                else:
####                    xposition -= 15


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
                if xposition <> display_width/2:
                    xposition += 1
                
                backx -= 10
                back1x -= 10
                back2x -= 10
            else:
                xposition += 15
            if yposition <> groundheight:
                yposition = groundheight
            if imagenumber < lastimage - 2:
                imagenumber += 1
            else:
                imagenumber = 1
            goingup = True

##        elif movement[pygame.K_LEFT]:
##
##            direction = "Left"
##            if not backgroundlock and not leftlock:
##                if xposition <> display_width/2:
##                    xposition += 1
##                backx += 10
##                back1x += 10
##                back2x += 10
##            else:
##                if leftlock:
##                    if xposition <= 15:
##                        dialoguebox("Apparently I can't go that way", "Small", [xposition + 10, yposition])
##                        xposition = xposition
##                    else:
##                        xposition -= 15
##                else:
##                    xposition -= 15
##            if yposition <> groundheight:
##                yposition = groundheight
##                
##            if imagenumber < lastimage - 2:
##                imagenumber += 1
##            else:
##                imagenumber = 1
##            goingup = True
            
        elif movement[pygame.K_DOWN]:
            yposition = groundheight + 40
            imagenumber = -1
            if not backgroundlock:

                backx += 5
                back1x += 5
                back2x += 5
                xposition -= 4
            
                

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
            if not backgroundlock:

                backx += 5
                back1x += 5
                back2x += 5
                xposition -= 4
        else:
            imagenumber = 0
            if not backgroundlock:

                backx += 5
                back1x += 5
                back2x += 5
                xposition -= 4
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

            
# dictdinoy = {dinowalk1 :groundheight + mariosize[1] - dinosize[1], dinowalk2 :groundheight + mariosize[1] - dinosize[1], dinostand:groundheight + mariosize[1] - dinosize[1], flyingdino: groundheight + mariosize[1]/2 - flysize[1]}
    
        if not dinoonscreen:
            whichdino = random.randint(0, len(dinoimagelist) - 1)

            dinox = display_width + 10

            dinoy = groundheight + mariosize[1] - dinosize[1]
            
                
                
            dinoonscreen = True    
        

        
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
            dinocount += 1
            

        
        
        background([snowbackground, snowbackground, snowbackground], [backx, back1x, back2x], [backy, back1y, back2y])

        gameDisplay.blit(imagelist[imagenumber], [xposition, yposition])
        lives(numberoflives, display_width - 300, 10)
        mariowidth = imagelist[imagenumber].get_size()
        dinowidth = dinoimage.get_size()
        
        checkx1 = xposition + mariowidth[0] >= dinox
        checkx2 = xposition + mariowidth[0] <= dinox +  dinowidth[0]
        checky1 = yposition + mariowidth[1] >= dinoy
        checky2 = yposition + mariowidth[1] <= dinoy + dinowidth[1]

        
        if not backgroundlock and checkx1 and checkx2 and checky1 and checky2 and heartcheck:
            heartcheck = False
            numberoflives -= 1
            xposition -= 6
            currenttime = time.time()

        if dinocount >= 5:
            backgroundlock = True
        
        if dinoonscreen and not backgroundlock:
            gameDisplay.blit(dinoimage, [dinox, dinoy])

        pygame.display.update()
        gameDisplay.fill(white)
    
        if not heartcheck and not dinoonscreen: 
            heartcheck = True
            
        if numberoflives <= 0:
            print "LOL U DED"
            quit_function()
               
        if backgroundlock:
            walk(xposition, display_width + 30, yposition, walklistright, "Right", backgroundimagelist = [snowbackground, snowbackground, snowbackground], backgroundx = [backx, back1x, back2x], backgroundy = [backy, back1y, back2y])            
            pygame.display.update()
            
            iceage(2)
            return
  
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
    cheat = False
    while gameon:
        clock.tick(fps)
        movement = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_function()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit_function()
                    
            
                if event.key == pygame.K_p:
                    cheat = pause_screen()

        if cheat:
            gameon = False
        
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
            if backgroundlock and xposition >= display_width/2 - 50 and not stage4done:
                stringstuff = firstintro(4)
                stage4done = True
                if stringstuff == 'done':
                    return
            if stage4done:
                background([cave], [0], [0])
                gameon = False
                return
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

    
time_increment = 0.4

ocean = pygame.image.load('sea.png')
oceanY = display_height - 50

MAXPOWER = 75
GRAVITY = 5

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
        if screen and (self.centre[1] >= oceanY or self.centre[0] >= display_width): return True
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
    else: location = (display_width - length - 5, 5)
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
        self.loc = [display_width - 50 - self.image_size[0], oceanY - self.image_size[1] + 15]
        self.gunBase = [self.loc[0] + 50, self.loc[1] + 4*self.image_size[1]//5 + 10]
        self.gunTip[0] = int(self.gunBase[0] - self.gunLength * cos(radians(self.theta)))
        self.gunTip[1] = int(self.gunBase[1] - self.gunLength * sin(radians(self.theta)))

    def shoot(self):
        global projectile
        if projectile == None: return
        vel_tot = random.randint(MAXPOWER//2, MAXPOWER)
        distance = abs(aip.loc[0] + aip.image_size[0]//2 - self.gunTip[0]) + random.randint(-aip.image_size[0]//2, aip.image_size[0]//2)
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

def shipGameLoop():
    global aip, projectile
    cheat = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_p:
                    cheat = pause_screen()
                    if cheat:
                        return
                elif event.key == pygame.K_SPACE:
                    if projectile[0] == None:
                        projectile[0] = Projectile(aip)
                        if projectile[1] == None:
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
                    if enemy.hp <= 0:
                        enemy.sunk = True
                        return 
                    projectile[0] = None
                elif damage != False and i == 1:
                    aip.loc[0] -= projectile[1].velocity[0]/MAXPOWER
                    aip.hp -= damage
                    if aip.hp <= 0:
                        shipGameLoop()
                    projectile[1] = None
                elif projectile[i].collide(screen = True):
                    projectile[i] = None
    
        drawAll()
        
        clock.tick(25)
        
def NPSK():
    mariox = display_width/2
    background([audi], [0], [0])
    marioheight = -100
    walk(0, display_width//2, display_height//2 + 100, walklistright, 'Right', backgroundimagelist = [audi],
         backgroundx = [0], backgroundy = [0]) 
##    while marioheight < display_height/2:
##        for event in pygame.event.get():
##            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
##                quit_function()
##        clock.tick(50)
##        theimage = pygame.transform.rotate(duck, marioheight)
##        background([audi, walklistright[0]], [0, mariox], [0, marioheight])
##
##        pygame.display.update()
##
##        gameDisplay.fill(white)
##        if marioheight + 30 <= display_height/2:
##            marioheight += 30
##        else:
##            marioheight = display_height/2
##    background([audi, walklistright[0]], [0, mariox], [0, marioheight])
    pygame.display.update()
    dialoguebox("That's all folks!", "Medium", [display_width//2, display_height//2 + 100])
    time.sleep(0.6)
    pygame.quit()
    quit()


#put list of functions for different levels here
#This simplifies code. We also don't need to hunt for relevent function when adding new levels.

CURRENTLEVEL = gameintro()
if CURRENTLEVEL == 1:
    firstgameloop()
    vortex()
    iceage()
    CURRENTLEVEL += 1
if CURRENTLEVEL == 2:
    vortex()
    launchgame()
    CURRENTLEVEL += 1
if CURRENTLEVEL == 3:
    vortex()
    brickbreakerintro()
    game = BrickBreaker()
    game.gameLoop()
    CURRENTLEVEL += 1
vortex()
NPSK()
