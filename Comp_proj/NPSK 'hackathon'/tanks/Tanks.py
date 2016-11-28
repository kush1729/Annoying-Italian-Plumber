import pygame, random
pygame.init()

#Colours

white = (255, 255, 255)
black = (0, 0, 0)
grey = (200, 200, 200)
red = (200, 0, 0)
light_red = (255, 0, 0)
yellow = (200, 200, 0)
light_yellow = (255, 255, 0)
blue = (0, 0, 255)
green = (34, 177, 76)
light_green = (0, 255, 0)

#Constants

FPS = 25
display_width, display_height = 800, 600
smallfont = pygame.font.SysFont("comicsansms", 20)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((display_width, display_height))
icon = pygame.image.load('tank.png')
pygame.display.set_icon(icon)
fire_sound = pygame.mixer.Sound('Shooting.wav')
explosion_sound = pygame.mixer.Sound('Explosion.wav')

ground_height = 35
tankWidth = 40
tankHeight = 20
turretWidth = 5
wheelWidth = 5

pygame.display.set_caption('TANKS')

#Basic Game Ware Functions 

def text_objects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()

def text_to_button(msg, color, btnx, btny, btnwidth, btnheight, size = "small"):
    textSurf , textRect = text_objects(msg, color, size)
    textRect.center = ((btnx + (btnwidth / 2)), (btny + (btnheight / 2)))
    gameDisplay.blit(textSurf, textRect)

def message_to_screen(msg, color, y_displace = 0, size = "small"):
    textSurf , textRect = text_objects(msg, color, size)
    textRect.center = (display_width / 2), (display_height / 2) + y_displace
    gameDisplay.blit(textSurf, textRect)

