import pygame


class Entity(pygame.sprite.Sprite):
    def __init__(self, img, pos):
        super(Entity, self).__init__()
        self.img = img
        self.rect = self.img.get_rect()
        self.rect.center = pos
        self.dx = 0
        self.dy = 0
        self.radius = int(
            self.rect.width * .9 / 2)
        self.old_pos = (0, 0)

    def rotate_sprite(self, img, angle):
        old_rect_center = self.rect.center
        self.img = pygame.transform.rotate(img, angle)
        self.rect = self.img.get_rect()
        self.rect.center = old_rect_center

    def update(self, width, height):
        x = (self.rect.center[0] + self.dx) % width
        y = (self.rect.center[1] + self.dy) % height
        self.old_pos = self.rect.center
        self.rect.center = (x, y)

    def back_after_collide(self):
        self.rect.center = self.old_pos
