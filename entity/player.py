from entity.entity import Entity
from math import sin, cos, radians


class Player(Entity):
    def __init__(self, pos, img):
        self.image = img
        super(Player, self).__init__(self.image, pos)
        self.forward = False
        self.turn_left = False
        self.turn_right = False
        self.angle = 0
        self.acceleration = 10
        self.radius=35

    def move(self, width, height):
        if self.forward:
            self.dx = self.acceleration * cos(radians(self.angle))
            self.dy = - self.acceleration * sin(radians(self.angle))
            Entity.update(self, width, height)
        if self.turn_left:
            self.angle = (self.angle + 10) % 360
        if self.turn_right:
            self.angle = (self.angle - 10) % 360
        Entity.rotate_sprite(self, self.image, self.angle)
