import pygame

from entity.finish import Finish
from entity.phantom import Phantom
from entity.start import Start
from entity.teleport import Teleport
from entity.wall import Wall
from system.map import Map
from math import sin, cos, pi, radians


class Game:
    def __init__(self, screen, game_name, difficult, imgs, x_offset, y_offset):
        self.alpha1 = 0
        self.alpha2 = 0
        self.start_time = 0
        self.run = True
        self.screen = screen
        pygame.display.set_caption(game_name)
        self.start = False
        self.finish = False
        self.ph = True

        self.imgs = imgs
        self.obj_list = pygame.sprite.Group()
        self.pl_grp = pygame.sprite.Group()
        self.pl = pygame.sprite.Sprite()

        x_offset = int(x_offset)
        y_offset = int(y_offset)
        self.difficult = difficult
        self.map = Map(difficult, x_offset, y_offset)
        self.pl = self.map.put_objects(self.obj_list, self.imgs)
        self.pl_grp.add(self.pl)

    def _render(self):
        self.screen.fill((255, 255, 255))
        self.obj_list.draw(self.screen)
        self.alpha1 += 5
        self.alpha2 -= 5
        alpha1 = self.alpha1
        alpha2 = self.alpha2
        a = 50
        x = self.pl.rect.centerx
        y = self.pl.rect.centery
        coord1 = [pi * (alpha1) / 180, pi * (alpha1 + 90) / 180]
        coord2 = [pi * (alpha2) / 180, pi * (alpha2 + 90) / 180]
        pygame.draw.polygon(self.screen, (255, 36, 0), (
            (x + a * sin(coord1[0]), y + a * cos(coord1[0])), (x + a * sin(coord1[1]), y + a * cos(coord1[1])),
            (x - a * sin(coord1[0]), y - a * cos(coord1[0])), (x - a * sin(coord1[1]), y - a * cos(coord1[1]))))
        pygame.draw.polygon(self.screen, (255, 36, 0), (
            (x + a * sin(coord2[0]), y + a * cos(coord2[0])), (x + a * sin(coord2[1]), y + a * cos(coord2[1])),
            (x - a * sin(coord2[0]), y - a * cos(coord2[0])), (x - a * sin(coord2[1]), y - a * cos(coord2[1]))))

        pygame.draw.polygon(self.screen, (0, 0, 0), (
            (x + a / 2 * sin(coord1[0]), y + a / 2 * cos(coord1[0])),
            (x + a / 2 * sin(coord1[1]), y + a / 2 * cos(coord1[1])),
            (x - a / 2 * sin(coord1[0]), y - a / 2 * cos(coord1[0])),
            (x - a / 2 * sin(coord1[1]), y - a / 2 * cos(coord1[1]))))
        pygame.draw.polygon(self.screen, (0, 0, 0), (
            (x + a / 2 * sin(coord2[0]), y + a / 2 * cos(coord2[0])),
            (x + a / 2 * sin(coord2[1]), y + a / 2 * cos(coord2[1])),
            (x - a / 2 * sin(coord2[0]), y - a / 2 * cos(coord2[0])),
            (x - a / 2 * sin(coord2[1]), y - a / 2 * cos(coord2[1]))))

        xx = 3 * self.pl.acceleration * cos(radians(self.pl.angle))
        yy = -3 * self.pl.acceleration * sin(radians(self.pl.angle))
        pygame.draw.line(self.screen, (255, 255, 255), (x, y), (x + xx, y + yy), 5)
        # pygame.draw.circle(self.screen, (150, 150, 150), (x, y), a + 1, 7)

        pygame.display.flip()

    def _check_collision(self):
        for collide_obj in self.obj_list:
            if pygame.sprite.collide_circle(self.pl, collide_obj):
                if isinstance(collide_obj, Wall):
                    self.pl.back_after_collide()
                if isinstance(collide_obj, Start):
                    self.start = True
                    self.finish = False
                if isinstance(collide_obj, Finish):
                    self.finish = True
                    if self.start:
                        self.run = False
                        # Results(self.screen, self.imgs, self.start_time, self.difficult).run()
                if isinstance(collide_obj, Teleport):
                    self.ph = False
                    self.pl.rect.center = collide_obj.tp_pos
                if isinstance(collide_obj, Phantom):
                    if self.ph:
                        self.pl.back_after_collide()

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.pl.forward = True
                # if event.key == pygame.K_DOWN:
                #     self.pl.forward = False
                if event.key == pygame.K_LEFT:
                    self.pl.turn_left = True
                if event.key == pygame.K_RIGHT:
                    self.pl.turn_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.pl.forward = False
                if event.key == pygame.K_LEFT:
                    self.pl.turn_left = False
                if event.key == pygame.K_RIGHT:
                    self.pl.turn_right = False

    def _update(self):
        self.pl.move(self.screen.get_width(), self.screen.get_height())
