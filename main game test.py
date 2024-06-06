import pygame,sys,random,time
from math import *

from entities import *
from weapons import *

#GENERAL NOTE: remember that when y value increases, the image actually moves down, not up, and vise versa

clock = pygame.time.Clock() #getting frame rate/defining frame rate as a variable

from pygame.locals import * #importing everything from pygame
#---------------------------------------------------------------------------------------------------------------------
pygame.init() #initialises/creates an instance of pygame


'''
#prototype/concept for cheat codes - will need to make a proper interactive display for the user to input codes later
#all cheat code abilities are currently commented out, as they are just rough notes/ideas for what each code should do e.g. player_dmg = player_dmg*3
def enter_code():
  myFile = open('Cheat Codes.csv','r')  #this is the file that all of the cheat codes are stored in
  code = input("Enter code: ") 
  code_true = False
  for line in myFile:
    l = line.split()
    if l[0] == code:
        code_true = True
        if l[0] == 'D4NG3R':
            #player_dmg = player_dmg*3
        elif l[0] == 'SPE3DJ':
            #player_speed = player_speed*5
        elif l[0] == 'B1GP3T':
            #pet_size = pet_size*7
            #pet_dmg = pet_dmg*5
            #pet_ability_cooldown = pet_ability_cooldown/2
        elif l[0] == 'MONSTR':
            #enemy_size = enemy_size*2
            #enemy_hp = enemy_hp*2
            #enemy_dmg = enemy_dmg*2
        elif l[0] == 'HORDGE':
            #player_weapon_size = player_weapon_size*3
            #player_weapon_dmg = player_wpn_dmg*3      
  if code_true == True:  
      print("Code accepted")    
  myFile.close()
'''

x=1920
y=1080
#y = 0 is the top of the screen, x = 0 is the very left of the screen
SCREEN = pygame.display.set_mode((x, y))
pygame.display.set_caption("Menu")

#equation for scaling pets/characters/enemies:
#x value: x/1920 * 80
#y value: 7/1080 * 140
#then halve/double (multiply/divide) values by same ratio accordingly to get right size

BG = pygame.image.load("Background.png").convert() #convert() makes it quicker when loading images, just a general function used after loading images to increase speed
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

#these are for entering cheat codes - this  feature will be available on the options screen
CODE_button = pygame.image.load("CODE button.png").convert_alpha()
CODE_button = pygame.transform.scale(CODE_button,(900,600))

CODE_hover = pygame.image.load("CODE hover.png").convert_alpha()
CODE_hover = pygame.transform.scale(CODE_hover,(900,600))

PLAYER = pygame.image.load("PLAYER.png").convert_alpha()
PLAYER = pygame.transform.scale(PLAYER,(80,140))

#load in all images for every frame of every entity

iron_armour_right = pygame.image.load("iron armour right.png").convert_alpha()
iron_armour_right = pygame.transform.scale(iron_armour_right,(80,140))

iron_armour_left = pygame.image.load("iron armour left.png").convert_alpha()
iron_armour_left = pygame.transform.scale(iron_armour_left,(80,140))

wizard_cat_right = pygame.image.load("wizard cat right.png").convert_alpha()
wizard_cat_right = pygame.transform.scale(wizard_cat_right,(102,1350/28))

wizard_cat_left = pygame.image.load("wizard cat left.png").convert_alpha()
wizard_cat_left = pygame.transform.scale(wizard_cat_left,(102,1350/28))

PLAYER_LEFT = pygame.image.load("PLAYER LEFT.png").convert_alpha()
PLAYER_LEFT = pygame.transform.scale(PLAYER_LEFT,(80,140))

shotgun_gun = pygame.image.load("shotgun.png").convert_alpha()
shotgun_gun = pygame.transform.scale(shotgun_gun,(100,25))

dand = pygame.image.load("dandelion_enemy.png").convert_alpha()
dand = pygame.transform.scale(dand,(200,200))

dandelion = Enemy(500,400)
dand_right_frames = [dand,PLAYER,wizard_cat_right]
dandelion.set_images(dand_right_frames)

