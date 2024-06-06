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
    
    def get_image(self,index):
        return self.images[index]
    
    def set_Rect(self,index):
        self.rect = self.images[index].get_rect()
    
    def get_Rect(self):
        return self.rect
    
    def set_floorRect(self,index):
        self.floorRect = pygame.Rect(self.get_posx(),self.get_posy()+self.images[index].get_height(),self.images[index].get_width(),10)

    def get_floorRect(self):
        return self.floorRect
        
    
    
    '''
    def fall(self,tile_rect):
        if self.floorRect.colliderect(tile_rect) == False:
            print("not touching floor")
            self.posy += 2 #fall down if not touching floor
        else:
            self.posy += 0
        
        return self.posy
    '''


   

    #for i in range(0,6): 6 is the length of the array of frames i.e. 6 frames
        #enemy1.get_image(i)
    
    
    
    #would have a for i in range loop in main code:
    #dandelion = Enemy((400,300))
    #for i in range(0,6):
    #   dandelion.get_image(i)
        


#debuff examples:
#if ally hit enemy:
#    if ally.get_element() == water, enemy.set_debuff(slow) (slow enemy movement speed)
#    if ally.get_element() == fire, enemy.set_debuff(burn) (enemy deal less dmg) 

    
class Enemy(Entity):
    def __init__(self, spawnposx, spawnposy):
        super().__init__(spawnposx, spawnposy)
        self.hp = 0
        self.dmg = 0
        self.speed = 0
        self.debuff = 0
        self.col_right = None
        self.col_left = None
        self.hitnum = 0
        self.hits = 0
        self.hp_bar = None
        self.hp_width = 0
        self.col_floor = False
        self.fallspeed = 0
        self.atkcd = 200 #cooldown before each attack, so enemy does not shoot constantly
        
        
        
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
        
    def set_debuff(self, newDebuff):
        self.debuff = newDebuff
        
    def get_debuff(self):
        return self.debuff
    
    def collide_floor(self,tilerect):
        if self.floorRect.colliderect(tilerect):
            self.col_floor = True
            #print("floor")
            self.fallspeed = 0
    
    def fall(self):
        self.posy += fallspeed

        

    def collide_right(self,rightrect):
        if self.rect.colliderect(rightrect):
            self.col_right = True
    
    def collide_left(self,leftrect):
        if self.rect.colliderect(leftrect):
            self.col_left = True

    #if player moves left, add scroll to enemy movement
    #if player moves right, subtract scroll from enemy movement

    #bugged movement: when ever the player moves, the enemy also moves in their direction i.e. moves a bit extra: this is why enemy backs off from player
    def movex(self,target_posx,scrollx,pright,pleft,pdistance):   
        '''
        if self.col_right == True:
            #print("collide right")
            self.posx += 20
            self.col_right = False
        
        if self.col_left == True:
            #print("collide left")
            self.posx -= 20
            self.col_left = False
        '''
        
        '''
        if pright == True:
            self.posx += 2
            
        if pleft == True:
            self.posx -= 2
        '''    
        
        if self.posx < target_posx:
            self.posx += self.speed
            
         
        if self.posx > target_posx:
            self.posx -= self.speed
 
        '''
        if pright == True:
            self.posx -= 6 #instead of this, I need to subtract the distance has moved by to ammend the scroll issue
        
        if pleft == True:
            self.posx += 6 #instead of this, I need to add the distance has moved by to ammend the scroll issue
        '''
        
        if pdistance != 0:
            
            #if pright == True or pleft == True:
                #self.posx -= pdistance - self.speed
            
            if pright == True:
                self.posx += self.speed - pdistance
            
            if pleft == True:
                self.posx -= self.speed + pdistance
            
        #return self.posx,scrollx
    
    def playerhit(self,wpnrect,swing,width,maxhp):
        if wpnrect.colliderect(self.rect):
            self.hitnum += 1
            
        if swing == False:
            self.hitnum = 0
        
        if self.hitnum == 1:
            self.hp -= 100
            self.hp_width -= width/(maxhp/100) #500 (max hp)/100 (player dmg) = 5
            
            print("hit")

    def hit(self,player_rect,player_hp):
        if player_rect.colliderect(self.rect):
            self.hits += 1
            print("hitting")
            if self.hits == 1:
                player_hp = player_hp - self.dmg
        else:
            self.hits = 0
            print("not hitting")
            #hit = True
        #self.hits = 0
            
        return player_hp
         
    
    def check(self,player_hp):
        player_hp -= 100
    
    def set_hpwidth(self,nWidth):
        self.hp_width = nWidth
    
    def get_hpwidth(self):
        return self.hp_width
    
    def set_hpbar(self,index):
        self.hp_bar = pygame.Rect(self.get_posx(),self.get_posy(),self.hp_width,20)
        
    def get_hpbar(self):
        return self.hp_bar
    
    def fall(self):
        self.posy += self.fallspeed
            

    

#make Ally inherit Enemy as a superclass, which is a child class inheriting from Entity
#an Ally will essentially be an enemy that targets enemies rather than the player
class Ally(Enemy):
    def __init__(self, spawnposx, spawnposy):
        super().__init__(spawnposx, spawnposy)
        self.element = 0 #element will apply debuff to enemy
        
        


class Cat(Entity): #this will have the different ability for the cat passsed in e.g. Cat.set_ability() and a getter
    def __init__(self, spawnposx, spawnposy):
        super().__init__(spawnposx, spawnposy)
        self.ability = 0
    