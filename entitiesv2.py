import pygame
#Entities i.e. enemies and allies
#an entity by itself will just be like an npc - no hp, no dmg, doesn't do anything
class Entity(): #the parent class/superclass for enemies and allies
    def __init__(self, spawnposx, spawnposy):
        self.images = [] #images for animation - should be 10 frames per entity
        self.posx = spawnposx
        self.posy = spawnposy
        self.rect = None
        self.floorRect = None
        self.index = 0
    
    def set_posx(self,newPosx): #this is for when you want to move an entity to a new position from its spawn/current position
        self.posx = newPosx
    
    
    def get_posx(self):
        return self.posx
    
    
    def set_posy(self,newPosy):
        self.posy = newPosy
    
    
    def get_posy(self):
        return self.posy
    
    def set_images(self,imageList):
        self.images = imageList
    
    def get_image(self):
        self.image = self.images[self.index]
        return self.image
        
    
    def set_Rect(self):
        self.rect = self.image.get_rect()
    
    def get_Rect(self):
        return self.rect
    
    def set_floorRect(self):
        self.floorRect = pygame.Rect(self.get_posx(),self.get_posy()+self.images[self.index].get_height(),self.images[self.index].get_width(),10)

    def get_floorRect(self):
        return self.floorRect
        
    

    
class Enemy(Entity):
    def __init__(self, spawnposx, spawnposy, projectile_left, projectile_right):
        super().__init__(spawnposx, spawnposy)
        self.proj_left = projectile_left
        self.proj_right = projectile_right
        self.proj_left_rect = None
        self.proj_right_rect = None
        self.projx = -9000 #nitially set to e.g. 9000 so cannot be seen on screen yet
        self.shootleft = False
        self.shootright = False
        self.image = None
        
        self.maxhp = 0
        self.hp = 0
        self.dmg = 0
        self.speed = 0
        self.dead = False
        
        self.col_right = None
        self.col_left = None
        self.col_floor = False
        
        self.hitnum = 0
        self.allyhitnum = 0
        self.hits = 0
        
        self.hp_bar = None
        self.hp_width = 0
        self.hpback = None
        self.hp_border = None
        
        self.fallspeed = 0
        self.atkcd = 100 #cooldown before each attack, so enemy does not shoot constantly
        self.attack = False
        
        self.distances = []

    def set_atkcd(self,Ncd):
        self.atkcd = Ncd
    
    def set_proj_right_rect(self,scrollx,scrolly):
         self.proj_right_rect = pygame.Rect(self.projx+scrollx,self.posy+scrolly,self.proj_right.get_height(),self.proj_right.get_width())

        
    def get_right_proj_rect(self):
        return self.proj_right_rect
    
    def set_proj_left_rect(self,scrollx,scrolly):
        self.proj_left_rect = pygame.Rect(self.projx+scrollx,self.posy+scrolly,self.proj_left.get_height(),self.proj_left.get_width())

    
    def get_left_proj_rect(self):
        return self.proj_left_rect
    
    #enemy attack - making enemy shoot porjectile and setting up cooldown
    #adjusting player health when hit by enemy projectile
    def atk(self,screen,targetx,target_rect,player_hp,scrollx,scrolly):
        if self.atkcd != 0:
            self.atkcd -= 1
        if self.atkcd == 0:
            if self.posx > targetx:
                if self.projx == -9000: #spawn value
                    self.projx = self.posx
                if self.proj_left_rect.colliderect(target_rect) == False:
                    self.projx -= 7
                    screen.blit(self.proj_left,(self.projx+scrollx,self.posy+scrolly))

                    
                else:
                    self.atkcd = 100
                    self.projx = -9000
                    self.proj_left_rect.x = -9000
                    player_hp = player_hp - self.dmg

                if self.projx < targetx:
                    self.projx = -9000
                    self.proj_left_rect.x = -9000
                    self.atkcd = 100
                
            if self.posx < targetx:
                if self.projx == -9000: 
                    self.projx = self.posx
                if self.proj_right_rect.colliderect(target_rect) == False:

                    self.projx += 7
                    screen.blit(self.proj_right,(self.projx+scrollx,self.posy+scrolly))

                    
                else:
                    self.atkcd = 100
                    self.projx = -9000
                    self.proj_right_rect.x = -9000
                    player_hp = player_hp - self.dmg

                if self.projx > targetx:
                    self.projx = -9000
                    self.proj_left_rect.x = -9000
                    self.atkcd = 100

        return player_hp
            
    def set_hp(self,newhp):
        self.hp = newhp
    
    def get_hp(self):
        return self.hp
    
    def set_dmg(self,newdmg):
        self.dmg = newdmg
    
    def get_dmg(self):
        return self.dmg
   
    def set_speed(self,newSpeed):
        self.speed = newSpeed
    
    def get_speed(self):
        return self.speed
        

        
    #check if enemy touches the ground
    def collide_floor(self,tilerect):
        if self.floorRect.colliderect(tilerect):
            self.col_floor = True
            self.fallspeed = 0
    
    def fall(self):
        self.posy += fallspeed

        

    def collide_right(self,rightrect):
        if self.rect.colliderect(rightrect):
            self.col_right = True
    
    def collide_left(self,leftrect):
        if self.rect.colliderect(leftrect):
            self.col_left = True



    #enemy movement - make enemy move to player's x position
    #check if enemy collides with side of tile/wall
    def movex(self,target_posx,scrollx):   
        if self.col_right == True:
            if self.posx < target_posx:
                self.speed = 2
                self.col_right = False
            else:
                self.speed = 0
        
        if self.col_left == True:
            if self.posx > target_posx:
                self.speed = 2
                self.col_left = False
            else:
                self.speed = 0
        
        if self.posx < target_posx:
            self.posx += self.speed
            
         
        if self.posx > target_posx:
            self.posx -= self.speed
 

    def get_distance(self,targetx):
        return abs(self.posx - targetx)
    
    #adjusting enemy health when hit by player or ally
    def playerhit(self,ally_proj_left_rect,ally_proj_right_rect,wpnrect,swing,width,maxhp):
        if wpnrect.colliderect(self.rect):
            self.hitnum += 1
            
        if swing == False:
            self.hitnum = 0
        
        if self.hitnum == 1:
            self.hp -= 100
            self.hp_width -= width/(maxhp/100) #500 (max hp)/100 (player dmg) = 5
            
            

        if ally_proj_left_rect.colliderect(self.rect) or ally_proj_right_rect.colliderect(self.rect):
            self.allyhitnum += 1
        
        if self.allyhitnum == 1:
            self.hp -= 100
            self.hp_width -= width/(maxhp/100) #500 (max hp)/100 (player dmg) = 5
            
            
        self.allyhitnum = 0


    
         
    #setting up and adjusting enemy hp bar
    
    def set_hpwidth(self,nWidth):
        self.hp_width = nWidth
    
    def get_hpwidth(self):
        return self.hp_width
    
    def set_hpbar(self):
        self.hp_bar = pygame.Rect(self.get_posx(),self.get_posy(),self.hp_width,20)
        
    def get_hpbar(self):
        return self.hp_bar
    
    def set_hpback(self):
        self.hpback = pygame.Rect(self.get_posx(),self.get_posy(),self.image.get_width(),20)
        
    def get_hpback(self):
        return self.hpback
    
    def set_hpborder(self):
        self.hp_border = pygame.Rect(self.get_posx()-10,self.get_posy()+10,self.image.get_width()+10,30)
    
    def get_hpborder(self):
        return self.hp_border
    
    def fall(self):
        self.posy += self.fallspeed
            

    

