
#importing librarires
import pygame,sys,math


from entitiesv2 import *
from weapons import *

#GENERAL NOTE: remember that when y value increases, the image actually moves down, not up, and vise versa

clock = pygame.time.Clock() #getting frame rate/defining frame rate as a variable

from pygame.locals import * #importing everything from pygame
#---------------------------------------------------------------------------------------------------------------------
pygame.init() #initialises/creates an instance of pygame


''''''''''''''''''''
'''Loading in and'''
'''scaling up all'''
'''of the images '''
''''''''''''''''''''

x=1920
y=1080
#y = 0 is the top of the screen, x = 0 is the very left of the screen
SCREEN = pygame.display.set_mode((x, y))
pygame.display.set_caption("Menu")


BG = pygame.image.load("Background.png").convert_alpha() #convert() makes it quicker when loading images, just a general function used after loading images to increase speed
BG = pygame.transform.scale(BG,(x,y)) #scaling the background image to the size of the screen itself

#getting all  the buttons for the menu
PLAY_button = pygame.image.load("PLAY button.png").convert_alpha()
PLAY_button = pygame.transform.scale(PLAY_button,(600,400))

PLAY_hover = pygame.image.load("PLAY hover.png").convert_alpha()
PLAY_hover = pygame.transform.scale(PLAY_hover,(600,400))

PAUSE_button = pygame.image.load("PAUSE button.png").convert_alpha()
PAUSE_button = pygame.transform.scale(PAUSE_button,(500,300))

PAUSE_hover = pygame.image.load("PAUSE hover.png").convert_alpha()
PAUSE_hover = pygame.transform.scale(PAUSE_hover,(500,300))

CONTINUE_button = pygame.image.load("CONTINUE button.png").convert_alpha()
CONTINUE_button = pygame.transform.scale(CONTINUE_button,(900,600))

CONTINUE_hover = pygame.image.load("CONTINUE hover.png").convert_alpha()
CONTINUE_hover = pygame.transform.scale(CONTINUE_hover,(900,600))

QUIT_button = pygame.image.load("QUIT button.png").convert_alpha()
QUIT_button = pygame.transform.scale(QUIT_button,(900,600))

QUIT_hover = pygame.image.load("QUIT hover.png").convert_alpha()
QUIT_hover = pygame.transform.scale(QUIT_hover,(900,600))

OPTIONS_button = pygame.image.load("OPTIONS button.png").convert_alpha()
OPTIONS_button = pygame.transform.scale(OPTIONS_button,(1350,750))

OPTIONS_hover = pygame.image.load("OPTIONS hover.png").convert_alpha()
OPTIONS_hover = pygame.transform.scale(OPTIONS_hover,(1350,750))


PLAYER = pygame.image.load("PLAYER.png").convert_alpha()
PLAYER = pygame.transform.scale(PLAYER,(80,140))

PLAYER_LEFT = pygame.transform.flip(PLAYER,True,False)



iron_armour_right = pygame.image.load("iron armour right.png").convert_alpha()
iron_armour_right = pygame.transform.scale(iron_armour_right,(80,140))

iron_armour_left = pygame.transform.flip(iron_armour_right,True,False)



wizard_cat_right = pygame.image.load("wizard cat right.png").convert_alpha()
wizard_cat_right = pygame.transform.scale(wizard_cat_right,(102,1350/28))

wizard_cat_left = pygame.transform.flip(wizard_cat_right,True,False)



heart = pygame.image.load("HEART.png").convert_alpha()
heart = pygame.transform.scale(heart,(200,200))


noheart = pygame.image.load("NO HEART.png").convert_alpha()
noheart = pygame.transform.scale(noheart,(200,200))

ability_button = pygame.image.load("ability.png").convert_alpha()
ability_button = pygame.transform.scale(ability_button,(500,500))

ability_cd = pygame.image.load("ability_cd.png").convert_alpha()
ability_cd = pygame.transform.scale(ability_cd,(500,500))

crosshair = pygame.image.load("crosshair.png").convert_alpha()
crosshair = pygame.transform.scale(crosshair,(1000,1000))

shotgun_gun = pygame.image.load("shotgun.png").convert_alpha()
shotgun_gun = pygame.transform.scale(shotgun_gun,(200,25))

shotgun_gun_left = pygame.transform.flip(shotgun_gun,True,False)





snake_left = pygame.image.load("snake left.png").convert_alpha()
snake_left = pygame.transform.scale(snake_left,(150,150))

snake_right = pygame.transform.flip(snake_left,True,False)

ally_left = pygame.image.load("ally left.png").convert_alpha()
ally_left = pygame.transform.scale(ally_left,(150,150))

ally_right = pygame.transform.flip(ally_left,True,False)






FLOOR = pygame.image.load("FLOOR.png").convert_alpha()
FLOOR = pygame.transform.scale(FLOOR,(131,60))

DIRT = pygame.image.load("DIRT.png").convert_alpha()
DIRT = pygame.transform.scale(DIRT,(131,60))

PLAYER_POS = [200,500]
PLAYER_hp = 3 #3 hearts so 3hp


