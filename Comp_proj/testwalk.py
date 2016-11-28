import pygame
import time
pygame.init()


# Colours:
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
darkgreen = (0, 155, 0)



width = 900
height = 600
heightofletters = height/2 - 100
letterrange = [1, 2]

# Images:
standstraight = pygame.image.load("C:/PythonX/images/standstraight.png")
walkimageright1 = pygame.image.load("C:/PythonX/images/walkimage1.png")
walkimageright2 = pygame.image.load("C:/PythonX/images/walkimage2.png")
walkimageright3 = pygame.image.load("C:/PythonX/images/walkimage3.png")
walkimageright4 = pygame.image.load("C:/PythonX/images/walkimage4.png")
walkimageright5 = pygame.image.load("C:/PythonX/images/walkimage5.png")
walkimageright6 = pygame.image.load("C:/PythonX/images/walkimage6.png")
walkimageright7 = pygame.image.load("C:/PythonX/images/walkimage7.png")


walkimageleft1 = pygame.transform.flip(walkimageright1, True, False)
walkimageleft2 = pygame.transform.flip(walkimageright2, True, False)
walkimageleft3 = pygame.transform.flip(walkimageright3, True, False)
walkimageleft4 = pygame.transform.flip(walkimageright4, True, False)
walkimageleft5 = pygame.transform.flip(walkimageright5, True, False)
walkimageleft6 = pygame.transform.flip(walkimageright6, True, False)
walkimageleft7 = pygame.transform.flip(walkimageright7, True, False)

swordimage = pygame.image.load("C:/PythonX/images/sword.png")


nounlist = [swordimage]
walklistright = [standstraight, walkimageright1, walkimageright2, walkimageright3, walkimageright4, walkimageright5, walkimageright6, walkimageright7]
walklistleft = [standstraight, walkimageleft1, walkimageleft2, walkimageleft3, walkimageleft4, walkimageleft5, walkimageleft6, walkimageleft7]
total_number_of_images = len(walklistright)

# Text sizes:
smallfont = pygame.font.SysFont("comicsansms", 15)
smallmedfont = pygame.font.SysFont("comicsansms", 30)
medfont = pygame.font.SysFont("comicsansms", 50)
mediumlargefont = pygame.font.SysFont("comicsansms", 60)
largefont = pygame.font.SysFont("comicsansms", 80)



gameDisplay = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
gameDisplay.fill(white)


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

def writing(text, colour, ht = -100, size = "smallmed", centre = False,
            requiredwidth = 20, timegap = 0.1):
    numberofspaces = ""
    
    for letters in text:
        msgbox(numberofspaces + letters, colour, ht, size, centre, requiredwidth)
        pygame.display.update()
        numberofspaces += "   "
        time.sleep(timegap)