#make Ally inherit Enemy as a superclass, which is a child class inheriting from Entity
#an Ally will essentially be an enemy that targets enemies rather than the player
class Ally(Enemy):
    def __init__(self, spawnposx, spawnposy, projectile_left, projectile_right):
        super().__init__(spawnposx, spawnposy, projectile_left, projectile_right)
        self.element = None #element will apply debuff to enemy
    
    #polymorphism - adjusting atk method from enemy class
    #makes ally attack enemy
    def atk(self,screen,targetx,target_rect,enemy_hp,scrollx,scrolly):
        if self.atkcd != 0:
            self.atkcd -= 1
        if self.atkcd == 0:
            if self.posx > targetx:
                if self.projx == -9000: #spawn value
                    self.projx = self.posx
                if self.proj_left_rect.colliderect(target_rect) == False:
                    self.projx -= 3
                    screen.blit(self.proj_left,(self.projx+scrollx,self.posy+scrolly))

                    
                else:
                    self.atkcd = 100
                    self.projx = -9000
                    self.proj_left_rect.x = -9000
                    player_hp = player_hp - self.dmg

                if self.projx < targetx:
                    self.projx = -9000
                    self.proj_left_rect.x = -9000
                    self.atkcd = 100
                
            if self.posx < targetx:
                if self.projx == -9000: 
                    self.projx = self.posx
                if self.proj_right_rect.colliderect(target_rect) == False:

                    self.projx += 3
                    screen.blit(self.proj_right,(self.projx+scrollx,self.posy+scrolly))

                    
                else:
                    self.atkcd = 100
                    self.projx = -9000
                    self.proj_right_rect.x = -9000
                    player_hp = player_hp - self.dmg

                if self.projx > targetx:
                    self.projx = -9000
                    self.proj_left_rect.x = -9000
                    self.atkcd = 100

        return enemy_hp
    
    #polymorphism - adjusted movex method from enemy class
    #makes ally move towards player
    #allows ally to phase through walls so they don't get stuck
    def movex(self,target_posx,scrollx):   
        if self.posx < target_posx:
            self.posx += self.speed
            
         
        if self.posx > target_posx:
            self.posx -= self.speed
 
    

    
