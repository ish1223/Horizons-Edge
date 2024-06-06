import pygame,sys,random,time,math


from entitiesv2 import *
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

#these are for entering cheat codes - this  feature will be available on the options screen
CODE_button = pygame.image.load("CODE button.png").convert_alpha()
CODE_button = pygame.transform.scale(CODE_button,(900,600))

CODE_hover = pygame.image.load("CODE hover.png").convert_alpha()
CODE_hover = pygame.transform.scale(CODE_hover,(900,600))

PLAYER = pygame.image.load("PLAYER.png").convert_alpha()
PLAYER = pygame.transform.scale(PLAYER,(80,140))

PLAYER_LEFT = pygame.transform.flip(PLAYER,True,False)

#PLAYER_LEFT = pygame.image.load("PLAYER LEFT.png").convert_alpha()
#PLAYER_LEFT = pygame.transform.scale(PLAYER_LEFT,(80,140))

#load in all images for every frame of every entity

iron_armour_right = pygame.image.load("iron armour right.png").convert_alpha()
iron_armour_right = pygame.transform.scale(iron_armour_right,(80,140))

iron_armour_left = pygame.transform.flip(iron_armour_right,True,False)

#iron_armour_left = pygame.image.load("iron armour left.png").convert_alpha()
#iron_armour_left = pygame.transform.scale(iron_armour_left,(80,140))

wizard_cat_right = pygame.image.load("wizard cat right.png").convert_alpha()
wizard_cat_right = pygame.transform.scale(wizard_cat_right,(102,1350/28))

wizard_cat_left = pygame.transform.flip(wizard_cat_right,True,False)

#wizard_cat_left = pygame.image.load("wizard cat left.png").convert_alpha()
#wizard_cat_left = pygame.transform.scale(wizard_cat_left,(102,1350/28))

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

#shotgun_gun_left = pygame.image.load("shotgun_left.png").convert_alpha()
#shotgun_gun_left = pygame.transform.scale(shotgun_gun_left,(200,25))


dand = pygame.image.load("dandelion_enemy.png").convert_alpha()
dand = pygame.transform.scale(dand,(200,200))

snake_left = pygame.image.load("snake left.png").convert_alpha()
snake_left = pygame.transform.scale(snake_left,(150,150))

snake_right = pygame.transform.flip(snake_left,True,False)

#snake_right = pygame.image.load("snake right.png").convert_alpha()
#snake_right = pygame.transform.scale(snake_right,(150,150))





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

#venom_right = pygame.image.load("venom right.png").convert_alpha()
#venom_right = pygame.transform.scale(venom_right,(150,150))

horizon = Weapon(PLAYER_POS[0],PLAYER_POS[1])
hori_right_frames = [HORIZON,wizard_cat_right,PLAYER_LEFT]
horizon.set_images(hori_right_frames)

shotgun = Gun(PLAYER_POS[0]-PLAYER.get_width(),PLAYER_POS[1])
shotgun_right_frames = [shotgun_gun,shotgun_gun,shotgun_gun]
shotgun.set_images(shotgun_right_frames)
shotgun_left_frames = [shotgun_gun_left,shotgun_gun_left,shotgun_gun_left]
shotgun_shoot_right_frames = []
shotgun_shoot_left_frames = []


dandelion = Enemy(1200,400,venom_left,venom_right)
#dand_right_frames = [snake_left,snake_right,wizard_cat_right]
dandelion.set_images([snake_left,snake_right,wizard_cat_right])
dandelion.set_dmg(1)

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

enemies = []
enemies.append(dandelion)
enemies.append(snake1)

enemies.append(snake2)
enemies.append(snake3)
enemies.append(snake4)

def get_font(size): #getting the font that I imported from the video I have referenced in the document
    return pygame.font.Font("font.ttf", size)

def pause():
    while True:
        pygame.mouse.set_visible(True) #making mouse visible again
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
                    play(PLAYER_POS,PLAYER_hp)
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

