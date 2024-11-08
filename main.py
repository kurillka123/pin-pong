import pygame

RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class BALL:
    width = 20
    height = 20

    def __init__(self, x:int, y:int, game):
        self.x = x 
        self.y = y
        self.color = WHITE
        self.speed = 5
        self.rect = pygame.Rect(self.x, self.y, BALL.width, BALL.height)
        self.game = game
        
    def move(self):
        self.x += 1
        self.y += 0
        # TODO изменить координаты у self.rect

    def render(self):
        pygame.draw.rect(self.game.screen, self.color, self.rect, 0)

    def update(self):
        self.move()


class Racket:
    width = 40
    height = 250
    def __init__(self, x: int, y: int, game):
        self.x = x 
        self.y = y
        self.color = WHITE
        self.speed = 5
        self.rect = pygame.Rect(self.x, self.y, Racket.width,  Racket.height)
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
        display_info = pygame.display.Info() # экземпляр класса Info
        self.window_width = display_info.current_w # атрибуты Info (ширина)
        self.window_height = display_info.current_h # атрибуты Info (высота)
        self.screen = pygame.display.set_mode(
            (self.window_width, self.window_height)
        )
        
        # левая ракетка
        self.racket_left = Racket(
            self.window_width // 10, 
            self.window_height // 2 - Racket.height // 2, 
            self
            )
        
        # правая ракетка
        self.racket_right = Racket(
            self.window_width // 10 * 9 - Racket.width,
            self.window_height // 2 - Racket.height // 2,
            self
            )
        
        # мяч
        x_ball = self.window_width // 2 - BALL.width // 2
        y_ball = self.window_height // 2 - BALL.height // 2
        self.ball = BALL(
            x_ball,
            y_ball, 
            self
            )
        
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
            self.handle_events() # вызов функции handle_events
            self.update() # вызов функции update
            self.render() # вызов функции render
        pygame.quit()

    def handle_events(self) -> None:
        '''обрабатывает события'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                self.is_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.racket_right.move(0, -30)
                elif event.key == pygame.K_DOWN:
                    self.racket_right.move(0, 30)
                elif event.key == pygame.K_w:
                    self.racket_left.move(0, -30)
                elif event.key == pygame.K_s:
                    self.racket_left.move(0, 30)
                elif event.key == pygame.K_ESCAPE:
                    self.is_running = False
                    
    def update(self) -> None:
        pass

    def render(self):
        '''отрисовывает обьекты на екране'''

        self.ball.update()

        self.screen.fill(BLACK)
        self.racket_left.render()
        self.racket_right.render()
        self.ball.render()
        pygame.display.flip()


Game(0, 0)