def button(text, x, y, width, height, inactive, active, action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        if click[0] == 1 and action != None:
            if action == 'quit':
                pygame.quit()
                quit()
            if action == 'controls':
                game_controls()
            if action == 'play':
                gameLoop()
        pygame.draw.rect(gameDisplay, active, (x, y, width, height))
    else:
        pygame.draw.rect(gameDisplay, inactive, (x, y, width, height))
    text_to_button(text, black, x, y, width, height)

def score(score):
    text = smallfont.render("Score: " + str(score), True, black)
    gameDisplay.blit(text, (0,0))

def pause():
    paused = True
    message_to_screen("Paused", black, -100, "large")
    message_to_screen("Press C to continue or Q to quit",
                          black, 25)
    pygame.display.update()
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        clock.tick(5)

#Game Logic And Game Play Functions

def tank(x, y, turPos):
    x = int(x)
    y = int(y)
    possibleTurrets = [(x - 27, y - 2), (x - 26, y - 5),
                       (x - 25, y - 8), (x - 23, y - 12),
                       (x - 20, y - 14), (x - 18, y - 15),
                       (x - 15, y - 17), (x - 13, y - 19),
                       (x - 11, y - 21)]
    pygame.draw.circle(gameDisplay, black, (x, y), int(tankHeight / 2))
    pygame.draw.rect(gameDisplay, black, (x - tankHeight, y, tankWidth, tankHeight))        
    pygame.draw.line(gameDisplay, black, (x, y), possibleTurrets[turPos],
                     turretWidth)
    startX = 15
    for i in range(7):
        pygame.draw.circle(gameDisplay, black, (x - startX, y + 20), wheelWidth)
        startX -= 5
    return possibleTurrets[turPos]

def enemy_tank(x, y, turPos):
    x = int(x)
    y = int(y)
    possibleTurrets = [(x + 27, y - 2), (x+26, y - 5),
                       (x+25, y - 8), (x+23, y - 12),
                       (x+20, y - 14), (x+18, y - 15),
                       (x+15, y - 17), (x+13, y - 19),
                       (x+11, y - 21)]
    pygame.draw.circle(gameDisplay, black, (x, y), int(tankHeight / 2))
    pygame.draw.rect(gameDisplay, black, (x - tankHeight, y, tankWidth, tankHeight))        
    pygame.draw.line(gameDisplay, black, (x, y), possibleTurrets[turPos],
                     turretWidth)
    startX = 15
    for i in range(7):
        pygame.draw.circle(gameDisplay, black, (x - startX, y + 20), wheelWidth)
        startX -= 5
    return possibleTurrets[turPos]

def game_controls():
    gcont = True
    while gcont:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                                        
        gameDisplay.fill(white)
        message_to_screen("CONTROLS", green,-100, "large")
        message_to_screen("Fire: Spacebar",
                          black, -20)
        message_to_screen("Move Turret: Up and Down arrows",
                          black, 10)
        message_to_screen("Move Tank: Left and Right arrows",
                          black, 40)
        message_to_screen("Pause: P",
                          black, 70, "small")
        
        button("play", 150, 500, 100, 50, green, light_green, "play")
        button("quit", 550, 500, 100, 50, red, light_red, "quit")
        
        pygame.display.update()
        clock.tick(15)

def barrier(xlocation, randomHeight, barrier_width):
    pygame.draw.rect(gameDisplay, black,
                     [xlocation, display_height - randomHeight,
                      barrier_width, randomHeight])    

def power(level):
    text = smallfont.render("Power: " + str(level) + "%", True, black)
    gameDisplay.blit(text, [display_width / 2, 0])

def explosion(x, y, size = 50):
    pygame.mixer.Sound.play(explosion_sound)
    explode = True
    while explode:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        startPoint = x, y
        colorChoices = [red, light_red, yellow, light_yellow]
        magnitude = 1
        while magnitude < size:
            exploding_bit_x = x + random.randrange(-magnitude, magnitude)
            exploding_bit_y = y + random.randrange(-magnitude, magnitude)
            pygame.draw.circle(gameDisplay, colorChoices[random.randrange(0,4)],
                               (exploding_bit_x, exploding_bit_y), random.randrange(1, 5))
            magnitude += 1
            pygame.display.update()
            clock.tick(100)
        explode = False
 
def fireShell(xy, tankx, tanky, turPos, fire_power, xlocation,
              barrier_width, randomHeight, etankx, etanky):
    pygame.mixer.Sound.play(fire_sound)
    damage = 0
    fire = True
    startingShell = list(xy)
    while fire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.draw.circle(gameDisplay, red, startingShell, 5)    
        startingShell[0] -= (12 - turPos)*2
        startingShell[1] += int(((startingShell[0] - xy[0]) * 0.015 / (fire_power / 50.0)) ** 2 - (turPos + turPos / (12 - turPos)))
        pygame.display.update()
        clock.tick(60)
        if startingShell[1] >= display_height - ground_height:
            hit_x = int((startingShell[0] * (display_height - ground_height)) / startingShell[1])
            hit_y = int(display_height - ground_height)
            if etankx + 10 > hit_x > etankx - 10:
                damage = 25
            elif etankx + 15 > hit_x > etankx - 15:
                damage = 18
            elif etankx + 20 > hit_x > etankx - 20:
                damage = 10
            elif etankx + 25 > hit_x > etankx - 25:
                damage = 5 
            explosion(hit_x, hit_y)
            fire = False
        if xlocation <= startingShell[0] <= (xlocation + barrier_width):
            if startingShell[1] >= display_height - randomHeight:
                hit_x = int(startingShell[0])
                hit_y = int(startingShell[1])
                explosion(hit_x, hit_y)
                fire = False
    return damage

def e_fireShell(xy, tankx, tanky, turPos, fire_power,
              xlocation, barrier_width, randomHeight, ptankx, ptanky):
    pygame.mixer.Sound.play(fire_sound)
    damage = 0
    currentPower = 30
    power_found = False
    while not power_found:
        currentPower += 1
        if currentPower > 100:
            power_found = True
        fire = True
        startingShell = list(xy)
        while fire:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()    
            startingShell[0] += (12 - turPos)*2
            startingShell[1] += int(((startingShell[0] - xy[0]) * 0.015 / (currentPower / 50.0)) ** 2 - (turPos + turPos / (12 - turPos)))
            if startingShell[1] >= display_height - ground_height:
                hit_x = int((startingShell[0] * (display_height - ground_height)) / startingShell[1])
                hit_y = int(display_height - ground_height)
                if ptankx + 15 > hit_x > ptankx - 15:
                    power_found = True
                fire = False
            if xlocation <= startingShell[0] <= (xlocation + barrier_width):
                if startingShell[1] >= display_height - randomHeight:
                    fire = False
    fire_power = random.randrange(int(currentPower * 0.9),
                                  int(currentPower * 1.1))     
    fire = True
    startingShell = list(xy)
    while fire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.draw.circle(gameDisplay, red, startingShell, 5)    
        startingShell[0] += (12 - turPos)*2
        startingShell[1] += int(((startingShell[0] - xy[0]) * 0.015 / (fire_power / 50.0)) ** 2 - (turPos + turPos / (12 - turPos)))
        pygame.display.update()
        clock.tick(60)
        if startingShell[1] >= display_height - ground_height:
            hit_x = int((startingShell[0] * (display_height - ground_height)) / startingShell[1])
            hit_y = int(display_height - ground_height)
            if ptankx + 10 > hit_x > ptankx - 10:
                damage = 25
            elif ptankx + 15 > hit_x > ptankx - 15:
                damage = 18
            elif ptankx + 20 > hit_x > ptankx - 20:
                damage = 10
            elif ptankx + 25 > hit_x > ptankx - 25:
                damage = 5
            explosion(hit_x, hit_y)
            fire = False
        if xlocation <= startingShell[0] <= (xlocation + barrier_width):
            if startingShell[1] >= display_height - randomHeight:
                hit_x = int(startingShell[0])
                hit_y = int(startingShell[1])
                explosion(hit_x, hit_y)
                fire = False
    return damage

def game_over():
    gameover = True
    while gameover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                                        
        gameDisplay.fill(white)
        message_to_screen("Game Over",
                          green,-100, "large")
        message_to_screen("You died.",
                          black, -30)
        button("play again", 150, 500, 150, 50, green, light_green, "play")
        button("controls", 350, 500, 100, 50, yellow, light_yellow,
               "controls")
        button("quit", 550, 500, 100, 50, red, light_red, "quit")
        pygame.display.update()
        clock.tick(15)            

def player_win():
    win = True
    while win:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                                        
        gameDisplay.fill(white)
        message_to_screen("You won!",
                          green,-100, "large")
        message_to_screen("Congratulations",
                          black, -30)
        button("play again", 150, 500, 100, 50, green, light_green,
               "play")
        button("controls", 350, 500, 100, 50, yellow, light_yellow,
               "controls")
        button("quit", 550, 500, 100, 50, red, light_red, "quit")
        pygame.display.update()
        clock.tick(15)
    
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                                        
        gameDisplay.fill(white)
        message_to_screen("Welcome to Tanks",
                          green,-100, "large")
        message_to_screen("The objective is to shoot and destroy the enemy tank before they destroy you.",
                          black, -30)
        message_to_screen("The more enemies you destroy, the harder they get.",
                          black, 10)
        button("play", 150, 500, 100, 50, green, light_green, "play")
        button("controls", 350, 500, 100, 50, yellow, light_yellow,
               "controls")
        button("quit", 550, 500, 100, 50, red, light_red, "quit")
        pygame.display.update()
        clock.tick(15)

def health_bars(player_health, enemy_health):
    if player_health > 66:
        p_color = light_green
    elif player_health > 33:
        p_color = light_yellow
    else:
        p_color = light_red
    if enemy_health > 66:
        e_color = light_green
    elif enemy_health > 33:
        e_color = light_yellow
    else:
        e_color = light_red
    pygame.draw.rect(gameDisplay, grey, (680, 25, 100, 25))
    pygame.draw.rect(gameDisplay, grey, (20, 25, 100, 25))
    pygame.draw.rect(gameDisplay, p_color, (680, 25, player_health, 25))
    pygame.draw.rect(gameDisplay, e_color, (20, 25, enemy_health, 25))
        
def gameLoop():
    gameExit = False
    gameOver = False
    mainTankX = display_width * 0.9
    mainTankY = display_height * 0.9
    enemyTankX = display_width * 0.1
    enemyTankY = display_height * 0.9
    xlocation = (display_width / 2) + random.randint(-0.1*display_width, 0.1 * display_width)
    randomHeight = random.randrange(display_height * 0.1, display_height*0.5)
    barrier_width = 50
    tankMove = 0
    currentTurPos = 0
    changeTur = 0
    fire_power = 50
    powerChange = 0
    player_health = enemy_health = 100
    while not(gameExit):
        if gameOver == True:
            message_to_screen("Game over", red, -50, "large")
            message_to_screen("press C to play again or Q to quit",
                              black, 50, size = "small" )
            pygame.display.update()
            
        while gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()
         
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tankMove = -5
                elif event.key == pygame.K_RIGHT:
                    tankMove = 5
                elif event.key == pygame.K_UP:
                    changeTur = 1
                elif event.key == pygame.K_DOWN:
                    changeTur = -1
                elif event.key == pygame.K_SPACE:
                    damage = fireShell(gun, mainTankX, mainTankY,
                              currentTurPos, fire_power,
                              xlocation, barrier_width,
                              randomHeight, enemyTankX, enemyTankY)
                    enemy_health -= damage
                    possibleMovement = ['f', 'r']
                    moveIndex = random.randrange(0,2)
                    for x in range(random.randrange(0,10)):
                        if display_width * 0.3 > enemyTankX > display_width * 0.03:
                            if possibleMovement[moveIndex] == 'f':
                                enemyTankX += 5
                            elif possibleMovement[moveIndex] == 'r':
                                enemyTankX -= 5
                            gameDisplay.fill(white)
                            health_bars(player_health, enemy_health)
                            gun = tank(mainTankX, mainTankY, currentTurPos)
                            enemy_gun = enemy_tank(enemyTankX, enemyTankY, 8)
                            power(fire_power)
                            barrier(xlocation, randomHeight, barrier_width)
                            gameDisplay.fill(green, rect = [0, display_height - ground_height,
                                                            display_width, ground_height])
                            pygame.display.update()
                            clock.tick(FPS)
                    damage = e_fireShell(enemy_gun, enemyTankX,
                                         enemyTankY, 8, 50,
                                         xlocation, barrier_width,
                                         randomHeight, mainTankX,
                                         mainTankY)
                    player_health -= damage
                elif event.key == pygame.K_a:
                    powerChange = -1
                elif event.key == pygame.K_d:
                    powerChange = 1
                elif event.key == pygame.K_p:
                    pause()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    tankMove = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    changeTur = 0
                elif event.key == pygame.K_a or event.key == pygame.K_d:
                    powerChange = 0
        gameDisplay.fill(white)
        health_bars(player_health, enemy_health)
        gun = tank(mainTankX, mainTankY, currentTurPos)
        enemy_gun = enemy_tank(enemyTankX, enemyTankY, 8)
        mainTankX += tankMove
        currentTurPos += changeTur
        fire_power += powerChange
        if player_health < 1:
            game_over()
        elif enemy_health < 1:
            player_win()
        if not fire_power in range(0, 101):
            fire_power -= powerChange
        if not currentTurPos in range(0, 9):
            currentTurPos -= changeTur
        if mainTankX - (tankWidth / 2) < xlocation + barrier_width:
            mainTankX -= tankMove
        power(fire_power)
        barrier(xlocation, randomHeight, barrier_width)
        gameDisplay.fill(green, rect = [0, display_height - ground_height,
                                        display_width, ground_height])
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    quit()
    
game_intro()
gameLoop()
