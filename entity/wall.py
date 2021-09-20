from entity.entity import Entity


class Wall(Entity):
    def __init__(self, pos, img):
        self.image = img
        super(Wall, self).__init__(self.image, pos)
