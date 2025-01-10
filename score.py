import pygame
import config

class Score(pygame.sprite.Sprite):
    '''табло для показа счета игрока'''
    def __init__(self, center_x: int, center_y: int, scene):
        super().__init__()
        self.scene = scene
        self.center_x = center_x
        self.center_y = center_y
        self.value = 0
        self.color = config.WHITE
        self.size = 1
        screen_width, screen_height= self.scene.game.screen.get_size()
        min_side = min(screen_width, screen_height)
        self.size = int(min_side * 0.03)
        self.font = pygame.font.Font(
            config.FONTS_DIR / 'PressStart2P-Regular.ttf', self.size
        )
        
        self.image = self.font.render(str(self.value), True, self.color)
        self.rect = self.image.get_rect()
        self.rect.centerx = center_x
        self.rect.centery = center_y
        self.scene.all_sprites.add(self)

    def update(self):
        self.image = self.font.render(str(self.value), True, self.color)
        self.rect = self.image.get_rect()
        self.rect.centerx = self.center_x
        self.rect.centery = self.center_y