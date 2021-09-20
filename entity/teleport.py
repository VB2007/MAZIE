from entity.entity import Entity


class Teleport(Entity):
    def __init__(self, pos, img, tp_pos):
        self.tp_pos=tp_pos
        self.image = img
        super(Teleport, self).__init__(self.image, pos)
