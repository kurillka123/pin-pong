from abc import ABC, abstractmethod
import config
import pygame


class Racket(ABC, pygame.sprite.Sprite):
    @abstractmethod
    def __init__(
            self, 
            center_x: int,
            scene
    ):
        super().__init__()
        self.scene = scene
        self.center_x = center_x
        self.color = config.WHITE
        self.speed = 5
        screen_width, screen_height= self.scene.game.screen.get_size()
        min_side = min(screen_width, screen_height)
        Racket.width =  int(min_side * 0.05)
        Racket.height = int(min_side * 0.2)
        self.image = pygame.Surface((Racket.width, Racket.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        self.goto_start()
        self.scene.all_sprites.add(self)
        self.scene.all_rackets.add(self)

    def goto_start(self):
        self.rect.centerx = self.center_x
        self.rect.centery = self.scene.game.window_height // 2
    
    def move():
        pass

    def collide_borders(self):
        if self.rect.bottom > self.scene.game.window_height:
            self.rect.bottom = self.scene.game.window_height
        elif self.rect.top < 0:
            self.rect.top = 0

    def update(self):
        self.move()
        self.collide_borders()


class RacketAuto(Racket):
    def __init__(self, center_x, scene):
        super().__init__(center_x, scene)
        self.delay = 22
        self.last_move = pygame.time.get_ticks()

    def move(self):
        if pygame.time.get_ticks() - self.last_move >= self.delay:
            if self.scene.ball.rect.centery < self.rect.centery:
                self.rect.centery -= self.speed
            elif self.scene.ball.rect.centery > self.rect.centery:
                self.rect.centery += self.speed
            self.last_move = pygame.time.get_ticks()
    

class RacketManual(Racket):
    def __init__(self, center_x, key_up, key_down, scene):
        super().__init__(center_x, scene)
        self.key_up = key_up
        self.key_down = key_down

    def move(self):
        if not self.scene.keys_pressed:
            return
        
        if self.scene.keys_pressed[self.key_down]:
            self.rect.y += self.speed
        elif self.scene.keys_pressed[self.key_up]:
            self.rect.y -= self.speed