FLOOR = pygame.image.load("FLOOR.png").convert_alpha()
FLOOR = pygame.transform.scale(FLOOR,(131,60))

DIRT = pygame.image.load("DIRT.png").convert_alpha()
DIRT = pygame.transform.scale(DIRT,(131,60))

PLAYER_POS = [200,500]

HORIZON = pygame.image.load("horizon.png").convert_alpha()
HORIZON = pygame.transform.scale(HORIZON,(35,110))

projectile1 = pygame.image.load("projectile1.png").convert_alpha()
projectile1 = pygame.transform.scale(projectile1,(500,500))



horizon = Weapon(PLAYER_POS[0],PLAYER_POS[1])
hori_right_frames = [HORIZON,wizard_cat_right,PLAYER_LEFT]
horizon.set_images(hori_right_frames)

shotgun = Gun(PLAYER_POS[0],PLAYER_POS[1])
shotgun_right_frames = [shotgun_gun,shotgun_gun,shotgun_gun]
shotgun.set_images(shotgun_right_frames)
shotgun_shoot_right_frames = []
shotgun_shoot_left_frames = []

def get_font(size): #getting the font that I imported from the video I have referenced in the document
    return pygame.font.Font("font.ttf", size)

def pause():
    while True:
        PAUSE_MOUSE_POS = pygame.mouse.get_pos()

        
        SCREEN.fill("purple")
        
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE_MOUSE_POS[0] in range(740,1230) and PAUSE_MOUSE_POS[1] in range(335,415): #if in range of continue button, back to play screen
                    play(PLAYER_POS)
                if PAUSE_MOUSE_POS[0] in range(860,1090) and PAUSE_MOUSE_POS[1] in range(725,830): #if in range of quit button, back to main menu
                    main_menu()
        
        pygame.display.update()
        
'''
def display_level(file):
    level = open(file+'.txt','r')
    item = level.read()
    level.close()
    level = level.split('\n')
    level_map = []
'''    

