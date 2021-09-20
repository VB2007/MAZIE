import pygame


class ImageLoader:
    @staticmethod
    def load_and_convert(frame, scale=(100, 100), angle=0):
        img = pygame.image.load(frame)
        img = pygame.transform.scale(img, scale)
        img = pygame.transform.rotate(img, angle)
        return img

    @staticmethod
    def draw_and_convert(color, scale, angle):
        img = pygame.Surface(scale)
        img = pygame.transform.rotate(img, angle)
        img.fill(color)
        img.set_colorkey(color)
        return img