HORIZON = pygame.image.load("horizon.png").convert_alpha()
HORIZON = pygame.transform.scale(HORIZON,(35,110))

venom_left = pygame.image.load("venom left.png").convert_alpha()
venom_left = pygame.transform.scale(venom_left,(150,150))

venom_right = pygame.transform.flip(venom_left,True,False) 


''''''''''''''''''''
''' Making all of'''
''' the objects/ '''
''' instances of '''
''' the classes  '''
''''''''''''''''''''

horizon = Weapon(PLAYER_POS[0],PLAYER_POS[1])
hori_right_frames = [HORIZON,wizard_cat_right,PLAYER_LEFT]
horizon.set_images(hori_right_frames)

shotgun = Gun(PLAYER_POS[0]-PLAYER.get_width(),PLAYER_POS[1])
shotgun_right_frames = [shotgun_gun,shotgun_gun,shotgun_gun]
shotgun.set_images(shotgun_right_frames)
shotgun_left_frames = [shotgun_gun_left,shotgun_gun_left,shotgun_gun_left]
shotgun_shoot_right_frames = []
shotgun_shoot_left_frames = []



snake1 = Enemy(1200,600,venom_left,venom_right)
snake1.set_images([snake_left,snake_right,wizard_cat_right])
snake1.set_dmg(1)


snake2 = Enemy(1000,600,venom_left,venom_right)
snake2.set_images([snake_left,snake_right,wizard_cat_right])
snake2.set_dmg(1)

snake3 = Enemy(200,600,venom_left,venom_right)
snake3.set_images([snake_left,snake_right,wizard_cat_right])
snake3.set_dmg(1)

snake4 = Enemy(600,600,venom_left,venom_right)
snake4.set_images([snake_left,snake_right,wizard_cat_right])
snake4.set_dmg(1)

ally = Ally(200,500,venom_left,venom_right)
ally.set_images([ally_left,ally_right,wizard_cat_right])
ally.set_dmg(1)

enemies = [] #empty list to be filled with enemies
killed = 0 #tracks how many enemies player has killed

#appending all enemies to enemies list
enemies.append(snake1)
enemies.append(snake2)
enemies.append(snake3)
enemies.append(snake4)


distances = [] #used to find enemy with shortest distance from player



def get_font(size): #getting the font that I imported from the video I have referenced in the document
    return pygame.font.Font("font.ttf", size)



''''''''''''''''''''
'''Options screen'''
''''''''''''''''''''

def options():
    while True:
            pygame.mouse.set_visible(True) #making mouse visible again
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

            
            SCREEN.fill("purple")
            

            SCREEN.blit(QUIT_button,(840,500))

            ''''''''''''''''''''
            '''Making text to'''
            '''display all of'''
            ''' the controls '''
            '''and describing'''
            '''game objective'''
            '''   and ally   '''
            ''''''''''''''''''''
            
            W = get_font(45).render("W/UP ARROW: SWITCH WEAPONS", True, "Green")
            W_POS = W.get_rect(center=(x/2, 130.5))
            
            A = get_font(45).render("A/LEFT ARROW: MOVE LEFT", True, "Green")
            A_POS = A.get_rect(center=(x/2, 190.5))

            D = get_font(45).render("D/RIGHT ARROW: MOVE RIGHT", True, "Green")
            D_POS = D.get_rect(center=(x/2, 250.5))
            
            E = get_font(45).render("E: TELEPORT (WHEN NOT ON COOLDOWN)", True, "Green")
            E_POS = E.get_rect(center=(x/2, 310.5))
            
            SPACE = get_font(45).render("SPACEBAR: JUMP", True, "Green")
            SPACE_POS = SPACE.get_rect(center=(x/2, 370.5))
        
            CLICK = get_font(45).render("LEFT CLICK: ATTACK", True, "Green")
            CLICK_POS = CLICK.get_rect(center=(x/2, 430.5))
            
            OBJECTIVE = get_font(20).render("OBJECTIVE: DEFEAT ALL ENEMIES IN THE LEVEL TO WIN. LOSE IF YOU ARE HIT 3 TIMES", True, "Green")
            OBJECTIVE_POS = OBJECTIVE.get_rect(center=(x/2, 530.5))
            
            ALLY = get_font(20).render("ALLY: A PURPLE SNAKE - ATTACKS THE CLOSEST ENEMY TO YOU - THEY DON'T TAKE DAMAGE AND FOLLOW YOU", True, "Green")
            ALLY_POS = ALLY.get_rect(center=(x/2, 590.5))
            
            SCREEN.blit(W,W_POS)
            SCREEN.blit(A,A_POS)
            SCREEN.blit(D,D_POS)
            SCREEN.blit(E,E_POS)
            SCREEN.blit(SPACE,SPACE_POS)
            SCREEN.blit(CLICK,CLICK_POS)
            SCREEN.blit(OBJECTIVE,OBJECTIVE_POS)
            SCREEN.blit(ALLY,ALLY_POS)

            
            ''''''''''''''''''''
            ''' Checking if  '''
            ''' mouse is in  '''
            ''' range of any '''
            ''' buttons and  '''
            '''displaying hover'''
            '''images as well'''
            '''as checking if'''
            '''  player has  '''
            ''' pressed quit '''
            '''    button    '''
            ''''''''''''''''''''
            
            if OPTIONS_MOUSE_POS[0] in range(860,1090) and OPTIONS_MOUSE_POS[1] in range(725,830):
                SCREEN.blit(QUIT_hover,(840,500))

                
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if OPTIONS_MOUSE_POS[0] in range(860,1090) and OPTIONS_MOUSE_POS[1] in range(725,830):
                        pygame.quit()
                        sys.exit()
            
            pygame.display.update()


    
