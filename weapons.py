class Weapon(): #xpos and ypos will be the x and y position of the player at all times, even while moving
    def __init__(self, xpos, ypos): #i.e. pass in PLAYER_POS[0], PLAYER_POS[1] and make them update as player moves
        self.x = xpos
        self.y = ypos
        self.images = [] #same as enemies: array of animation frames (for left and right if required)
        self.dmg = 0

        
    def set_posx(self,newPosx):
        self.x = newPosx
    
    def get_posx(self):
        return self.x
    
    def set_posy(self,newPosy):
        self.y = newPosy
    
    def get_posy(self):
        return self.y
    
    def set_dmg(self,newDmg):
        self.dmg = newDmg
    
    def get_dmg(self):
        return self.dmg
    
    def set_images(self,imageList):
        self.images = imageList

    def get_image(self,index):
        return self.images[index]

    def set_element(self,newElement):
        self.element = newElement
    
    def get_element(self):
        return self.element
        
#gun inherits weapon
class Gun(Weapon):
    def __init__(self, xpos, ypos):
        super().__init__(xpos, ypos)
        self.projectile = 0 #projectile image
    
    
    #this code was unused due to running out of development time
    def set_projectile(newImage):
        self.projectile = newImage
        
    def get_projectile():
        return self.projectile
        
    