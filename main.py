import pygame

from system.game import Game
from system.image_loader import ImageLoader
from system.score_board import score_list

diff = int(input('Set difficulty level: '))
WIDTH = 1000
HEIGHT = 1000
FPS = 30
X_OFFSET = 100
Y_OFFSET = 100

clock = pygame.time.Clock()

img_loader = ImageLoader()
imgs = [img_loader.load_and_convert('imgs/player.png'), img_loader.load_and_convert('imgs/wall.png'),
        img_loader.load_and_convert('imgs/start.png'), img_loader.load_and_convert('imgs/finish.jpeg'),
        img_loader.load_and_convert('imgs/tp.png')]

mazie = Game(pygame.display.set_mode((WIDTH, HEIGHT)), 'MAZIE', diff, imgs, X_OFFSET, Y_OFFSET)
s = 0
while mazie.run:
    if mazie.start:
        s += 1
        pygame.display.set_caption('MAZIE   sec:' + str(s // 30))
    clock.tick(FPS)
    mazie._handle_events()
    mazie._check_collision()
    mazie._update()
    mazie._render()

score_list(diff, s)

for i in range(2):
    clock.tick(1)
pygame.quit()