def play(PLAYER_POS,PLAYER_hp): #maybe pass in save_point as a parameter, and set it to True when you pass checkpoint i.e. play(PLAYER_POS,save_point) would be play(PLAYER_POS,True)

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


    #--------------------------------------------------------------------------------------------
    #save_point = False #checkpoint for level
    #if save_point == True: 
        #PLAYER_POS = [7000,500] #position of checkpoint that player will respawn at if they die

    #if player_hitbox.colliderect(save_point_rect):
        #save_point = True
    #--------------------------------------------------------------------------------------------
    
    realscroll = [0,0] #how far screen scrolls by on x and y axis - for camera movement 
    
    
    
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


    
    
    
    delay = False
    d = 0 #counter for how many times you go through while loop
    index = 0
    angle = 0 #angle to rotate image during melee swing animation
    aimangle = 0
    cd = 0 #ability cooldown
    enemySpeed = 4
    
    melee = True
    ranged = False
    
    for h in range(len(enemies)):
        enemies[h].set_hp(500) #setting hp of enemy
        #dandmaxhp = dandelion.get_hp()
        enemies[h].set_hpwidth(enemies[h].get_image().get_width())
    #PLAYER_hp = 500
    
    while True: #making sure that all the changes remain on the screen and don't disappear straight away
        
        for h in range(len(enemies)):
            enemies[h].fall()
            enemies[h].fallspeed = 10 #GRAVITY WORKS
        distance1 = PLAYER_POS[0]
        SCREEN.fill((0,181,226))
        #SCREEN.fill((255,0,0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos() 
        speed = 14
        
        pygame.mouse.set_visible(False) #making mouse cursor invisible
        
        realscroll[0] -= (PLAYER_POS[0]+realscroll[0]-x/2+PLAYER.get_width()/2)/30 #how fast/slow the camera catches up to the player's central position (can be changed by the divider e.g. 30 -> 50 is slower)
        realscroll[1] -= (PLAYER_POS[1]-y/2+PLAYER.get_height()/2+realscroll[1])/30
        scroll = realscroll.copy()
        scroll[0] = int(scroll[0])
        scroll[1] = int(scroll[1])
        

        
        #if PLAYER_POS[1] >= -100:
            #scroll[1] = 0
        
        

        
        d = d+1 #tracks how many times the while/play game loop has run
        if cd != 0: #if ability is on cooldown, reduce cooldown until 0
            cd -= 1
        
        
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
        #pygame.draw.rect(SCREEN, (255,0,0), FLOOR_rect)
        #pygame.draw.rect(SCREEN, (255,0,0), FLOOR_rect)
        pygame.draw.rect(SCREEN, (200,0,0), player_hitbox)
        pygame.draw.rect(SCREEN, (234,221,202), player_floor_hitbox)
        pygame.draw.rect(SCREEN, (234,221,202), player_top_hitbox)
        pygame.draw.rect(SCREEN, (234,221,202), player_right_hitbox)
        pygame.draw.rect(SCREEN, (234,221,202), player_left_hitbox)
        SCREEN.blit(DIRT,(200,5000))#testing the ground
        SCREEN.blit(FLOOR,(200,5000))
        

        '''
        if PLAYER_hp == 1:
            SCREEN.blit(heart,(50,25))
        if PLAYER_hp == 2:
            SCREEN.blit(heart,(50,25))
            SCREEN.blit(heart,(250,25))
        if PLAYER_hp == 3:
            SCREEN.blit(heart,(50,25))
            SCREEN.blit(heart,(250,25))
            SCREEN.blit(heart,(450,25))
        '''
        
        #-------------------------------------------------        
        #if index == len(dand_right_frames): #check if index points to item that is 1 above the end of the list of frames: if so, reset animation
            #index = 0                       #temporary code, unless everything has the same number of animation frames e.g. 6 (which I plan to do)
        
        #testing movement of an animated entity - making entity follow player
        enemy_x = dandelion.get_posx()
        enemy_y = dandelion.get_posy()
        
        

        #dandelion.set_posx(dandelion.get_posx()+3)
        #dandelion.set_posy(dandelion.get_posy()+5)

        
        #enemies[h].get_posx() = dandelion.get_posx()
        #enemies[h].get_posy() + scroll[1] = dandelion.get_posy() + scroll[1] #add on scroll so that the enemy's ypos is given the illusion of
                                                    #remaining static on screen - without this, it looks like the enemy
                                                    #moves up and down when really it's everything else scrolling on the screen
        
        #initialising some enemy attributes
        for h in range(len(enemies)):
            #enemies[h].get_image() = dandelion.get_image(index)
            enemies[h].get_image()
            #bookmarkj
            enemies[h].set_Rect()
            dandrect = dandelion.get_Rect()

            if enemies[h].get_Rect().colliderect(FLOOR_right_rect) == False:
                enemies[h].set_speed(enemySpeed) #enemySpeed initially = 2
                #print("no")

            enemies[h].set_floorRect()
            dandfloorRect = dandelion.get_floorRect()
            
            
            dandhp = dandelion.get_hpwidth
            
            enemies[h].set_hpbar()
            enemies[h].set_hpborder()
            enemies[h].set_hpback()
            
            #dandhpbar = dandelion.get_hpbar()
            #dandhpborder = dandelion.get_hpborder()
            
            #dandhpback = pygame.Rect(dandelion.get_posx(),dandelion.get_posy()+enemies[h].get_image().get_height(),enemies[h].get_image().get_width(),20)
            
            if enemies[h].get_hp() > 0:
                enemies[h].get_Rect().center = (enemies[h].get_posx() + (enemies[h].get_image().get_width()/2)+scroll[0],enemies[h].get_posy() + scroll[1] + (enemies[h].get_image().get_height()/2))
                enemies[h].get_floorRect().center = (enemies[h].get_posx() + (enemies[h].get_image().get_width()/2)+scroll[0],enemies[h].get_posy() + scroll[1] + (enemies[h].get_image().get_height()))
                enemies[h].get_hpback().center = (enemies[h].get_posx() + (enemies[h].get_image().get_width()/2)+scroll[0],enemies[h].get_posy() + scroll[1])
                enemies[h].get_hpbar().center = (enemies[h].get_posx() + (enemies[h].get_image().get_width()/2)+scroll[0],enemies[h].get_posy() + scroll[1])
                enemies[h].get_hpborder().center = (enemies[h].get_posx() + (enemies[h].get_image().get_width()/2)+scroll[0],enemies[h].get_posy() + scroll[1])
                
            else:
                enemies[h].get_Rect().center = (9000,9000)
                enemies[h].get_floorRect().center = (9000,9000)
                enemies[h].get_hpbar().center = (9000,9000)
                enemies[h].get_hpborder().center = (9000,9000)
                enemies[h].get_hpback().center = (9000,9000)
                enemies[h].set_atkcd(9000) #removes bug where sometimes would see "final" projectile falling thropugh floor towards new ypos, 9000

            
            
            
        #hp_bar here bookmarkj
        
        #dandelion.fall(FLOOR_rect) #not working properly
        

        #level_map is an array created from the imported text file for the level map
        for i in range(0,len(level_map)-1):
            for j in range(len(level_map[i])-1):
                if level_map[i][j] == '1':
                    SCREEN.blit(DIRT,(j*tile_width + scroll[0],i*tile_height + scroll[1]))
                if level_map[i][j] == '2':
                    SCREEN.blit(FLOOR,(j*tile_width + scroll[0],i*tile_height + scroll[1]))
                    FLOOR_rect = pygame.Rect(j*tile_width-10 + scroll[0],i*tile_height-10 + scroll[1],tile_width+20,20)
                    pygame.draw.rect(SCREEN, (255,0,0), FLOOR_rect)
                    FLOOR_left_rect = pygame.Rect(j*tile_width-10 + scroll[0],i*tile_height+10 + scroll[1],30,tile_height-10)
                    pygame.draw.rect(SCREEN, (255,255,0), FLOOR_left_rect)
                    FLOOR_right_rect = pygame.Rect(j*tile_width+tile_width-10 + scroll[0],i*tile_height+10 + scroll[1],20,tile_height-10)
                    pygame.draw.rect(SCREEN, (255,255,0), FLOOR_right_rect)
                    FLOOR_bottom_rect = pygame.Rect(j*tile_width + scroll[0],i*tile_height+tile_height-10 + scroll[1],tile_width,20)
                    pygame.draw.rect(SCREEN, (200,200,200), FLOOR_bottom_rect)                    
                
                if player_floor_hitbox.colliderect(FLOOR_rect):
                    floor = True #setting variable to true when touching floor
                    fall = False
                #remember put controls back here
                
                
                if player_right_hitbox.colliderect(FLOOR_left_rect):
                    speed = 0
                    #PLAYER_POS[0] -= 5 #this is the old code that caused the player jittering
                    if moving_left == True:
                        speed = 14
                
                if player_left_hitbox.colliderect(FLOOR_right_rect):
                    speed = 0
                    #PLAYER_POS[0] += 2 #old code that caused jitter effect
                    if moving_right == True:
                        speed = 14
                        
                for h in range(len(enemies)):
                    enemies[h].collide_floor(FLOOR_rect)
                    enemies[h].collide_right(FLOOR_right_rect)
                    enemies[h].collide_left(FLOOR_left_rect)

                    
                '''
                dandelion.collide_floor(FLOOR_rect)
                dandelion.collide_right(FLOOR_right_rect)
                dandelion.collide_left(FLOOR_left_rect)
                '''
                #if dandelion.get_floorRect().colliderect(FLOOR_rect) == False:
                #    dandelion.posy += 0.01
                #else:
                #    dandelion.posy -= 1
                
                #print(a)
                
                '''
                if dandrect.colliderect(FLOOR_right_rect):
                    #dandelion.set_speed(dandelion.get_speed()+speed)
                    dandelion.set_posx(enemies[h].get_posx()+20)
                    #print("collide")

                if dandrect.colliderect(FLOOR_left_rect):
                    #dandelion.set_speed(dandelion.get_speed()-speed)
                    dandelion.set_posx(enemies[h].get_posx()-20)
                    #print("collide")
                '''
                    
        #----------------------------------------------------------------


        #dandelion.noFloor(FLOOR_rect)
        
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
    
        if moving_right ==  True:
            default = False
            face_left = False
            #SCREEN.blit(PLAYER,(PLAYER_POS[0],PLAYER_POS[1]))
            PLAYER_POS[0] += speed
            face_right = True
            #distance2 = PLAYER_POS[0]
            #distance = distance2 - distance1
        
        if moving_left == True:
            default = False
            face_right = False
            #SCREEN.blit(PLAYER_LEFT,(PLAYER_POS[0],PLAYER_POS[1]))
            PLAYER_POS[0] -= speed
            face_left = True
            #distance2 = PLAYER_POS[0]
            #distance = distance2 - distance1
            

        
        

        #----------------------------------------------------
        

        horizon.set_posx(PLAYER_POS[0])
        horizon.set_posy(PLAYER_POS[1])
    
        shotgun.set_posx(PLAYER_POS[0] - PLAYER.get_width())
        shotgun.set_posy(PLAYER_POS[1])
        
        #--------------------------------------------------------------
        
        delay = True
        
        #SCREEN.blit(dandelion.get_image(index),(300,200))
        #SCREEN.blit(horizon.get_image(index),(500,200))
        #SCREEN.blit(HORIZON,(400,400))
        #SCREEN.blit(shotgun_gun,(300,300))
        
        #----------------------------------------------------
        #test code for rotating image animation
        if melee == True:
            hori2 = pygame.image.load("hori2.png").convert_alpha()
            if face_left == True:
                hori2 = pygame.transform.flip(hori2,True,False)
                #hori2 = pygame.image.load("hori2 left.png")
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
            #print(aimangle)
            
            '''
            if aimangle > 90 or aimangle < -90:
                shotgun.set_images(shotgun_left_frames)
                shotty_center = (PLAYER_POS[0]+50 - (shotty.get_width()/2) + scroll[0],PLAYER_POS[1]+80 - (shotty.get_height()/2) + scroll[1])
            else:
                shotgun.set_images(shotgun_right_frames)
                shotty_center = (PLAYER_POS[0]+50 - (shotty.get_width()/2) + scroll[0],PLAYER_POS[1]+80 - (shotty.get_height()/2) + scroll[1]) 
            shotty = shotgun.get_image(index)
            '''
            
            shotty = pygame.transform.rotate(shotty,aimangle)
            shotty_center = (PLAYER_POS[0]+50 - (shotty.get_width()/2) + scroll[0],PLAYER_POS[1]+80 - (shotty.get_height()/2) + scroll[1])
            SCREEN.blit(shotty,shotty_center)
           
        
        horibox = pygame.Rect(9000,9000,HORIZON.get_height(),HORIZON.get_width())
            
        
        '''
        hori2hitbox = hori2.get_rect()
        #hori2hitbox.center = (PLAYER_POS[0]+50 + (hori2.get_width()/2),PLAYER_POS[1]+80 + (hori2.get_height()/2) - (hori2.get_height()))
        hori2hitbox.center = (PLAYER_POS[0] + PLAYER.get_width()/2 , PLAYER_POS[1] + PLAYER.get_height()/2)
        pygame.draw.rect(SCREEN, (200,0,0), hori2hitbox)
        '''



        xj = horizon.get_posx()
        yj = horizon.get_posy
        
        #---------------------------------------------------------------------------------
        #testing to see that when enemy hp = 0, they are no longer displayed on the screen
        if swing == True:
            if melee == True:
                if face_right == True or default == True:
                    angle = angle-6 #turns through clockwise (-ve is clockwise, +ve anticlockwise)
                    if angle != -90:
                        horibox = pygame.Rect(PLAYER_POS[0] + PLAYER.get_width()/2 + scroll[0] , PLAYER_POS[1] + PLAYER.get_height()/2 - HORIZON.get_height() + 20 + scroll[1], HORIZON.get_height(),HORIZON.get_height())
                        pygame.draw.rect(SCREEN, (200,0,0), horibox)
                    if angle == -90:
                        angle = 0
                        swing = False
                else:
                    angle = angle+6 #turns through clockwise (-ve is clockwise, +ve anticlockwise)      
                    if angle != 90:
                        horibox = pygame.Rect(PLAYER_POS[0]-29 - PLAYER.get_width()/2 + scroll[0] , PLAYER_POS[1] + PLAYER.get_height()/2 - HORIZON.get_height() + 20 + scroll[1], HORIZON.get_height(),HORIZON.get_height())
                        pygame.draw.rect(SCREEN, (200,0,0), horibox)
                    if angle == 90:
                        angle = 0
                        swing = False
                
         
        
        for h in range(len(enemies)):
            enemies[h].maxhp = 500
            enemies[h].set_proj_right_rect(scroll[0],scroll[1])
            enemies[h].set_proj_left_rect(scroll[0],scroll[1])
            PLAYER_hp = enemies[h].atk(SCREEN,PLAYER_POS[0],player_hitbox,PLAYER_hp,scroll[0],scroll[1])
            #andelion.set_atkcd()
            #print(dandelion.get_atkcd())
            
            enemies[h].playerhit(horibox,swing,enemies[h].get_image().get_width(),enemies[h].maxhp)
            #PLAYER_hp = dandelion.hit(player_hitbox,PLAYER_hp)
            enemies[h].check(PLAYER_hp)
            
            pygame.draw.rect(SCREEN, (0,0,55), enemies[h].get_Rect())
            pygame.draw.rect(SCREEN, (255, 165, 0), enemies[h].get_floorRect())
            
            pygame.draw.rect(SCREEN, (0,0,0), enemies[h].get_hpborder())
            pygame.draw.rect(SCREEN, (255,0,0), enemies[h].get_hpback())
            pygame.draw.rect(SCREEN, (0,255,0), enemies[h].get_hpbar())
            
            #if dandrect.colliderect(player_hitbox):
                #PLAYER_hp -= dandelion.get_dmg()
            
            #dandelion.hit(player_hitbox)
            
        if PLAYER_hp <= 0:
            main_menu()
        #print(PLAYER_hp)
        
        
        '''
        if horibox.colliderect(dandrect):
            hitcount += 1
            
        if swing == False:
            hitcount = 0
            
        if hitcount == 1:
            print("hello")
            dandelion.set_hp(dandelion.get_hp() - 100)
        '''


        #---------------------------------------------------------------------------------
        
        #SCREEN.blit(dandelion.get_image(index),(enemies[h].get_posx(),enemies[h].get_posy() + scroll[1]))
        #SCREEN.blit(horizon.get_image(index),(horizon.get_posx(),horizon.get_posy()))
        #SCREEN.blit(shotty,(shotgun.get_posx()+10,shotgun.get_posy()+70))
        
        #--------------------------------------------------------------
        
        if d == 20: #this is how long each frame stays on the screen for
            #index = index + 1
            d = 0
        
        
        for h in range(len(enemies)):
            if enemies[h].get_posx() > PLAYER_POS[0]:
                enemies[h].index = 0
            if enemies[h].get_posx() < PLAYER_POS[0]:
                enemies[h].index = 1
            #else:
                #index = 1

        
        
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

        SCREEN.blit(PAUSE_button,(1570,-85))
        
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
                    checkpoint[1] -= 150 #stops player falling through floor when you press continue
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
                    
                if event.key == K_e:
                    if cd == 0: #prevents cooldown from extending while cooldown is already active i.e. if press e while on cooldown, cooldown doesn't reset to 200 again
                        cd = 200 #setting ability on cooldown
                        PLAYER_POS[0] = PLAY_MOUSE_POS[0] - scroll[0]
                        PLAYER_POS[1] = PLAY_MOUSE_POS[1] - scroll[1] - 10 - PLAYER.get_height() #making it so the bottom of the player goes to the mouse pos instead of top
                                                                                                 #taking off extra 10 to make it harder to teleport inside of a floor

            
            
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
        
        distance2 = PLAYER_POS[0]
        distance = distance2 - distance1
        #print(distance2,distance1,distance)
        #print(scroll[0])
        for h in range(len(enemies)):
            enemies[h].movex(PLAYER_POS[0],scroll[0],moving_right,moving_left,distance/2) #I think the camera scroll messes up the collisions with sides of tiles (do -scroll[0])

            if enemies[h].get_hp() > 0:
                #pygame.draw.rect(SCREEN, (0,0,55), dandrect)
                #SCREEN.blit(dandelion.get_image(index),(enemies[h].get_posx(),enemies[h].get_posy() + scroll[1]))
                SCREEN.blit(enemies[h].get_image(),(enemies[h].get_posx()+scroll[0],enemies[h].get_posy() + scroll[1]))

        '''    
        if moving_right == True:
            SCREEN.blit(PLAYER,(PLAYER_POS[0],PLAYER_POS[1]))
        if moving_left == True:
            SCREEN.blit(PLAYER_LEFT,(PLAYER_POS[0],PLAYER_POS[1]))
        '''

        #SCREEN.blit(HORIZON,(PLAYER_POS[0],PLAYER_POS[1]))
        #SCREEN.blit(venom_left,(500,400))
        #SCREEN.blit(venom_right,(700,500))
        
        #displaying pause button in top-right corner
        
        SCREEN.blit(ability_cd,(-100,700))
        if cd == 0: #if ability not on cooldown
            SCREEN.blit(ability_button,(-100,700))
        SCREEN.blit(crosshair,(PLAY_MOUSE_POS[0]-20,PLAY_MOUSE_POS[1]-20))
        
        SCREEN.blit(noheart,(50,25))
        SCREEN.blit(noheart,(250,25))
        SCREEN.blit(noheart,(450,25))
        
        #SCREEN.blit(snake_left,(50,300))
        
        if PLAYER_hp >= 1:
            SCREEN.blit(heart,(50,25))
        if PLAYER_hp >= 2:
            SCREEN.blit(heart,(250,25))
        if PLAYER_hp >= 3:
            SCREEN.blit(heart,(450,25))
        
        pygame.display.update() #need to update display within the while loop so the correct screen is shown
        clock.tick(60) #setting frame rate to 60 fps
        '''
        print(dandelion.get_posx())
        print(dandelion.get_posy())
        print(PLAYER_POS)
        '''

        
def main_menu():
    while True:
        pygame.mouse.set_visible(True) #making mouse visible again
        SCREEN.blit(BG, (0, 0))#name of image and coordinates: blit means putting that image on top of the current surface
        
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MENU_MOUSE_POS[0] in range(750,1150) and MENU_MOUSE_POS[1] in range(330,450):
                    play(PLAYER_POS,PLAYER_hp)
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








