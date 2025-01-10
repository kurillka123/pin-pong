import config
import pygame
import math
import random


class Ball(pygame.sprite.Sprite):
    width = 35
    height = 35
    speed = 3

    def __init__(self, scene) -> None:
        super().__init__()
        self.scene = scene
        self.velocity_x = 0
        self.velocity_y = 0
        self.angle = 60 # углы в градусах
        self.color = config.WHITE
        self.speed = Ball.speed

        screen_width, screen_height = self.scene.game.screen.get_size()
        min_side = min(screen_width, screen_height)
        width =  int(min_side * 0.03)
        height = int(min_side * 0.03)
        self.image = pygame.Surface((width, height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.goto_start()
        self.sounds = { 
            'collide': pygame.mixer.Sound(config.SOUNDS_DIR / 'collide.wav'),
            'win': pygame.mixer.Sound(config.SOUNDS_DIR / 'win.wav'),
            'loose': pygame.mixer.Sound(config.SOUNDS_DIR / 'loose.wav')
                      
        }
        self.scene.all_sprites.add(self)

    def goto_start(self):
        self.rect.centerx = self.scene.game.window_width // 2
        self.rect.centery = self.scene.game.window_height // 2
        self.angle = random.randint(45, 135) * random.choice((-1, 1))

    def move(self) -> None:
        self.velocity_x = math.cos(math.radians(self.angle - 90))
        self.velocity_y = math.sin(math.radians(self.angle - 90))
        self.rect.x += self.velocity_x * self.speed
        self.rect.y += self.velocity_y * self.speed

    def collide_barders(self) -> None:
        '''столкновение с экраном'''
        if self.rect.top > 0 and self.rect.bottom < self.scene.game.window_height:
            return
        
        self.angle *= -1
        self.angle += 180
        self.sounds['collide'].play()

    def collide_rackets(self):
        '''столкновение с ракетками'''
        if pygame.sprite.spritecollide(self, self.scene.all_rackets, False):
            self.angle *= -1
            self.sounds['collide'].play()

    def update(self) -> None:
        self.move()
        self.check_goal()
        self.collide_barders()
        self.collide_rackets()

    def check_goal(self) -> None:
        if self.rect.right >  self.scene.game.window_width:
            self.scene.score_left.value += 1
            self.goto_start()
            self.scene.racket_left.goto_start()
            self.scene.racket_right.goto_start()
            self.sounds['win'].play()
        elif self.rect.left < 0:
            self.scene.score_right.value += 1
            self.goto_start()
            self.scene.racket_left.goto_start()
            self.scene.racket_right.goto_start()
            self.sounds['win'].play()