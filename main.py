import pygame
'''
мяч
ракетка
'''
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Racket:
    def __init__(self, x: int, y: int, game):
        '''
        полнозкранный режим
        как узнать размер полного экрана
        помещать ракетки посередине вертикали
        рассчитать размеры и координаты ракеток относительно экрана
        '''
        self.x = x
        self.y = y
        self.width = 10
        self.haight = 100
        self.color = WHITE
        self.speed = 5
        self.rect = pygame.Rect(self.x, self.y, self.width, self.haight)
        self.game = game

    def move(self, x: int, y: int):
        '''двигает ракетку'''
        self.rect.move_ip(x, y)

    def render(self):
        '''рисует ракетку'''
        pygame.draw.rect(self.game.screen, self.color,self.rect, 0)




class Game:
    def __init__(self, width: int, height: int) -> None:
        pygame.init()
        display_info = pygame.display.Info()
        self.window_width = display_info.current_w
        self.window_height = display_info.current_h
        self.screen = pygame.display.set_mode(
            (self.window_width, self.window_height)
        )
        self.racket_left = Racket(50, 250, self)
        self.racket_right = Racket(450, 250, self)
        self.is_running = True
        self.main_loop()

    def main_loop(self) -> None:
        while self.is_running:
            '''
            сбор событий
            изменения (обьектов)
            рендер (отрисовка)
            ожидание FPS
            '''
            self.handle_events()
            self.update()
            self.render()
        pygame.quit()

    def handle_events(self) -> None:
        '''обрабатывает события'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.racket_right.move(0, -10)
                elif event.key == pygame.K_DOWN:
                    self.racket_right.move(0, 10)
                elif event.key == pygame.K_w:
                    self.racket_left.move(0, -10)
                elif event.key == pygame.K_s:
                    self.racket_left.move(0, 10)
                elif event.key == pygame.K_ESCAPE:
                    self.is_running = False
                    
    def update(self) -> None:
        pass

    def render(self):
        '''отрисовывает обьекты на екране'''
        self.screen.fill(BLACK)
        self.racket_left.render()
        self.racket_right.render()
        pygame.display.flip()


Game(0, 0)