''''''''''''''''''''
''' Pause screen '''
''''''''''''''''''''

def pause():
    while True:
        pygame.mouse.set_visible(True) #making mouse visible again
        PAUSE_MOUSE_POS = pygame.mouse.get_pos()

        
        SCREEN.fill("purple")
        
        ''''''''''''''''''''
        '''Displaying all'''
        '''buttons on the'''
        '''  screen and  '''
        ''' checking if  '''
        ''' mouse is in  '''
        '''  of button/  '''
        '''button clicked'''
        ''''''''''''''''''''

        SCREEN.blit(CONTINUE_button,(740,100))
        SCREEN.blit(QUIT_button,(840,500))
        SCREEN.blit(OPTIONS_button,(310,190))
        
        
        if PAUSE_MOUSE_POS[0] in range(740,1230) and PAUSE_MOUSE_POS[1] in range(315,415):
            SCREEN.blit(CONTINUE_hover,(740,100))
        if PAUSE_MOUSE_POS[0] in range(860,1090) and PAUSE_MOUSE_POS[1] in range(725,830):
            SCREEN.blit(QUIT_hover,(840,500))
        if PAUSE_MOUSE_POS[0] in range(775,1170) and PAUSE_MOUSE_POS[1] in range(525,640):
            SCREEN.blit(OPTIONS_hover,(310,190))    
            
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if PAUSE_MOUSE_POS[0] in range(740,1230) and PAUSE_MOUSE_POS[1] in range(335,415):
                    play(PLAYER_POS,PLAYER_hp)
                if PAUSE_MOUSE_POS[0] in range(860,1090) and PAUSE_MOUSE_POS[1] in range(725,830):
                    main_menu()
                if PAUSE_MOUSE_POS[0] in range(685,1170) and PAUSE_MOUSE_POS[1] in range(535,650):
                    options()
        
        pygame.display.update()
        
        
        
''''''''''''''''''''
''' Win screen  '''
''''''''''''''''''''        

def win():
    while True:
        pygame.mouse.set_visible(True) #making mouse visible again
        WIN_MOUSE_POS = pygame.mouse.get_pos()

        
        SCREEN.fill("green")
        
        
        

        WIN_MSG = get_font(75).render("CONGRATULATIONS - YOU WIN!", True, "white") #has the game's title and color
        WIN_POS = WIN_MSG.get_rect(center=(x/2, 400))
        win_outline1 = get_font(75).render("CONGRATULATIONS - YOU WIN!", True, "black") #creating outline for title
        win_outline1_pos = win_outline1.get_rect(center=((x/2), 408.5)) #outline placed 8 pixels underneath title for shadowy effect
        
        SCREEN.blit(win_outline1,win_outline1_pos)
        SCREEN.blit(WIN_MSG, WIN_POS)
        
        SCREEN.blit(QUIT_button,(840,500))
        
        

        if WIN_MOUSE_POS[0] in range(860,1090) and WIN_MOUSE_POS[1] in range(725,830):
            SCREEN.blit(QUIT_hover,(840,500))
    
            
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if WIN_MOUSE_POS[0] in range(860,1090) and WIN_MOUSE_POS[1] in range(725,830): #if in range of quit button, back to main menu
                    pygame.quit()
                    sys.exit()
        
        pygame.display.update()


''''''''''''''''''''
''' Lose screen  '''
''''''''''''''''''''

def lose():
    while True:
        pygame.mouse.set_visible(True) #making mouse visible again
        LOSE_MOUSE_POS = pygame.mouse.get_pos()
   
        SCREEN.fill("red")  

        LOSE_MSG = get_font(75).render("YOU LOSE", True, "white")
        LOSE_POS = LOSE_MSG.get_rect(center=(x/2, 400))
        lose_outline1 = get_font(75).render("YOU LOSE", True, "black")
        lose_outline1_pos = lose_outline1.get_rect(center=((x/2), 408.5))
        
        SCREEN.blit(lose_outline1,lose_outline1_pos)
        SCREEN.blit(LOSE_MSG, LOSE_POS)
        
        SCREEN.blit(QUIT_button,(840,500))  

        if LOSE_MOUSE_POS[0] in range(860,1090) and LOSE_MOUSE_POS[1] in range(725,830):
            SCREEN.blit(QUIT_hover,(840,500))
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if LOSE_MOUSE_POS[0] in range(860,1090) and LOSE_MOUSE_POS[1] in range(725,830): 
                    pygame.quit()
                    sys.exit()
        
        pygame.display.update()



''''''''''''''''''''
''' Play screen  '''
''''''''''''''''''''

