from paddle import Paddle
from ball import Ball
import pygame
import random
 
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    #logo = pygame.image.load("logo32x32.png")
    #pygame.display.set_icon(logo)
    pygame.display.set_caption("My pong")
     
    # create a surface on screen that has the size of 240 x 180
    WIDTH =800
    HEIGHT = 400
    BORDER = 20
    
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    #add a solid background as r,g,b:
    screen.fill((0,0,0))
    pygame.display.update() 
    #top wall
    wcolor = pygame.Color("white")
    bgcolor  = pygame.Color("black")
    bounds=pygame.draw.rect(screen, wcolor, pygame.Rect((0,0), (WIDTH,BORDER)))
    
    #left wall
    bounds1=pygame.draw.rect(screen, wcolor, pygame.Rect((0,0), (BORDER, HEIGHT)))
    #bottom wall
    bounds2=pygame.draw.rect(screen, wcolor, pygame.Rect((0,HEIGHT-BORDER), (WIDTH,BORDER)))
    
    x0 = random.randint(0,WIDTH)
    y0 = random.randint(0,HEIGHT)
    
    vx0 = 5

    vy0 = 5
    FPS =30
    

    ball1 = Ball(x0,y0,vx0,vy0,screen,wcolor, bgcolor,WIDTH, HEIGHT)
    ball1.show(wcolor)
    
    
    pygame.display.update()
    # define a variable to control the main loop
    running = True
    clock = pygame.time.Clock()
     
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
        pygame.display.update()
        clock.tick(FPS)
        ball1.update()
        
        

           
            
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
