import pygame
pygame.init()
# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
# Set the height and width of the screen
size = [400, 300]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("First Game")
x=350
y=500
width=40
height=60
vel=5
run= True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            run=False
# Clear the screen and set the screen background
    screen.fill(WHITE)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x-=vel
    if keys[pygame.K_RIGHT]:
        x+=vel
    if keys[pygame.K_UP]:
        pass
    if keys[pygame.K_DOWN]:
        pass
# Draw a rectangle outline
    pygame.draw.rect(screen, BLACK, [75, 10, 50, 20],2)
    pygame.display.update()
    
pygame.quit()
