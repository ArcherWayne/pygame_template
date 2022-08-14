import pygame, sys, time
from setting import *
from debug import debug


class MAINGAME:
    def __init__(self):
        ## pygame setup

        pygame.init()
        self.screen = pygame.display.set_mode(window_size)
        # pygame.display.set_caption('window_name')
        # pygame.display.set_icon(pygame.image.load('assets/blade game.png'))
        # background_surface = pygame.transform.scale(
        #     pygame.image.load('assets/background/ground.png').convert(), (setting.WIN_WIDTH, setting.WIN_HEIGTH))
        # background_rect = background_surface.get_rect(center=(setting.WIN_WIDTH / 2, setting.WIN_HEIGTH / 2))
        # clock = pygame.time.Clock()
        # font = pygame.font.Font('assets/font/Pixeltype.ttf', 50)

# group setup ----------------------------------------------------------------------------------------------- #
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

# class setup
        # class = Class()

# attribute setup
        self.last_time = time.time()
        self.game_active = True


    def game_loop(self):
        # delta time    ------------------------------------------------------------------------------------- #
        dt = time.time() - last_time
        last_time = time.time()

        # event loop    ------------------------------------------------------------------------------------- #
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE):
                pygame.quit()
                sys.exit()

        if self.game_active:
            self.screen.fill(WHITE)
            # screen.blit(background_surface, background_rect)
            self.all_sprites.update()
            self.all_sprites.draw(self.screen)


        pygame.display.update()

    def update(self):
        pass

if __name__ == "__main__":
    main_game = MAINGAME()
    main_game.game_loop()

