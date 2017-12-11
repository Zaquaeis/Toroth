import pygame

# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BROWN = (200,200,20)
# size of a tile
SIZE = 75

class Player(pygame.sprite.Sprite):
    def __init__(self):

 
       # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
 
       # Load the image
        self.image = pygame.image.load("player2.png").convert()
 
        # Set our transparent color
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.left += 15
        self.rect.right -= 15
        self.is_player = True
    
class Tree(pygame.sprite.Sprite):
    def __init__(self):
    

       # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
 
       # Load the image
        self.image = pygame.image.load("tree.png").convert()
 
        # Set our transparent color
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.barrier = True
        self.ch = 'T'
        self.is_player = False
        #is_barrier detects if collision detection is required

class Cobble(pygame.sprite.Sprite):
    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("CobblePath75x75.V1.1.png").convert()

#Do we even need this shit?
        #self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.barrier = False
        self.ch = "C"
        self.is_player = False
        
class Grass(pygame.sprite.Sprite):
    """
    This class represents the ball.
    It derives from the "Sprite" class in Pygame.
    """


    def __init__(self):
   
  
 
        
        pygame.sprite.Sprite.__init__(self)


        self.image = pygame.Surface([75, 75])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.barrier = False
        self.ch = ' '
        self.is_player = False    

class Water(pygame.sprite.Sprite):
    """
    This class represents the ball.
    It derives from the "Sprite" class in Pygame.
    """


    def __init__(self):
 
        pygame.sprite.Sprite.__init__(self)


        self.image = pygame.Surface([75,75])
        self.image.fill(BLUE)
        self.barrier = True
        self.rect = self.image.get_rect()
        self.ch = 'A'
        self.is_player = False
class Block(pygame.sprite.Sprite):
    """
    This class represents the ball.
    It derives from the "Sprite" class in Pygame.
    """


    def __init__(self):
  
        pygame.sprite.Sprite.__init__(self)


        self.image = pygame.Surface([75, 75])
        self.image.fill(RED)
        self.barrier = True
        self.rect = self.image.get_rect()
        self.ch = 'W'
        self.is_player = False
        

class Door(pygame.sprite.Sprite):
    """
    This class represents the ball.
    It derives from the "Sprite" class in Pygame.
    """


    def __init__(self):
  
        pygame.sprite.Sprite.__init__(self)


        self.image = pygame.Surface([75, 75])
        self.image.fill(BROWN)
        self.barrier = True
        self.rect = self.image.get_rect()
        self.ch = 'D'
        self.is_player = False
        self.map_portal = 'map2.txt'
TILE_DICT = {'D':Door,'A':Water,'W':Block,'T':Tree,' ':Grass,'B':Block,'P':Grass,'H':Grass,'R':Grass,'O':Grass,'S':Grass,'C':Cobble}
#list of all tiles and what constructors to call
def draw(text,x_dim,y_dim,bl,al):
   tiles = [y_dim*[None]]*x_dim
   f = open(text,'r')
   m = f.read()
   x = 0
   y = 0
   #read the file as a string, and move char by char calling the appropriate constructor for the given char
   for character in m:
       
       if character != '\n':
           tiles[x][y] = TILE_DICT[character]()
           tiles[x][y].rect.x = x*(SIZE)
           tiles[x][y].rect.y = y*(SIZE)
           if tiles[x][y].barrier:
               bl.add(tiles[x][y])
           al.add(tiles[x][y])
           x += 1
        
           
       else:
           y +=1
           x = 0


   return tiles
pygame.init()
x_speed = 0
y_speed = 0
TILE_DIMX = 10
TILE_DIMY = 10
# Set the height and width of the screen
screen_width = SIZE*TILE_DIMX
screen_height = SIZE*TILE_DIMY
screen = pygame.display.set_mode([screen_width, screen_height])

block_list = pygame.sprite.Group()

all_sprites_list = pygame.sprite.Group()
tiles = draw('map.txt',53,52,block_list,all_sprites_list)
x_start = 26
y_start = 37
        
        
  


player = Player()

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
player.rect.x = TILE_DIMX*SIZE/2
player.rect.y = TILE_DIMY*SIZE/2
for t in all_sprites_list:

    if not t.is_player:
        t.rect.x -= (x_start - (TILE_DIMX/2))*SIZE
        t.rect.y -= (y_start - (TILE_DIMY/2))*SIZE
        
        
# -------- Main Program Loop -----------

while not done:
    open_attempt = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_LEFT:
                x_speed = -8
            elif event.key == pygame.K_RIGHT:
                x_speed = 8
            elif event.key == pygame.K_UP:
                y_speed = -8
            elif event.key == pygame.K_DOWN:
                y_speed = 8
            elif event.key == pygame.K_w:
                open_attempt = True
            
                
        # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0
    
    screen.fill(GREEN)
    x1 = player.rect.x
    y1 = player.rect.y
    player.rect.x += x_speed
    player.rect.y += y_speed
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, False)
    if len(blocks_hit_list) >0:
        
        for entry in blocks_hit_list:
            if hasattr(entry,'map_portal') and open_attempt:
                block_list = pygame.sprite.Group()

                all_sprites_list = pygame.sprite.Group()
                tiles = draw(entry.map_portal,52,52,block_list,all_sprites_list)
                player.rect.x =200
                player.rect.y = 200
        
        player.rect.x -= x_speed
        player.rect.y -= y_speed
    else:
       for s in all_sprites_list:
           if not s.is_player:
               s.rect.x -= x_speed
               s.rect.y -= y_speed
       player.rect.x -= x_speed
       player.rect.y -= y_speed

    all_sprites_list.draw(screen)
    screen.blit(player.image,player.rect)
# Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
pygame.quit()



