from entity.entity import Entity


class Phantom(Entity):
    def __init__(self, pos, img):
        self.image = img
        super(Phantom, self).__init__(self.image, pos)
