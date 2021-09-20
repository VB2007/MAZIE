from entity.entity import Entity


class Finish(Entity):
    def __init__(self, pos, img):
        self.image = img
        super(Finish, self).__init__(self.image, pos)
