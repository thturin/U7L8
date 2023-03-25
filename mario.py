import pygame

class Mario:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(pygame.image.load("images/mario_sprite.png"), (60, 90))
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        # need a delta
        self.delta = 0.5

    def move_direction(self, direction):
        if direction == 'right':
            self.x = self.x + self.delta
        elif direction == 'left':
            self.x -= self.delta
        elif direction == 'down':
            self.y += self.delta
        elif direction == 'up':
            self.y -= self.delta

        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

# class Mario:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.image = pygame.transform.scale(pygame.image.load("images/mario_sprite.png"),(75,100))  # TOO BIG!!!!!! need to resize
#         self.image_size = self.image.get_size()
#         self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
#         # need a delta
#         self.delta = .1
#
# # add move method in demo
#
#     def move_direction(self, direction):
#         if direction == "right":
#             self.x = self.x + self.delta
#         self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