def play(PLAYER_POS): #maybe pass in save_point as a parameter, and set it to True when you pass checkpoint i.e. play(PLAYER_POS,save_point) would be play(PLAYER_POS,True)

    checkpoint = [200,500]

    '''
    myFile = open('level_map.txt','r')
    #for j in range(0,19):
    for line in myFile:
        print(line)
        for i in range(len(line)):
            if line[i] == '1':
                print("hello")
            if line[i] == '2':
                print("hi")
            if line[i] == '0':
                print("hey")
    myFile.close()
    '''


    #representing level as text file
    file = open('level_map.txt','r')
    data = file.read()
    file.close()
    data = data.split('\n') #formatting the file correclty into rows in python
    level_map = []
    for row in data: 
        level_map.append(list(row)) 
    

    tile_width = FLOOR.get_width() #getting the width of each tile in pixels
    tile_height = FLOOR.get_height() #getting the height of each tile


    #--------------------------------------------------------------------------------------------
    #save_point = False #checkpoint for level
    #if save_point == True: 
        #PLAYER_POS = [7000,500] #position of checkpoint that player will respawn at if they die

    #if player_hitbox.colliderect(save_point_rect):
        #save_point = True
    #--------------------------------------------------------------------------------------------

    face_left = False
    face_right = False
    default = True
    
    moving_right = False
    moving_left = False
    go_right = False
    go_left = False
    jump = False
    upwards = False
    midair = False #keep track of when player is in the air
    speed_boost = False
    speed = 14
    floor = False
    
    
    gravity = 0 #downward acceleration when characxter is in the air
    fall = False
    jump = False
    #If not colliding with floor:
                     #Fall = True
    
    swing = False
    
    player_hitbox = pygame.Rect(PLAYER_POS[0],PLAYER_POS[1],PLAYER.get_width(),PLAYER.get_height())
    player_floor_hitbox = pygame.Rect(PLAYER_POS[0],PLAYER_POS[1]+PLAYER.get_height(),PLAYER.get_width(),5) #making hitbox for player's feet to check when touching floor/ground
    player_top_hitbox = pygame.Rect(PLAYER_POS[0],PLAYER_POS[1],PLAYER.get_width(),5)
    player_right_hitbox = pygame.Rect(PLAYER_POS[0]+PLAYER.get_width(),PLAYER_POS[1],5,PLAYER.get_height())
    player_left_hitbox = pygame.Rect(PLAYER_POS[0],PLAYER_POS[1],5,PLAYER.get_height())
    
    horizon_hitbox = pygame.Rect(PLAYER_POS[0],PLAYER_POS[1],HORIZON.get_width(),HORIZON.get_height())
    
    


    #if player_hitbox.colliderect(FLOOR_rect):
        #fall = False
    #----------------------------------------------------------------------------------------------

    #----------------------------------------------------------------------------------------------
    '''
    #pseudocode for enemy firing projectile in correct direction towards the player
    if enemy_x_coordinate < PLAYER_POS[0]: #if enemy behind polayer, shoot to the right
        projectile_x_coordinate += 5
    if enemy_x_coordinate > PLAYER_POS[0]: #if enemy in front of player, shoot to the left
        projectile_x_coordinate -= 5
    '''
    
    '''
    #pseudocode for enemy projectile colliding with player
    if projectile_x_coordinate in range(PLAYER_POS[0],PLAYER_POS[0]+PLAYER.get_width()) and projectile_y_coordinate in range(PLAYER_POS[1],PLAYER_POS[1]+PLAYER.get_height()):
        hp = hp-1
        if hp == 0:
            game over
    '''

    '''
    #--------------------------------------------------------------------------------------------------------
    #put the lines below about gravity into the while True loop
    if gravity > 3: #set max acceleration when falling, otherwise velocity would increase towards infinity
        gravity = 3
    #--------------------------------------------------------------------------------------------------------
    '''
    
    '''
    #displaying level from array - will be moved to text file later
    for i in range(0,len(level_map)-1):
        for j in range(len(level_map[i])-1):
            if level_map[i][j] == '1':
                SCREEN.blit(DIRT,(j*tile_width,i*tile_height))
            if level_map[i][j] == '2':
                SCREEN.blit(FLOOR,(j*tile_width,i*tile_height))
                FLOOR_rect = pygame.Rect(j*tile_width,i*tile_height-10,tile_width,20)
                pygame.draw.rect(SCREEN, (255,0,0), FLOOR_rect)
                FLOOR_left_rect = pygame.Rect(j*tile_width-10,i*tile_height+10,30,tile_height-10)
                pygame.draw.rect(SCREEN, (255,255,0), FLOOR_left_rect)
                FLOOR_right_rect = pygame.Rect(j*tile_width+tile_width-10,i*tile_height+10,20,tile_height-10)
                pygame.draw.rect(SCREEN, (255,255,0), FLOOR_right_rect)
                FLOOR_bottom_rect = pygame.Rect(j*tile_width,i*tile_height+tile_height-10,tile_width,20)
                pygame.draw.rect(SCREEN, (200,200,200), FLOOR_bottom_rect)                    
            
            if player_floor_hitbox.colliderect(FLOOR_rect):
                floor = True #setting variable to true when touching floor
                fall = False
            
            
            if player_right_hitbox.colliderect(FLOOR_left_rect):
                #if player_floor_hitbox.colliderect(FLOOR_rect):
                #moving_right = False
                speed = 0
                #if player_floor_hitbox.colliderect(FLOOR_rect):
                    #floor = True
                #if player_floor_hitbox.colliderect(FLOOR_rect):
                PLAYER_POS[0] -= 5 #stops player clipping into side of tile: the two big FLOOR_right_rect's are glitchy with this effect
            if player_left_hitbox.colliderect(FLOOR_right_rect):
                #if player_floor_hitbox.colliderect(FLOOR_rect):
                #moving_left = False
                speed = 0
                #if player_floor_hitbox.colliderect(FLOOR_rect):
                    #floor = True
                #if player_floor_hitbox.colliderect(FLOOR_rect):
                PLAYER_POS[0] += 2 #stops player clipping into side of tile
   '''
    
    
    
    delay = False
    d = 0 #counter for how many times you go through while loop
    index = 0
    angle = 0 #angle to rotate image during melee swing animation
    hitcount = 0
    
    melee = True
    ranged = False
    
    dandelion.set_hp(500) #setting hp of enemy
    
    while True: #making sure that all the changes remain on the screen and don't disappear straight away
        SCREEN.fill((0,181,226))
        PLAY_MOUSE_POS = pygame.mouse.get_pos() 
        speed = 14        
        
        #displaying pause button in top-right corner
        SCREEN.blit(PAUSE_button,(1570,-85))
        
        d = d+1 #tracks how many times the while/play game loop has run
        
        

        
        '''
        angle = angle-6 #turns through clockwise (-ve is clockwise, +ve anticlockwise)      
        if angle == -90:
            angle = 0
            rotate = False
        '''
        
        #-------------------------------------------------
        #SCREEN.blit(FLOOR,(200,500))#testing the floor
        FLOOR_rect = pygame.Rect(200,5000,tile_width,10)
        FLOOR_left_rect = pygame.Rect(200,5000,tile_width,10)
        FLOOR_right_rect = pygame.Rect(200,5000,tile_width,10)
        FLOOR_safe_rect = pygame.Rect(200,5000,tile_width,10)
        FLOOR_bottom_rect = pygame.Rect(200,5000,tile_width,10)
        pygame.draw.rect(SCREEN, (255,0,0), FLOOR_rect)
        #pygame.draw.rect(SCREEN, (255,0,0), FLOOR_rect)
        pygame.draw.rect(SCREEN, (200,0,0), player_hitbox)
        pygame.draw.rect(SCREEN, (234,221,202), player_floor_hitbox)
        pygame.draw.rect(SCREEN, (234,221,202), player_top_hitbox)
        pygame.draw.rect(SCREEN, (234,221,202), player_right_hitbox)
        pygame.draw.rect(SCREEN, (234,221,202), player_left_hitbox)
        SCREEN.blit(DIRT,(331,970))#testing the ground
        SCREEN.blit(FLOOR,(462,970))
        
        
        #-------------------------------------------------        
        


        #displaying level from array - will be moved to text file later
        for i in range(0,len(level_map)-1):
            for j in range(len(level_map[i])-1):
                if level_map[i][j] == '1':
                    SCREEN.blit(DIRT,(j*tile_width,i*tile_height))
                if level_map[i][j] == '2':
                    SCREEN.blit(FLOOR,(j*tile_width,i*tile_height))
                    FLOOR_rect = pygame.Rect(j*tile_width-10,i*tile_height-10,tile_width+20,20)
                    pygame.draw.rect(SCREEN, (255,0,0), FLOOR_rect)
                    FLOOR_left_rect = pygame.Rect(j*tile_width-10,i*tile_height+10,30,tile_height-10)
                    pygame.draw.rect(SCREEN, (255,255,0), FLOOR_left_rect)
                    FLOOR_right_rect = pygame.Rect(j*tile_width+tile_width-10,i*tile_height+10,20,tile_height-10)
                    pygame.draw.rect(SCREEN, (255,255,0), FLOOR_right_rect)
                    FLOOR_bottom_rect = pygame.Rect(j*tile_width,i*tile_height+tile_height-10,tile_width,20)
                    pygame.draw.rect(SCREEN, (200,200,200), FLOOR_bottom_rect)                    
                
                if player_floor_hitbox.colliderect(FLOOR_rect):
                    floor = True #setting variable to true when touching floor
                    fall = False
                #remember put controls back here
                
                
                if player_right_hitbox.colliderect(FLOOR_left_rect):
                    speed = 0
                    PLAYER_POS[0] -= 5 #stops player clipping into side of tile: the two big FLOOR_right_rect's are glitchy with this effect
                
                if player_left_hitbox.colliderect(FLOOR_right_rect):
                    speed = 0
                    PLAYER_POS[0] += 2 #stops player clipping into side of tile
   
        #----------------------------------------------------------------




        if face_left == True:
            SCREEN.blit(PLAYER_LEFT,(PLAYER_POS[0],PLAYER_POS[1]))
            SCREEN.blit(iron_armour_left,(PLAYER_POS[0],PLAYER_POS[1])) #testing armour on player
            SCREEN.blit(wizard_cat_left,(PLAYER_POS[0]+60,PLAYER_POS[1]+PLAYER.get_height()-wizard_cat_left.get_height())) #testing cat following player
            
        
        if face_right == True:
            SCREEN.blit(PLAYER,(PLAYER_POS[0],PLAYER_POS[1]))
            SCREEN.blit(iron_armour_right,(PLAYER_POS[0],PLAYER_POS[1])) #testing armour on player
            SCREEN.blit(wizard_cat_right,(PLAYER_POS[0]-60,PLAYER_POS[1]+PLAYER.get_height()-wizard_cat_right.get_height())) #testing cat following player
        
        if default == True:
            SCREEN.blit(PLAYER,(PLAYER_POS[0],PLAYER_POS[1]))
            SCREEN.blit(iron_armour_right,(PLAYER_POS[0],PLAYER_POS[1])) #testing armour on player
            SCREEN.blit(wizard_cat_right,(PLAYER_POS[0]-60,PLAYER_POS[1]+PLAYER.get_height()-wizard_cat_right.get_height())) #testing cat following player
        
        if moving_right ==  True:
            default = False
            face_left = False
            #SCREEN.blit(PLAYER,(PLAYER_POS[0],PLAYER_POS[1]))
            PLAYER_POS[0] += speed
            face_right = True
        
        if moving_left == True:
            default = False
            face_right = False
            #SCREEN.blit(PLAYER_LEFT,(PLAYER_POS[0],PLAYER_POS[1]))
            PLAYER_POS[0] -= speed
            face_left = True        
        

        
        
        if index == len(dand_right_frames): #check if index points to item that is 1 above the end of the list of frames: if so, reset animation
            index = 0                       #temporary code, unless everything has the same number of animation frames e.g. 6 (which I plan to do)
        

        
        delay = True
        
        #SCREEN.blit(dandelion.get_image(index),(300,200))
        #SCREEN.blit(horizon.get_image(index),(500,200))
        #SCREEN.blit(HORIZON,(400,400))
        #SCREEN.blit(shotgun_gun,(300,300))
        
        #----------------------------------------------------
        #test code for rotating image animation
        if melee == True:
            obba = pygame.image.load("hori2.png")
            obba = pygame.transform.scale(obba,(35,220))
            obba = pygame.transform.rotate(obba,angle)
            obba_center = (PLAYER_POS[0]+50 - (obba.get_width()/2),PLAYER_POS[1]+80 - (obba.get_height()/2))
            SCREEN.blit(obba,obba_center)
       
       
        if ranged == True:
            SCREEN.blit(shotgun.get_image(index),(shotgun.get_posx()+10,shotgun.get_posy()+70))
           
        
        obbabox = pygame.Rect(9000,9000,HORIZON.get_height(),HORIZON.get_width())
            
        
        '''
        obbahitbox = obba.get_rect()
        #obbahitbox.center = (PLAYER_POS[0]+50 + (obba.get_width()/2),PLAYER_POS[1]+80 + (obba.get_height()/2) - (obba.get_height()))
        obbahitbox.center = (PLAYER_POS[0] + PLAYER.get_width()/2 , PLAYER_POS[1] + PLAYER.get_height()/2)
        pygame.draw.rect(SCREEN, (200,0,0), obbahitbox)
        '''
        #----------------------------------------------------
        

        horizon.set_posx(PLAYER_POS[0])
        horizon.set_posy(PLAYER_POS[1])
    
        shotgun.set_posx(PLAYER_POS[0])
        shotgun.set_posy(PLAYER_POS[1])
        
        #--------------------------------------------------------------
        #testing movement of an animated entity - making entity follow player
        enemy_x = dandelion.get_posx()
        enemy_y = dandelion.get_posy()
        enemy_x_speed = 2
        enemy_y_speed = 2
        
        #if enemy collide with floor_left or floor_right rect:
        #   enemy_x_speed = 0
        #   enemy_y_speed = 0
        
        #will initialise dandelion here but with moving_right_frames
        if enemy_x < PLAYER_POS[0]:
            dandelion.set_posx(enemy_x+enemy_x_speed)
        
        #will initialise dandelion here but with moving_left_frames
        if enemy_x > PLAYER_POS[0]:
            dandelion.set_posx(enemy_x-enemy_x_speed)
        
        if enemy_x == PLAYER_POS[0]:
            dandelion.set_posx(PLAYER_POS[0])
        
        if enemy_y < PLAYER_POS[1]-70: #offsetting y pos of enemy so it doesn't look like it's through the floor
            dandelion.set_posy(enemy_y+enemy_y_speed)
    
        if enemy_y > PLAYER_POS[1]-70:
            dandelion.set_posy(enemy_y-enemy_y_speed)
        
        if enemy_y == PLAYER_POS[1]:
            dandelion.set_posy(PLAYER_POS[1])

        #dandelion.set_posx(dandelion.get_posx()+3)
        #dandelion.set_posy(dandelion.get_posy()+5)
        
        currentx = dandelion.get_posx()
        currenty = dandelion.get_posy()
        xj = horizon.get_posx()
        yj = horizon.get_posy
        
        dandrect = dand.get_rect()
        dandrect.center = (currentx + (dand.get_width()/2),currenty + (dand.get_height()/2))
        #pygame.draw.rect(SCREEN, (0,0,55), dandrect)
        
        #---------------------------------------------------------------------------------
        #testing to see that when enemy hp = 0, they are no longer displayed on the screen
        if swing == True:
            if melee == True:
                angle = angle-6 #turns through clockwise (-ve is clockwise, +ve anticlockwise)      
                if angle != -90:
                    obbabox = pygame.Rect(PLAYER_POS[0] + PLAYER.get_width()/2 , PLAYER_POS[1] + PLAYER.get_height()/2,HORIZON.get_height(),HORIZON.get_width())
                    pygame.draw.rect(SCREEN, (200,0,0), obbabox)
                if angle == -90:
                    angle = 0
                    swing = False
            
        if obbabox.colliderect(dandrect):
            hitcount += 1
            
        if swing == False:
            hitcount = 0
            
        if hitcount == 1:
            print("hello")
            dandelion.set_hp(dandelion.get_hp() - 100)
        
        '''
        if dandelion.get_posx() == PLAYER_POS[0] and dandelion.get_posy() == PLAYER_POS[1]-70:
            dandelion.set_hp(dandelion.get_hp() - 5)
        '''
        if dandelion.get_hp() > 0:
            pygame.draw.rect(SCREEN, (0,0,55), dandrect)
            SCREEN.blit(dandelion.get_image(index),(currentx,currenty))
            
        #---------------------------------------------------------------------------------
        
        #SCREEN.blit(dandelion.get_image(index),(currentx,currenty))
        #SCREEN.blit(horizon.get_image(index),(horizon.get_posx(),horizon.get_posy()))
        #SCREEN.blit(shotgun.get_image(index),(shotgun.get_posx()+10,shotgun.get_posy()+70))
        
        #--------------------------------------------------------------
        
        if d == 20: #this is how long each frame stays on the screen for
            index = index + 1
            d = 0


        
        
        #----------------------------------------------------------------
        #trying to represent level in text file
        #there are 19 lines in the text file
        '''
        myFile = open('level_map.txt','r')
        #for j in range(0,19):
        for line in myFile:
            print(line)
            for i in range(len(line)):
                if line[i] == '1':
                    print("hello")
                if line[i] == '2':
                    print("hi")
                if line[i] == '0':
                    print("hey")
        myFile.close()
        '''
        
        
        player_hitbox.x = PLAYER_POS[0]#updating x and y coordinates of hitbox to match player's position
        player_hitbox.y = PLAYER_POS[1]
        
        player_floor_hitbox.x = PLAYER_POS[0]#updating x and y coordinates of player's feet to match player's position
        player_floor_hitbox.y = PLAYER_POS[1]+PLAYER.get_height()
        
        player_top_hitbox.x = PLAYER_POS[0]#updating x and y coordinates of player's feet to match player's position
        player_top_hitbox.y = PLAYER_POS[1]        
        
        player_right_hitbox.x = PLAYER_POS[0]+PLAYER.get_width()
        player_right_hitbox.y = PLAYER_POS[1]
        
        player_left_hitbox.x = PLAYER_POS[0]
        player_left_hitbox.y = PLAYER_POS[1]
        
        #weapon_hitbox.x = PLAYER_POS[0]
        #weapon_hitbox.y = PLAYER_POS[1]
        
        #horizon = weapon(weapon_hitbox.x,weapon_hitbox.y)
        
        #test.x = PLAYER_POS[0]
        #test.y = PLAYER_POS[1]
        
        '''
        #remember y axis is inverted
        while fall == True:
            #before_fall = PLAYER_POS[1]
            PLAYER_POS[1] += gravity
            gravity += 10
            if gravity > 70:
                gravity = 70
            #if PLAYER_POS[1] > before_fall:
                #PLAYER_POS[1] = before_fall
        '''

        

        
        if upwards == True:
            floor = False
            if PLAYER_POS[1] > current_y-300:
                PLAYER_POS[1] -= 25
                #if player_hitbox.colliderect(FLOOR_rect):
                    #upwards = False
                if PLAYER_POS[1] <= current_y-300 or player_top_hitbox.colliderect(FLOOR_bottom_rect):
                    upwards = False
            '''
            before_jump = PLAYER_POS[1]
            if PLAYER_POS[1] > before_jump - 150:
                PLAYER_POS[1] -= 10
            '''
            
        if fall == True:
            PLAYER_POS[1] += 10
            '''
            while gravity < 10:
                gravity += 2
                PLAYER_POS[1] += gravity
            '''

        '''    
        if moving_right == True:
            if player_right_hitbox.colliderect(FLOOR_left_rect):
                go_right = False
            go_right = True
        
        if moving_left == True:
            if player_left_hitbox.colliderect(FLOOR_right_rect):
                go_left = False
            go_left = True
        '''
        if jump == True:
            fall = False
            if floor == True:
                upwards = True
            jump = False
            fall = True
        '''
        if speed_boost == True:
            timer = time.time()
            if timer < 10:
                speed = 280
            speed_boost = False
        '''
        
        if player_floor_hitbox.colliderect(FLOOR_rect): #checking if bottom of player collides with floor
            fall = False
        else:
            fall = True
            floor = False

        
        if PLAY_MOUSE_POS[0] in range(1750,1850) and PLAY_MOUSE_POS[1] in range(30,90):
            SCREEN.blit(PAUSE_hover,(1570,-85))
    
        for event in pygame.event.get(): #this loop is used for all events e.g. button presses or mouse clicks
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() #this loop means: when the window is closed, stop running
                           #without this, the window will not close when the x button is pressed 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_MOUSE_POS[0] in range(1750,1850) and PLAY_MOUSE_POS[1] in range(30,90): #if in range of pause button, pause the game
                    checkpoint = PLAYER_POS
                    pause()
            
            
            if event.type == KEYDOWN: #if the event is a key is being pressed
                '''
                if event.key == K_a:
                    speed_boost = True
                '''
                if event.key == K_RIGHT or event.key == K_d:
                    #PLAYER_POS[0] += 10
                    moving_right = True
                     
                if event.key == K_LEFT or event.key == K_a:
                    #PLAYER_POS[0] -= 10
                    moving_left = True
                
                
                
                
                
                if event.key == K_SPACE:
                    current_y = PLAYER_POS[1]
                    #if player_floor_hitbox.colliderect(FLOOR_rect): #(I think) this is not working, hence why you can jump while in the air
                        #jump = True
                    jump = True
                    #swing = True
                
                if event.key == K_e:

                    PLAYER_POS[0] = PLAY_MOUSE_POS[0]
                    PLAYER_POS[1] = PLAY_MOUSE_POS[1]

            
            
            if event.type == KEYUP:
                if event.key == K_RIGHT or event.key == K_d:
                    moving_right = False
                
                if event.key == K_LEFT or event.key == K_a:
                    moving_left = False
                    
                if event.key == K_SPACE:
                    jump = False
                
                if event.key == K_q:
                    if melee == True:
                        melee = False
                        ranged = True
                
                if event.key == K_w:
                    if ranged == True:
                        ranged = False
                        melee = True
            
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                swing = True
            

        '''    
        if moving_right == True:
            SCREEN.blit(PLAYER,(PLAYER_POS[0],PLAYER_POS[1]))
        if moving_left == True:
            SCREEN.blit(PLAYER_LEFT,(PLAYER_POS[0],PLAYER_POS[1]))
        '''

        #SCREEN.blit(HORIZON,(PLAYER_POS[0],PLAYER_POS[1]))
        SCREEN.blit(projectile1,(500,400))
        
        
        pygame.display.update() #need to update display within the while loop so the correct screen is shown
        clock.tick(60) #setting frame rate to 60 fps
        '''
        print(dandelion.get_posx())
        print(dandelion.get_posy())
        print(PLAYER_POS)
        '''
        
        
