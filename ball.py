import pygame
class Ball:
    Radius = 15
    def __init__ (self,x,y,vx,vy, screen, wcolor,bgcolor,width, height):
        self.x = x
        self.y = y
        self.screen = screen
        self.vx = vx
        self.vy = vy
        self.wcolor = wcolor
        self.bgcolor = bgcolor
        self.width = width
        self.height =height
        




    def show(self, color):
        pygame.draw.circle(self.screen, color, (self.x, self.y), self.Radius)

    def update(self):
        self.show(self.bgcolor)
        self.x = self.x + self.vx
        self.y =self.y + self.vy
        if self.x < 0:
            self.vx = abs(self.vx)
        if self.y<0:
            self.vy = abs(self.vy)
        if self.x>self.width:
            self.vx = -abs(self.vx)
        if self.y > self.height:
            self.vy = - abs(self.vy)
        self.show(self.wcolor)

   
    
   



    
    
