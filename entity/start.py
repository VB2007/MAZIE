from entity.entity import Entity


class Start(Entity):
    def __init__(self, pos, img):
        self.image = img
        super(Start, self).__init__(self.image, pos)