def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))#name of image and coordinates: blit means putting that image on top of the current surface
        
        MENUQUIT_button = pygame.image.load("QUIT button.png")
        MENUQUIT_button = pygame.transform.scale(MENUQUIT_button,(1100,750))
        MENUQUIT_hover = pygame.image.load("QUIT hover.png")
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MENU_MOUSE_POS[0] in range(750,1150) and MENU_MOUSE_POS[1] in range(330,450):
                    play(PLAYER_POS)
                if MENU_MOUSE_POS[0] in range(835,1100) and MENU_MOUSE_POS[1] in range(745,860):
                    pygame.quit()
                    sys.exit()
                #if MENU_MOUSE_POS[0] in range(685,1170) and MENU_MOUSE_POS[1] in range(535,650):
                    #options()

        pygame.display.update()
        
main_menu()

#NOTES FOR NEXT TIME:
#-----10/8/22 REPORT-----
#previously working on player movement
#lines 90,91,131,133 and 147-164 added in last update
#also added options button and hover for menu and pause screens

#-----1/9/22 REPORT-----
#got horizontal movement working
#created player model
#created models for floor and ground
#started working on storing level map in external text file and importing it (line 194)

#-----3/9/22 REPORT-----
#attempting to implement jumping and falling
#jump somewhat working, need to fix limit to jump height (currently able to jump infinitely high)
#fix gravity
#remember to check line 330 (temp fix for falling)
#check spacebar key press loop (line mentioned above)