def play(PLAYER_POS,PLAYER_hp):

    checkpoint = [200,500]
    


    #representing level as text file
    file = open('level_map.txt','r')
    data = file.read()
    file.close()
    data = data.split('\n')
    level_map = []
    for row in data: 
        level_map.append(list(row)) 
    

    tile_width = FLOOR.get_width() #getting the width of each tile in pixels
    tile_height = FLOOR.get_height() #getting the height of each tile



    
    realscroll = [0,0] #how far screen scrolls by on x and y axis - for camera movement 
    
    
    #setting up key variables
    face_left = False
    face_right = False
    default = True
    
    moving_right = False
    moving_left = False
    go_right = False
    go_left = False
    jump = False
    upwards = False
    speed_boost = False
    speed = 14
    floor = False
    
    

    fall = False
    jump = False

    
    swing = False #check when player is attacking with sword
    
    ''''''''''''''''''''
    '''  Setting up  '''
    '''  all of the  '''
    '''   player's   '''
    '''   hitboxes   '''
    ''''''''''''''''''''
    
    player_hitbox = pygame.Rect(PLAYER_POS[0],PLAYER_POS[1],PLAYER.get_width(),PLAYER.get_height())
    player_floor_hitbox = pygame.Rect(PLAYER_POS[0],PLAYER_POS[1]+PLAYER.get_height(),PLAYER.get_width(),5) #making hitbox for player's feet to check when touching floor/ground
    player_top_hitbox = pygame.Rect(PLAYER_POS[0],PLAYER_POS[1],PLAYER.get_width(),5)
    player_right_hitbox = pygame.Rect(PLAYER_POS[0]+PLAYER.get_width(),PLAYER_POS[1],5,PLAYER.get_height())
    player_left_hitbox = pygame.Rect(PLAYER_POS[0],PLAYER_POS[1],5,PLAYER.get_height())
    
    horizon_hitbox = pygame.Rect(PLAYER_POS[0],PLAYER_POS[1],HORIZON.get_width(),HORIZON.get_height())
    
    



    
    
    #setting up remaining key variables
    d = 0 #counter for how many times you go through while loop
    index = 0
    angle = 0 #angle to rotate image during melee swing animation
    aimangle = 0
    cd = 0 #ability cooldown
    enemySpeed = 4
    
    #checks if gun or sword should be shown
    melee = True
    ranged = False
    
    killed = 0 #counts number of enemies killed
    
    
    for h in range(len(enemies)):
        enemies[h].set_hp(500) #setting hp of enemy
        enemies[h].set_hpwidth(enemies[h].get_image().get_width())

    
    while True: #making sure that all the changes remain on the screen and don't disappear straight away
        
        ally.fall() #making sure ally falls when in air
        ally.fallspeed = 10
        
        for h in range(len(enemies)):
            enemies[h].fall() #making sure enemies fall when in air
            enemies[h].fallspeed = 10
            
            
        
        SCREEN.fill((0,181,226))
        PLAY_MOUSE_POS = pygame.mouse.get_pos() 
        speed = 14
        
        pygame.mouse.set_visible(False) #making mouse cursor invisible
        
        #camera scroll
        realscroll[0] -= (PLAYER_POS[0]+realscroll[0]-x/2+PLAYER.get_width()/2)/30 #how fast/slow the camera catches up to the player's central position
        realscroll[1] -= (PLAYER_POS[1]-y/2+PLAYER.get_height()/2+realscroll[1])/30
        scroll = realscroll.copy()
        scroll[0] = int(scroll[0])
        scroll[1] = int(scroll[1])
        

        
        

        
        d = d+1 #tracks how many times the while/play game loop has run
        if cd != 0: #if ability is on cooldown, reduce cooldown until 0
            cd -= 1
        
        
        #-------------------------------------------------
        #setting up floor hitboxes
        FLOOR_rect = pygame.Rect(200,5000,tile_width,10)
        FLOOR_left_rect = pygame.Rect(200,5000,tile_width,10)
        FLOOR_right_rect = pygame.Rect(200,5000,tile_width,10)
        FLOOR_safe_rect = pygame.Rect(200,5000,tile_width,10)
        FLOOR_bottom_rect = pygame.Rect(200,5000,tile_width,10)

        

        
        #initialising some ally attributes
        ally.get_image()
        ally.set_Rect()
        ally.get_Rect().center = (ally.get_posx() + (ally.get_image().get_width()/2)+scroll[0],ally.get_posy() + scroll[1] + (ally.get_image().get_height()/2))
        ally.set_floorRect()
        ally.get_floorRect().center = (ally.get_posx() + (ally.get_image().get_width()/2)+scroll[0],ally.get_posy() + scroll[1] + (ally.get_image().get_height()))
        
        
        ally.set_speed(2)
        
        
        #displaying left or right image for ally depending on what side of the player they are on
        if ally.get_posx() < PLAYER_POS[0]:
            ally.index = 1
        else:
            ally.index = 0
        
        

        #checking if enemies are alive and displaying correct image
        #setting up enemy hp bars
        for h in range(len(enemies)):

            enemies[h].get_image()

            enemies[h].set_Rect()



            enemies[h].set_floorRect()
            
            enemies[h].set_hpbar()
            enemies[h].set_hpborder()
            enemies[h].set_hpback()

            if enemies[h].get_hp() > 0:
                enemies[h].get_Rect().center=(enemies[h].get_posx()+(enemies[h].get_image().get_width()/2)+scroll[0],enemies[h].get_posy() + scroll[1]+(enemies[h].get_image().get_height()/2))
                enemies[h].get_floorRect().center=(enemies[h].get_posx()+(enemies[h].get_image().get_width()/2)+scroll[0],enemies[h].get_posy()+scroll[1]+(enemies[h].get_image().get_height()))
                enemies[h].get_hpback().center = (enemies[h].get_posx() + (enemies[h].get_image().get_width()/2)+scroll[0],enemies[h].get_posy() + scroll[1])
                enemies[h].get_hpbar().center = (enemies[h].get_posx() + (enemies[h].get_image().get_width()/2)+scroll[0],enemies[h].get_posy() + scroll[1])
                enemies[h].get_hpborder().center = (enemies[h].get_posx() + (enemies[h].get_image().get_width()/2)+scroll[0],enemies[h].get_posy() + scroll[1])
                
            else:
                enemies[h].get_Rect().center = (9000,9000)
                enemies[h].get_floorRect().center = (9000,9000)
                enemies[h].get_hpbar().center = (9000,9000)
                enemies[h].get_hpborder().center = (9000,9000)
                enemies[h].get_hpback().center = (9000,9000)
                enemies[h].set_atkcd(9000)

            
            
            

        

        #level_map is an array created from the imported text file for the level map
        for i in range(0,len(level_map)-1):
            for j in range(len(level_map[i])-1):
                if level_map[i][j] == '1':
                    SCREEN.blit(DIRT,(j*tile_width + scroll[0],i*tile_height + scroll[1]))
                if level_map[i][j] == '2':
                    SCREEN.blit(FLOOR,(j*tile_width + scroll[0],i*tile_height + scroll[1]))
                    FLOOR_rect = pygame.Rect(j*tile_width-10 + scroll[0],i*tile_height-10 + scroll[1],tile_width+20,20)
                    FLOOR_left_rect = pygame.Rect(j*tile_width-10 + scroll[0],i*tile_height+10 + scroll[1],30,tile_height-10)
                    FLOOR_right_rect = pygame.Rect(j*tile_width+tile_width-10 + scroll[0],i*tile_height+10 + scroll[1],20,tile_height-10)
                    FLOOR_bottom_rect = pygame.Rect(j*tile_width + scroll[0],i*tile_height+tile_height-10 + scroll[1],tile_width,20)                   
                
                
                #checking if enemies, player and ally are colliding with floor tiles
                if player_floor_hitbox.colliderect(FLOOR_rect):
                    floor = True #setting variable to true when touching floor
                    fall = False
                
                
                
                if player_right_hitbox.colliderect(FLOOR_left_rect):
                    speed = 0
                    if moving_left == True:
                        speed = 14
                
                if player_left_hitbox.colliderect(FLOOR_right_rect):
                    speed = 0
                    if moving_right == True:
                        speed = 14
                
                ally.collide_floor(FLOOR_rect)
                ally.collide_right(FLOOR_right_rect)
                ally.collide_left(FLOOR_left_rect)
                
                for h in range(len(enemies)):
                    enemies[h].collide_floor(FLOOR_rect)
                    enemies[h].collide_right(FLOOR_right_rect)
                    enemies[h].collide_left(FLOOR_left_rect)


                

        #----------------------------------------------------------------



        #displaying ally and player on screen
        SCREEN.blit(ally.get_image(),(ally.get_posx()+scroll[0],ally.get_posy() + scroll[1]))
        
        
        #checking if player facing left of right
        if face_left == True:
            SCREEN.blit(PLAYER_LEFT,(PLAYER_POS[0] + scroll[0],PLAYER_POS[1] + scroll[1]))
            SCREEN.blit(iron_armour_left,(PLAYER_POS[0] + scroll[0],PLAYER_POS[1] + scroll[1])) #testing armour on player
            SCREEN.blit(wizard_cat_left,(PLAYER_POS[0]+60 + scroll[0],PLAYER_POS[1]+PLAYER.get_height()-wizard_cat_left.get_height() + scroll[1])) #testing cat following player
            
        
        if face_right == True:
            SCREEN.blit(PLAYER,(PLAYER_POS[0] + scroll[0],PLAYER_POS[1] + scroll[1]))
            SCREEN.blit(iron_armour_right,(PLAYER_POS[0] + scroll[0],PLAYER_POS[1] + scroll[1])) #testing armour on player
            SCREEN.blit(wizard_cat_right,(PLAYER_POS[0]-60 + scroll[0],PLAYER_POS[1]+PLAYER.get_height()-wizard_cat_right.get_height() + scroll[1])) #testing cat following player
        
        if default == True:
            SCREEN.blit(PLAYER,(PLAYER_POS[0] + scroll[0],PLAYER_POS[1] + scroll[1]))
            SCREEN.blit(iron_armour_right,(PLAYER_POS[0] + scroll[0],PLAYER_POS[1] + scroll[1])) #testing armour on player
            SCREEN.blit(wizard_cat_right,(PLAYER_POS[0]-60 + scroll[0],PLAYER_POS[1]+PLAYER.get_height()-wizard_cat_right.get_height() + scroll[1])) #testing cat following player
        
        #making player move in correct direction
        if moving_right ==  True:
            default = False
            face_left = False

            PLAYER_POS[0] += speed
            face_right = True

        
        if moving_left == True:
            default = False
            face_right = False

            PLAYER_POS[0] -= speed
            face_left = True

            

        
        

        #----------------------------------------------------
        
        #making weapons stick to player
        horizon.set_posx(PLAYER_POS[0])
        horizon.set_posy(PLAYER_POS[1])
    
        shotgun.set_posx(PLAYER_POS[0] - PLAYER.get_width())
        shotgun.set_posy(PLAYER_POS[1])
        
        #--------------------------------------------------------------

        #code for displaying sword
        if melee == True:
            hori2 = pygame.image.load("hori2.png").convert_alpha()
            if face_left == True:
                hori2 = pygame.transform.flip(hori2,True,False)

            hori2 = pygame.transform.scale(hori2,(35,220))
            hori2 = pygame.transform.rotate(hori2,angle)
            hori2_center = (PLAYER_POS[0]+50 - (hori2.get_width()/2) + scroll[0],PLAYER_POS[1]+80 - (hori2.get_height()/2) + scroll[1])
            if face_left == True:
                hori2_center = (PLAYER_POS[0]+33 - (hori2.get_width()/2) + scroll[0],PLAYER_POS[1]+80 - (hori2.get_height()/2) + scroll[1])
            SCREEN.blit(hori2,hori2_center)
            
        
        #making shotgun rotate to cursor
        shotty = shotgun.get_image(index)
        if ranged == True:
            xdif = PLAY_MOUSE_POS[0] - 50/2*math.pi - shotgun.get_posx() - scroll[0]
            ydif = -(PLAY_MOUSE_POS[1] - 80/2*math.pi - shotgun.get_posy()) + scroll[1]
            if xdif == 0:
                if ydif < 0:
                    incline = (math.pi)/2 #90 degrees in radians
                else:
                    incline = -(math.pi)/2 #-90 degrees in radians
            else:
                incline = math.atan2(ydif,xdif) #angle in radians between crosshair and shotgun
            aimangle = math.degrees(incline) #convert angle from radians to degrees
            if aimangle > 90 or aimangle < -90: #flippinng shotgun to face same way as player aiming
                shotty = pygame.transform.flip(shotty,False,True)
            
            
            #displaying shotgun in correct location
            shotty = pygame.transform.rotate(shotty,aimangle)
            shotty_center = (PLAYER_POS[0]+50 - (shotty.get_width()/2) + scroll[0],PLAYER_POS[1]+80 - (shotty.get_height()/2) + scroll[1])
            SCREEN.blit(shotty,shotty_center)
           
        #setting up sword hitbox
        horibox = pygame.Rect(9000,9000,HORIZON.get_height(),HORIZON.get_width())
            
        
        


        
        #---------------------------------------------------------------------------------
        #swing animation anbd hitbox for sword
        if swing == True:
            if melee == True:
                if face_right == True or default == True:
                    angle = angle-6 #turns through clockwise (-ve is clockwise, +ve anticlockwise)
                    if angle != -90:
                        horibox = pygame.Rect(PLAYER_POS[0]+PLAYER.get_width()/2+scroll[0],PLAYER_POS[1]+PLAYER.get_height()/2-HORIZON.get_height() + 20 + scroll[1], HORIZON.get_height(),HORIZON.get_height())
                    if angle == -90:
                        angle = 0
                        swing = False
                else:
                    angle = angle+6 #turns through clockwise (-ve is clockwise, +ve anticlockwise)      
                    if angle != 90:
                        horibox = pygame.Rect(PLAYER_POS[0]-29-PLAYER.get_width()/2+scroll[0],PLAYER_POS[1]+PLAYER.get_height()/2-HORIZON.get_height()+20+scroll[1],HORIZON.get_height(),HORIZON.get_height())
                    if angle == 90:
                        angle = 0
                        swing = False
                
         
        #sewtting projectiles for ally
        ally.set_proj_right_rect(scroll[0],scroll[1])
        ally.set_proj_left_rect(scroll[0],scroll[1])
        
        
        #making enemies attack player and ally attack enemies
        #checking if enemy hit by player or ally and adjusting health
        #checking if player hit by enemy and adjusting health
        for h in range(len(enemies)):
            enemies[h].maxhp = 500
            enemies[h].set_proj_right_rect(scroll[0],scroll[1])
            enemies[h].set_proj_left_rect(scroll[0],scroll[1])
            PLAYER_hp = enemies[h].atk(SCREEN,PLAYER_POS[0],player_hitbox,PLAYER_hp,scroll[0],scroll[1])
            if ally.proj_right_rect.colliderect(enemies[h]) or ally.proj_left_rect.colliderect(enemies[h]):
                ally.projx = -9000
                ally.atkcd = 100
            enemies[h].playerhit(ally.proj_left_rect,ally.proj_right_rect,horibox,swing,enemies[h].get_image().get_width(),enemies[h].maxhp)
            
            

            
            
            #displaying enemy hp bars
            pygame.draw.rect(SCREEN, (0,0,0), enemies[h].get_hpborder())
            pygame.draw.rect(SCREEN, (255,0,0), enemies[h].get_hpback())
            pygame.draw.rect(SCREEN, (0,255,0), enemies[h].get_hpbar())
            
            



 
        #check if player has died/lost
        if PLAYER_hp <= 0:
            lose()

        
        
        


       
        
        if d == 20: #this is how long each frame stays on the screen for
            d = 0
        
        #making enemies face left or right
        for h in range(len(enemies)):
            if enemies[h].get_posx() > PLAYER_POS[0]:
                enemies[h].index = 0
            if enemies[h].get_posx() < PLAYER_POS[0]:
                enemies[h].index = 1

        
        
        
        
        #making sure player hitboxes follow the player
        player_hitbox.x = PLAYER_POS[0] + scroll[0]#updating x and y coordinates of hitbox to match player's position
        player_hitbox.y = PLAYER_POS[1] + scroll[1]
        
        player_floor_hitbox.x = PLAYER_POS[0] + scroll[0]#updating x and y coordinates of player's feet to match player's position
        player_floor_hitbox.y = PLAYER_POS[1]+PLAYER.get_height() + scroll[1]
        
        player_top_hitbox.x = PLAYER_POS[0] + scroll[0]#updating x and y coordinates of player's feet to match player's position
        player_top_hitbox.y = PLAYER_POS[1] + scroll[1]        
        
        player_right_hitbox.x = PLAYER_POS[0]+PLAYER.get_width() + scroll[0]
        player_right_hitbox.y = PLAYER_POS[1] + scroll[1]
        
        player_left_hitbox.x = PLAYER_POS[0] + scroll[0]
        player_left_hitbox.y = PLAYER_POS[1] + scroll[1]
        
        
        
        
        

        #code for jumping upwards
        if upwards == True:
            floor = False
            if PLAYER_POS[1] > current_y-300:
                PLAYER_POS[1] -= 25
                ally.posy -= 25

                if PLAYER_POS[1] <= current_y-300 or player_top_hitbox.colliderect(FLOOR_bottom_rect):
                    upwards = False
            
        #code for gravity to make sure player falls   
        if fall == True:
            PLAYER_POS[1] += 10
            

        #code for jumping
        if jump == True:
            fall = False
            if floor == True:
                upwards = True
            jump = False
            fall = True
        
        #making sure player only falls if not touching ground
        if player_floor_hitbox.colliderect(FLOOR_rect): #checking if bottom of player collides with floor
            fall = False
        else:
            fall = True
            floor = False
        
        #dispalying pause button and checking if it is hovered over/clicked
        SCREEN.blit(PAUSE_button,(1570,-85))
        
        if PLAY_MOUSE_POS[0] in range(1750,1850) and PLAY_MOUSE_POS[1] in range(30,90):
            SCREEN.blit(PAUSE_hover,(1570,-85))
    
        for event in pygame.event.get(): #this loop is used for all events e.g. button presses or mouse clicks
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() #this loop means: when the window is closed, stop running
                           #without this, the window will not close when the x button is pressed 
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if PLAY_MOUSE_POS[0] in range(1750,1850) and PLAY_MOUSE_POS[1] in range(30,90): #if in range of pause button, pause the game
                    checkpoint = PLAYER_POS
                    checkpoint[1] -= 150 #stops player falling through floor when you press continue
                    pause()
            
            #checking player inputs and making sure correct output is carried out
            if event.type == KEYDOWN: #if the event is a key is being pressed
                if event.key == K_RIGHT or event.key == K_d:
                    moving_right = True
                     
                if event.key == K_LEFT or event.key == K_a:
                    moving_left = True
                
                if event.key == K_SPACE:
                    current_y = PLAYER_POS[1]
                    jump = True
                    
                if event.key == K_e:
                    if cd == 0: #prevents cooldown from extending while cooldown is already active i.e. if press e while on cooldown, cooldown doesn't reset to 200 again
                        cd = 200 #setting ability on cooldown
                        PLAYER_POS[0] = PLAY_MOUSE_POS[0] - scroll[0]
                        PLAYER_POS[1] = PLAY_MOUSE_POS[1] - scroll[1] - 10 - PLAYER.get_height() #making it so the bottom of the player goes to the mouse pos instead of top
                                                                                                 #taking off extra 10 to make it harder to teleport inside of a floor

            
            #makes sure correct outputs occur when player releases a key
            if event.type == KEYUP:
                if event.key == K_RIGHT or event.key == K_d:
                    moving_right = False
                
                if event.key == K_LEFT or event.key == K_a:
                    moving_left = False
                    
                if event.key == K_SPACE:
                    jump = False
                
                
                if event.key == K_w or event.key == K_UP:
                    if ranged == True:
                        ranged = False
                        melee = True
                    elif melee == True:
                        melee = False
                        ranged = True
            
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                swing = True
        


        #making enemies and ally move towards player
        #keeping track of how many enemies are dead
        for h in range(len(enemies)):
            enemies[h].movex(PLAYER_POS[0],scroll[0]) 
            ally.movex(PLAYER_POS[0]-200,scroll[0])
            
            if enemies[h].get_hp() > 0:
                SCREEN.blit(enemies[h].get_image(),(enemies[h].get_posx()+scroll[0],enemies[h].get_posy() + scroll[1]))
            
            if enemies[h].get_hp() <= 0:
                if enemies[h].dead == False:
                    enemies[h].dead = True
                    killed += 1
                    
            #checks is player has won by seeing if all enemies are dead
            if killed == len(enemies):
                win()
            
            #calculating enemy with shortest distance from player so ally knows who to target
            distances.append(abs(enemies[h].get_posx() - PLAYER_POS[0]))
        
            
            
            if abs(enemies[h].get_posx() - PLAYER_POS[0]) == min(distances):
                enemies[h].hp = ally.atk(SCREEN,enemies[h].get_posx(),enemies[h].get_Rect(),enemies[h].get_hp(),scroll[0],scroll[1])
                
           
            if len(distances) == len(enemies):
                distances.clear()           
            

        
        
        #ability button and cooldown button as well as displaying heart and empty heart images
        
        SCREEN.blit(ability_cd,(-100,700))
        if cd == 0: #if ability not on cooldown
            SCREEN.blit(ability_button,(-100,700))
        SCREEN.blit(crosshair,(PLAY_MOUSE_POS[0]-20,PLAY_MOUSE_POS[1]-20))
        
        SCREEN.blit(noheart,(50,25))
        SCREEN.blit(noheart,(250,25))
        SCREEN.blit(noheart,(450,25))
        
        
        if PLAYER_hp >= 1:
            SCREEN.blit(heart,(50,25))
        if PLAYER_hp >= 2:
            SCREEN.blit(heart,(250,25))
        if PLAYER_hp >= 3:
            SCREEN.blit(heart,(450,25))
        
        pygame.display.update() #need to update display within the while loop so the correct screen is shown
        clock.tick(60) #setting frame rate to 60 fps
        