def button(textinbutton, x, y, width1, height1, inactivecolour,
           activecolour, action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width1 > cur[0] > x and y + height1 > cur[1] > y:
        
        pygame.draw.rect(gameDisplay, activecolour, (x, y, width1,
                                                     height1))
    
        if click[0] == 1 and action <> None:

            if action == "quit":
                pygame.quit()
                quit()
            if action == "Ready":
                action = True
            
            
            return action
    else:
        pygame.draw.rect(gameDisplay, inactivecolour, (x, y, width1, height1))
        
    text_button(textinbutton, black, x, y, width1, height1)
    pygame.display.update()


def objectpickup(image, manxposition, manyposition, theimagenumber = 0, direction = "Right"):

    if theimagenumber == 0:
        xchange, ychange, angle = +70, +80, 330


    elif direction == "Right":
        if theimagenumber == 1 or theimagenumber == 2 or theimagenumber == 5:
            xchange, ychange, angle = 60, 10, 45

        elif theimagenumber == 3:
            xchange, ychange, angle = 50, 110, 310
        elif theimagenumber == 6:
            xchange, ychange, angle = 40, 140, 270
        elif theimagenumber == 4 or theimagenumber == 7:
            xchange, ychange, angle = +98, 33, 0

    elif direction == "Left":
        if theimagenumber == 1 or theimagenumber == 2 or theimagenumber == 5:
            xchange, ychange, angle = 5, 20, 360-45
        elif theimagenumber == 3:
            xchange, ychange, angle = 40, 110, 360-310
        elif theimagenumber == 6:
            xchange, ychange, angle = 15, 125, 360 - 270
        elif theimagenumber == 4 or theimagenumber == 7:
            xchange, ychange, angle = 25, 33, 0
            
        
        




    
        
    theactualimage = pygame.transform.rotate(image, angle)

        
    gameDisplay.blit(theactualimage, (manxposition + xchange, manyposition + ychange))


def storyline(text, word, printheight = heightofletters, thetimegap = 0.05):
    requiredwidth = 20
    writing(text, black, ht = heightofletters, timegap = thetimegap, requiredwidth = requiredwidth)
    text = " " + text
    length = len(text)
    for i in range(length - len(word)):
        if text[i] == word[0] and text[i-1] == " ":
            count = 1
            for k in range(1, len(word)):
                if text[i+k] == word[k]:
                    count += 1
                else:
                    break

            if count == len(word):
                index = range(i, i + len(word))
    countspace = 0
    for i in range(length):
        if i < index[0]: 
            if text[i].isspace():
                countspace += 1

        else:
            break

    if length/5 <= index[-1] < length * 2/5.0:
        letterrange = [requiredwidth + (index[0] * 10), requiredwidth + (index[len(index)-1] * 11)]
    elif index[-1] >= length * 4/5.0:
        letterrange = [requiredwidth + (index[0] * 13), requiredwidth + (index[len(index)-1] * 13)]
    elif length * 3/5.0 > index[-1] >= length * 2/5.0:
        letterrange = [requiredwidth + (index[0] * 11), requiredwidth + (index[len(index)-1] * 12)]
        
    elif length * 4/5.0 > index[-1] >= length * 3/5.0:
        letterrange = [requiredwidth + (index[0] * 12), requiredwidth + (index[len(index)-1] * 12)]   


    else:
        letterrange = [requiredwidth + (index[0] * 9), requiredwidth + (index[len(index)-1] * 10)]
    return letterrange[0], letterrange[1]
    

    
    
    
        



def drawman(xposition, yposition, imagenumber, direction = "Right"):
    if direction == "Right":
        theimage = walklistright[imagenumber]
    else:
        theimage = walklistleft[imagenumber]
    gameDisplay.blit(theimage, [xposition, yposition])


    

def gameintro():
    intro = True
    gameDisplay.fill(white)
    pygame.display.update()


    initialwidth = -100
    heightofletters = height/2 - 100
    
    imagenumber = 0
    changewidth = 0
    while intro:

        Ready = False
        while not Ready:
            msgbox("Adjust the Screen and then click Start", red, ht = -100, size = "medium")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                    pygame.quit()
                    
            Ready = button("Start", width/2 - 50, height/2 - 50, 100, 100, green, darkgreen, action = "Ready")

        gameDisplay.fill(white)
                
                
                
##        clock.tick(10)
##        
##        writing("Welcome, oh great, .... erm ... computer player!", red, centre = False, requiredwidth = 50) 
##        time.sleep(0.2)
##        gameDisplay.fill(white)
##
##        
##        writing("Meet the greatest warrior of all time... ", red, ht = -100, size = "smallmed", centre = False, requiredwidth = 50)
##        writing("The all powerful...",  red, ht = -50, size = "smallmed", centre = False, requiredwidth = 50)
##        writing("Totally awesome...", red, ht = 0, size = "smallmed", centre = False, requiredwidth = 50) 
##        writing("Amazingest superhero ever... ", red, ht = 50, size = "smallmed", centre = False, requiredwidth = 50)
##        writing("Stan!", red, ht = 100, size = "smallmed", centre = False, requiredwidth = 50)
##        pygame.display.update()
##        time.sleep(2)
##        gameDisplay.fill(white)
##
##        
##        writing("...", red, ht = -100, size = "large", centre = True, timegap = 0.4) 
##        pygame.display.update()
##
        
##        time.sleep(2)
##        gameDisplay.fill(white)
##        writing("Erm... Stan...? That's your cue Stan...", red , ht = -100, size = "small", centre = False, requiredwidth = 50)
##        
##        time.sleep(2)
##        gameDisplay.fill(white)
##
##
##        
##        writing("...", red, ht = -100, size = "large", centre = True, timegap = 0.4) 
##        pygame.display.update()
##        time.sleep(2)
##
        gameDisplay.fill(white)
        msgbox("STAN!", red, ht = -100, size = "large")
        pygame.display.update()
        time.sleep(2)
        
        while initialwidth < 50:
            clock.tick(20)
            changewidth += 15
            initialwidth += changewidth
            imagenumber += 1
            drawman(initialwidth, heightofletters, imagenumber, direction = "Right")
            pygame.display.update()
            gameDisplay.fill(white)

        drawman(initialwidth, heightofletters, imagenumber = 0)

        writing("Hmmm... the \" knights \" sure are getting shorter...", red, ht = -250, size = "small", timegap = 0.05)
        pygame.display.update()
        time.sleep(0.2)
        gameDisplay.fill(white)
        drawman(initialwidth, heightofletters, imagenumber = 0)
        pygame.display.update()
        msgbox("Anyway!", red, ht = -250, size = "large")
        writing("Control Stan and help him get through his quest...", red, ht = -175, size = "smallmed")
        pygame.display.update()
        gameDisplay.fill(white)
        
        drawman(initialwidth, heightofletters, imagenumber = 0)
        writing("Press the Right and Left arrow keys to move", red, ht = -150, size = "smallmed")
        Testwalk = True
        TestRight, TestLeft = 0, 0
        direction = "Right"
        fps = 10
        while Testwalk:
            
            changewidth = 0
            clock.tick(fps)
            
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            movement = pygame.key.get_pressed()
                    
            if movement[pygame.K_RIGHT] == True:
                changewidth += 15
                imagenumber += 1
                direction = "Right"
                TestRight += 1
                
                    
                    
            elif movement[pygame.K_LEFT] == True:
                changewidth -= 15
                imagenumber += 1
                direction = "Left"
                TestLeft += 1

            else:
                imagenumber = 0
            if initialwidth < 0 and direction == "Left" or initialwidth >= width - 130 and direction == "Right":
                changewidth, imagenumber = 0, 0
            initialwidth += changewidth
            
            if imagenumber >= total_number_of_images:
                imagenumber = 1
            
            
            drawman(initialwidth, heightofletters, imagenumber, direction)
    ##        print imagenumber
            
                    
                    
                    
        
        
            pygame.display.update()
            gameDisplay.fill(white)
##            print TestRight, TestLeft
            if TestRight > 5 and TestLeft > 5:
                if initialwidth == 50:
                    Testwalk = False
            elif TestRight > 5:
                msgbox("Now Try left: ", red, 200, size = "smallmed")
            elif TestLeft > 5:
                msgbox("Now Try right: ", red, 200, size = "smallmed")
                    

        intro = False
        
    gameDisplay.fill(white)
    imagenumber = 0
    drawman(initialwidth, heightofletters, imagenumber)
    pygame.display.update()

    gameloop()




# All scenes here:

def Scene1():
    gameDisplay.fill(white)
    letterrange[0], letterrange[1] = storyline("Once upon a time a simple boy found a sword lying on the ground", "sword", thetimegap = 0.01)            

    return letterrange[0], letterrange[1]


            
    
def Scene2():
    gameDisplay.fill(white)
    letterrange[0], letterrange[1] = storyline("He had no idea how it worked...", "idea", thetimegap = 0.01)            

    return letterrange[0], letterrange[1]

    


    

def gameloop():
    gameon = True
    print "G"
    initialwidth = 50
    
    fps = 10
    
    imagenumber = 0
    direction = "Right"
    wordsappear = Pickup = Newscenechosen = False
    Scenenumber = Newscenenumber = 1
    while gameon:
        changewidth = 0
        clock.tick(fps)
              
        
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            

        movement = pygame.key.get_pressed()
                
        if movement[pygame.K_RIGHT] == True:
            changewidth += 15
            imagenumber += 1
            direction = "Right"
            
                
                
        elif movement[pygame.K_LEFT] == True:
            changewidth -= 15
            imagenumber += 1
            direction = "Left"

        elif movement[pygame.K_DOWN] == True:

            if letterrange[0] <= initialwidth <= letterrange[1]:
                Pickup = True
                
        

        else:
            imagenumber = 0


        
        
        if initialwidth < 0 and direction == "Left" or initialwidth >= width - 130 and direction == "Right":
            changewidth = 0
            imagenumber = 0
        initialwidth += changewidth
        
        if imagenumber >= total_number_of_images:
            imagenumber = 1

        drawman(initialwidth, heightofletters, imagenumber, direction)

        while not wordsappear:
            if Scenenumber == 1:
                letterrange[0], letterrange[1] = Scene1()
            wordsappear = True

                
       
        if Newscenechosen and initialwidth >= width - 130:
        
            if Scenenumber == 2:
                letterrange[0], letterrange[1] = Scene2()
            initialwidth = 50
        
            
             

        

        
        
        if Pickup:
            if Scenenumber == 2:
                print "Idea!"
            objectpickup(swordimage, initialwidth, heightofletters, imagenumber, direction)
            if not Newscenechosen:
                Newscenenumber = Scenenumber + 1
                Newscenechosen = True
            
                wordsappear = False
        
                    
        Scenenumber = Newscenenumber
        
        pygame.display.update()
        gameDisplay.fill(white, rect =[0, 0, width, height- (heightofletters - 63)])

gameloop()