#-----5/9/22 REPORT-----
#floor collisions working (check line 224-232)
#jumping working, fixed infinite jump issue

#-----7/9/22 REPORT-----
#floor collisions working correclty: player can no longer be stuck on the bottom of the floor suspended in the air
#added hitbox to player's feet so floor collisions to also help with issue above
#to fix player clipping slightly through the floor, just raise the coordinates of the floor rect a few pixels up
#represented level as array (very laggy)
#maybe add a player_head_hitbox (just like player_floor_hitbox) so the player can't jump through floors above their head

#-----15/9/22 REPORT-----
#fixed pausing: no longer have to restart level when selecting "continue" from pause menu (did so by adding checkpoint variable)

#-----19/9/22 REPORT-----
#made it so player faces left and right when moving in each direction (using 'face_left' and 'face_right' variables)
#when you start the game or load the play screen from the pause menu, the player is automatically facing right (using 'default' variable)
#note: quitting to main menu from pause menu then selecting play option will not restart level progress - only way to restart is closing game and running it again

#-----19/9/22 REPORT-----
#tested armour on player by blitting new image on top of player model
#tested wizard cat which follows player
#made 'save_point' variable to be used as a checkpoint in the level later on e.g. if you cross save_point and die after, you respawn at save_point instead of beginning of level

#-----27/9/22 REPORT-----
#fixed jumping animation
#trying to fix jumping when clipping throough floor tiles that are above you
#created 'midair' variable so I can start to implement wall sliding/jumping
#wall jumping: if in midair and wall touching wall and jump is pressed, then jump up and outwards






