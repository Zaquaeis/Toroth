import pygame

# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (0,255,0)
BLUE = (0,0,255)


class Player(pygame.sprite.Sprite):
    def __init__(self):
   
 
       # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
 
       # Load the image
        self.image = pygame.image.load("player.png").convert()
 
        # Set our transparent color
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.left += 15
        self.rect.right -= 15
class Tree(pygame.sprite.Sprite):
    def __init__(self):
    
 
       # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
 
       # Load the image
        self.image = pygame.image.load("tree.png").convert()
 
        # Set our transparent color
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.barrier = False
        self.ch = 'T'

class Grass(pygame.sprite.Sprite):
    """
    This class represents the ball.
    It derives from the "Sprite" class in Pygame.
    """


    def __init__(self, width, height):
   
  
 
        
        pygame.sprite.Sprite.__init__(self)


        self.image = pygame.Surface([width, height])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.barrier = False
        self.ch = ' '
                

class Water(pygame.sprite.Sprite):
    """
    This class represents the ball.
    It derives from the "Sprite" class in Pygame.
    """


    def __init__(self, width, height):
 
        pygame.sprite.Sprite.__init__(self)


        self.image = pygame.Surface([width, height])
        self.image.fill(BLUE)
        self.barrier = True
        self.rect = self.image.get_rect()
        self.ch = 'A'
class Block(pygame.sprite.Sprite):
    """
    This class represents the ball.
    It derives from the "Sprite" class in Pygame.
    """


    def __init__(self, width, height):
  
        pygame.sprite.Sprite.__init__(self)


        self.image = pygame.Surface([width, height])
        self.image.fill(RED)
        self.barrier = True
        self.rect = self.image.get_rect()
        self.ch = 'W'
def draw(text):
    tiles = []
    f = open(text,'r')
    print f
    m = f.read()
    print m
    x= 0
    y = 0
    for ch in m:
        
    
        if ord(ch) ==32:
                tile = Grass(75,75)
                tile.rect.x = x
                tile.rect.y = y
                tiles.append(tile)
        if ch == 'A':
                tile = Water(75,75)
                tile.rect.x = x
                tile.rect.y = y
                tiles.append(tile)
        if ch == 'W':
                tile = Block(75,75)
                tile.rect.x = x
                tile.rect.y = y
                tiles.append(tile)
        if ch == 'D':
                tile = Block(75,75)
                tile.rect.x = x
                tile.rect.y = y
                tiles.append(tile)

        if ch == 'B':
                tile = Block(75,75)
                tile.rect.x = x
                tile.rect.y = y
                tiles.append(tile)
        if ch == 'T':
                tile = Grass(75,75)
                tile.rect.x = x
                tile.rect.y = y
                tiles.append(tile)
        if ch != '\n':
            x += 75    
            if x >=75*53:
                x = 0
                y += 75
        


    return tiles       

pygame.init()
x_speed = 0
y_speed = 0

# Set the height and width of the screen
screen_width = 1000
screen_height = 1000
screen = pygame.display.set_mode([screen_width, screen_height])

block_list = pygame.sprite.Group()

all_sprites_list = pygame.sprite.Group()
tiles = draw('map.txt')
for tile in tiles:
    if tile.barrier:
        block_list.add(tile)
        
        
        
    all_sprites_list.add(tile)


player = Player()
player.rect.x = 100
player.rect.y = 100
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 

 
# -------- Main Program Loop -----------
while not done:
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
            
                
        # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0
    
    screen.fill(WHITE)
    x1 = player.rect.x
    y1 = player.rect.y
    player.rect.x += x_speed
    player.rect.y += y_speed
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, False)
    if len(blocks_hit_list) >0:
        
        player.rect.x = x1
        player.rect.y = y1
    if player.rect.x > 1000:
        player.rect.x = 0
        
        for s in all_sprites_list:
            s.rect.x -= 1000

    if player.rect.x < 0:
        player.rect.x = 1000
        
        for s in all_sprites_list:
            s.rect.x += 1000

    if player.rect.y > 1000:
        player.rect.y = 0
        
        for s in all_sprites_list:
            s.rect.x -= 1000

    if player.rect.y < 0 :
        player.rect.y = 1000
        
        for s in all_sprites_list:
            s.rect.y += 1000



    all_sprites_list.draw(screen)
    screen.blit(player.image,player.rect)
# Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
pygame.quit()
