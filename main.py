import config  # импорт файла config
import pygame  # импорт модуля pygame
from scene import GameplayScene, MenuScene

class  Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.mixer.init()
        display_info = pygame.display.Info()  # экземпляр класса Info
        self.window_width = display_info.current_w  # атрибуты Info (ширина)
        self.window_height = display_info.current_h  # атрибуты Info (высота)
        self.screen = pygame.display.set_mode(
            (self.window_width, self.window_height)
        )
        self.scene = GameplayScene(self)
        self.is_running = True  
        self.keys_pressed = None
        print(self.keys_pressed)
        self.clock = pygame.time.Clock()  
          
    def main_loop(self) -> None:
        while self.is_running:
            '''
            сбор событий
            изменения (обьектов)
            рендер (отрисовка)
            ожидание FPS
            '''
            self.scene.handle_events()  # вызов функции handle_events
            self.scene.update()  # вызов функции update
            self.scene.render()  # вызов функции render
            self.clock.tick(config.FPS)
        pygame.quit()
                    
    def update(self) -> None:
        self.scene.all_sprites.update()


if __name__ == '__main__':
    game = Game()  # создание экземпляра класса
    game.main_loop()