''''''''''''''''''''
'''   Main menu  '''
''''''''''''''''''''
        
def main_menu():
    while True:
        pygame.mouse.set_visible(True) #making mouse visible again
        SCREEN.blit(BG, (0, 0))#name of image and coordinates: blit means putting that image on top of the current surface
        
        ''''''''''''''''''''
        '''Displaying all'''
        '''buttons on the'''
        '''  screen and  '''
        ''' checking if  '''
        ''' mouse is in  '''
        '''  of button/  '''
        '''button clicked'''
        ''''''''''''''''''''
        
        
        MENUQUIT_button = pygame.image.load("QUIT button.png").convert_alpha()
        MENUQUIT_button = pygame.transform.scale(MENUQUIT_button,(1100,750))
        MENUQUIT_hover = pygame.image.load("QUIT hover.png").convert_alpha()
        MENUQUIT_hover = pygame.transform.scale(MENUQUIT_hover,(1100,750))

        SCREEN.blit(PLAY_button,(650,200))
        SCREEN.blit(MENUQUIT_button,(800,450))
        SCREEN.blit(OPTIONS_button,(310,200))

        MENU_MOUSE_POS = pygame.mouse.get_pos()


        MENU_TITLE = get_font(75).render("HORIZON'S EDGE", True, "Purple") #has the game's title and color
        MENU_POS = MENU_TITLE.get_rect(center=(x/2, 130.5))
        menu_outline1 = get_font(75).render("HORIZON'S EDGE", True, "black") #creating outline for title
        menu_outline1_pos = menu_outline1.get_rect(center=((x/2), 138.5)) #outline placed 8 pixels underneath title for shadowy effect
        
        SCREEN.blit(menu_outline1,menu_outline1_pos)
        SCREEN.blit(MENU_TITLE, MENU_POS)
        
    
        if MENU_MOUSE_POS[0] in range(750,1150) and MENU_MOUSE_POS[1] in range(330,450): #rough dimensions of play button to check if the mouse hovers over the button
            SCREEN.blit(PLAY_hover,(650,200))
        if MENU_MOUSE_POS[0] in range(835,1100) and MENU_MOUSE_POS[1] in range(745,860):
            SCREEN.blit(MENUQUIT_hover,(800,450))
        if MENU_MOUSE_POS[0] in range(775,1170) and MENU_MOUSE_POS[1] in range(535,650):
            SCREEN.blit(OPTIONS_hover,(310,200))
            

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if MENU_MOUSE_POS[0] in range(750,1150) and MENU_MOUSE_POS[1] in range(330,450):
                    play(PLAYER_POS,PLAYER_hp)
                if MENU_MOUSE_POS[0] in range(835,1100) and MENU_MOUSE_POS[1] in range(745,860):
                    pygame.quit()
                    sys.exit()
                if MENU_MOUSE_POS[0] in range(685,1170) and MENU_MOUSE_POS[1] in range(535,650):
                    options()

        pygame.display.update()
        
main_menu()