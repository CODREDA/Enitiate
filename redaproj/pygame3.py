import pygame
pygame.init()
# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
win = pygame.display.set_mode((700, 700))
pygame.display.set_caption("First Game")
x=350
y=550
width=64
height=64
vel=5

isJump = False
jumpCount= 10

left= False
right= False
walkCount=0

run= True
while run:
    pygame.time.delay(20)
    win.fill(BLACK)
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            run=False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x >= 0:
        x-=vel
    if keys[pygame.K_RIGHT] and x < 660:
        x+=vel
    if not(isJump):
        if keys[pygame.K_UP]:
            pass
        if keys[pygame.K_DOWN]:
            pass
        if keys[pygame.K_SPACE]:
            isJump = True
    
    else:
        if jumpCount>=-10:
            neg=1
            if jumpCount<0:   
                neg= -1
            y-=(jumpCount**2)*0.5*neg
            jumpCount-=1
            
        else:
            isJump=False
            jumpCount =10

    pygame.draw.rect(win,GREEN,(x, y, width, height))
    pygame.display.update()
pygame.quit()
