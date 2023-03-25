import pygame,math

class Coin:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(pygame.image.load("images/coin-sprite.png"),(20,20))
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 0.2
        self.direction = [1,1]

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def movement(self,max_width,max_height):
        if self.x < 0 or self.x+self.image_size[0]>max_width:
            self.direction[0]*=(-1)
        if self.y <0 or self.y+self.image_size[1]>max_height:
            self.direction[1]*=(-1)

        self.x +=self.delta*self.direction[0]
        self.y+=self.delta*self.direction[1]
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])


