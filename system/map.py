from entity.finish import Finish
from entity.phantom import Phantom
from entity.player import Player
from entity.start import Start
from entity.teleport import Teleport
from entity.wall import Wall


class Map:
    def __init__(self, difficulty: int, offset_x, offset_y):
        self.map = list()

        self.offset_x = offset_x
        self.offset_y = offset_y
        file_path = None
        if difficulty == 1:
            self.file_path = 'maps/diff1.txt'
        elif difficulty == 2:
            self.file_path = 'maps/diff2.txt'
        elif difficulty == 3:
            self.file_path = 'maps/diff3.txt'
        elif difficulty == 4:
            self.file_path = 'maps/diff4.txt'
        self.difficulty=difficulty

        with open(self.file_path, 'r') as file_path:
            for i in file_path.readlines():
                self.map.append(i.strip('\n').split())

    def put_objects(self, obj_list, imgs) -> Player:
        y: int = 0
        for line in self.map:
            x: int = 0
            for char in line:
                pos_x = x * self.offset_x + 35
                pos_y = y * self.offset_y + 35
                pos_center = (pos_x, pos_y)
                if char == '1':
                    obj_list.add(Wall(pos_center, imgs[1]))
                elif char == 'p':
                    ret = Player(pos_center, imgs[0])
                elif char == 's':
                    obj_list.add(Start(pos_center, imgs[2]))
                elif char == 'f':
                    obj_list.add(Finish(pos_center, imgs[3]))
                elif char == '_':
                    obj_list.add(Phantom(pos_center, imgs[1]))
                elif char == 't3.1':
                    obj_list.add(Teleport(pos_center, imgs[4], (750, 50)))
                elif char == 't4.1':
                    obj_list.add(Teleport(pos_center, imgs[2], (435, 835)))
                elif char == 't4.2':
                    obj_list.add(Teleport(pos_center, imgs[4], (250, 550)))
                x += 1
            y += 1
        return ret
