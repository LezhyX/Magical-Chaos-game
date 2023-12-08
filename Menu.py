import pygame
import sys
from Button import MenuButton

pygame.init()
width, height = 1280, 720
max_fps = 30

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Magical Chaos")
menu_background = pygame.image.load('menu_background_720.jpg')
clock = pygame.time.Clock()
monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
fullscreen_mode = False


def main_menu():
    choose_level = MenuButton(width / 2 - 200, height / 5, 400, height / 10, 'Выбрать уровень', 'red_button.png',
                              'red_button_hover.png', 'click.ogg')
    gear = MenuButton(width / 2 - 200, height / 3, width / 3.2, 50, 'Снаряжение', 'yellow_button.png',
                      'yellow_button_hover.png', 'click.ogg')
    introduction = MenuButton(width / 2 - 200, height / 3 + 80, width / 3.2, height / 14.4,
                              'Справка', 'yellow_button.png', 'yellow_button_hover.png', 'click.ogg')
    settings = MenuButton(width / 2 - 200, height / 3 + 160, width / 3.2, height / 14.4,
                          'Настройки', 'yellow_button.png', 'yellow_button_hover.png', 'click.ogg')
    log_out = MenuButton(width / 2 - 200, height / 3 + 240, width / 3.2, height / 14.4, 'Выйти',
                         'yellow_button.png', 'yellow_button_hover.png', 'click.ogg')
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(menu_background, (0, 0))

        font = pygame.font.Font('Silver.ttf', 150)
        text_surface = font.render("Magical Chaos", True, (106, 90, 205))
        text_rect = text_surface.get_rect(center=(width / 2, height / 7.2))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    logout_confirmation()

            if event.type == pygame.USEREVENT and event.button == choose_level:
                fade()
                level_selection()

            if event.type == pygame.USEREVENT and event.button == settings:
                fade()
                settings_menu()

            if event.type == pygame.USEREVENT and event.button == gear:
                fade()
                gear_menu()

            if event.type == pygame.USEREVENT and event.button == introduction:
                fade()
                introduction_menu()

            if event.type == pygame.USEREVENT and event.button == log_out:
                logout_confirmation()

            for button in [choose_level, gear, introduction, settings, log_out]:
                button.check_click(event)

        for button in [choose_level, gear, introduction, settings, log_out]:
            button.set_pos(width / 2 - 200)
            button.check_hover(pygame.mouse.get_pos())
            button.show(screen)
        pygame.display.flip()


def level_selection():
    tutorial = MenuButton(width / 2 - 200, height / 5, 400, height / 15, 'В пещерах...', 'yellow_button.png',
                          'yellow_button_hover.png', 'click.ogg')
    level_one = MenuButton(width / 2 - 200, height / 5 + 72, 400, height / 15, 'В небе...', 'yellow_button.png',
                           'yellow_button_hover.png', 'click.ogg')
    level_two = MenuButton(width / 2 - 200, height / 5 + 144, 400, height / 15, 'Coming Soon...', 'yellow_button.png',
                           'yellow_button_hover.png', 'click.ogg')
    back = MenuButton(width / 2 - 200, height / 5 + 216, 400, height / 15, 'Назад', 'red_button.png',
                      'red_button_hover.png', 'click.ogg')

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(menu_background, (0, 0))

        font = pygame.font.Font('Silver.ttf', 150)
        text_surface = font.render("Выбор уровня", True, (106, 90, 205))
        text_rect = text_surface.get_rect(center=(width / 2, height / 7.2))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            if event.type == pygame.USEREVENT and event.button == tutorial:
                tutorial_selection()
                fade()

            if event.type == pygame.USEREVENT and event.button == level_one:
                fade()
                level_one_selection()

            if event.type == pygame.USEREVENT and event.button == back:
                fade()
                running = False

            for button in [tutorial, level_one, level_two, back]:
                button.check_click(event)

        for button in [tutorial, level_one, level_two, back]:
            button.set_pos(width / 2 - 200)
            button.check_hover(pygame.mouse.get_pos())
            button.show(screen)
        pygame.display.flip()


def tutorial_selection():
    start = MenuButton(width / 8, height / 1.5, 300, height / 15, 'Начать', 'yellow_button.png',
                       'yellow_button_hover.png', 'click.ogg')
    back = MenuButton(width * 7 / 8 - 300, height / 1.5, 300, height / 15, 'Назад', 'red_button.png',
                      'red_button_hover.png', 'click.ogg')

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(menu_background, (0, 0))

        font = pygame.font.Font('Silver.ttf', 50)
        text_surface = font.render("Первый и одновременно обучающий уровень,", True, (255, 0, 0))
        text_surface1 = font.render('создан для освоения игры', True, (255, 0, 0))
        text_rect = text_surface.get_rect(center=(width / 2, 300))
        text_rect1 = text_surface1.get_rect(center=(width / 2, 350))
        screen.blit(text_surface, text_rect)
        screen.blit(text_surface1, text_rect1)

        font = pygame.font.Font('Silver.ttf', 150)
        text_surface = font.render("Пещеры: обучение", True, (106, 90, 205))
        text_rect = text_surface.get_rect(center=(width / 2, height / 7.2))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            if event.type == pygame.USEREVENT and event.button == back:
                fade()
                running = False

            for button in [start, back]:
                button.check_click(event)

        for button in [start, back]:
            button.check_hover(pygame.mouse.get_pos())
            button.show(screen)
        pygame.display.flip()


def level_one_selection():
    back = MenuButton(width / 2 - 200, height / 2, 400, height / 10, 'Ok', 'red_button.png',
                      'red_button_hover.png', 'click.ogg')
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(menu_background, (0, 0))

        font = pygame.font.Font('Silver.ttf', 100)
        text_surface = font.render("WIP", True, (106, 90, 205))
        text_rect = text_surface.get_rect(center=(width / 2, 300))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    fade()
                    running = False

            if event.type == pygame.USEREVENT and event.button == back:
                fade()
                running = False

            for button in [back]:
                button.check_click(event)

        for button in [back]:
            button.check_hover(pygame.mouse.get_pos())
            button.show(screen)

        pygame.display.flip()


def settings_menu():
    global screen
    video = MenuButton(width / 2 - 200, height / 5, 400, height / 15, 'Видео', 'yellow_button.png',
                       'yellow_button_hover.png', 'click.ogg')
    audio = MenuButton(width / 2 - 200, height / 5 + 72, 400, height / 15, 'Аудио', 'yellow_button.png',
                       'yellow_button_hover.png', 'click.ogg')
    back = MenuButton(width / 2 - 200, height / 5 + 144, 400, height / 15, 'Назад', 'red_button.png',
                      'red_button_hover.png', 'click.ogg')
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(menu_background, (0, 0))

        font = pygame.font.Font('Silver.ttf', 100)
        text_surface = font.render("Настройки", True, (106, 90, 205))
        text_rect = text_surface.get_rect(center=(width / 2, 100))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    fade()
                    running = False

            if event.type == pygame.USEREVENT and event.button == video:
                fade()
                video_settings()

            if event.type == pygame.USEREVENT and event.button == audio:
                fade()
                change_volume()

            if event.type == pygame.USEREVENT and event.button == back:
                fade()
                running = False

            for button in [video, audio, back]:
                button.check_click(event)

        for button in [video, audio, back]:
            button.set_pos(width / 2 - 200)
            button.check_hover(pygame.mouse.get_pos())
            button.show(screen)
        pygame.display.flip()


def gear_menu():
    back = MenuButton(width / 2 - 200, height / 2, 400, height / 10, 'Ok', 'red_button.png',
                      'red_button_hover.png', 'click.ogg')
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(menu_background, (0, 0))

        font = pygame.font.Font('Silver.ttf', 100)
        text_surface = font.render("WIP", True, (106, 90, 205))
        text_rect = text_surface.get_rect(center=(width / 2, 300))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    fade()
                    running = False

            if event.type == pygame.USEREVENT and event.button == back:
                fade()
                running = False

            for button in [back]:
                button.check_click(event)

        for button in [back]:
            button.check_hover(pygame.mouse.get_pos())
            button.show(screen)

        pygame.display.flip()


def introduction_menu():
    back = MenuButton(width / 2 - 200, height / 2, 400, height / 10, 'Ok', 'red_button.png',
                      'red_button_hover.png', 'click.ogg')
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(menu_background, (0, 0))

        font = pygame.font.Font('Silver.ttf', 100)
        text_surface = font.render("WIP", True, (106, 90, 205))
        text_rect = text_surface.get_rect(center=(width / 2, 300))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    fade()
                    running = False

            if event.type == pygame.USEREVENT and event.button == back:
                fade()
                running = False

            for button in [back]:
                button.check_click(event)

        for button in [back]:
            button.check_hover(pygame.mouse.get_pos())
            button.show(screen)

        pygame.display.flip()


def logout_confirmation():
    logout = MenuButton((width / 3) - (width / 6.4), height / 1.8, width / 3.2, height / 9.6, 'Да', 'red_button.png',
                        'red_button_hover.png', 'click.ogg')
    back = MenuButton(width * 2 / 3 - (width / 6.4), height / 1.8, width / 3.2, height / 9.6, 'Нет',
                      'yellow_button.png',
                      'yellow_button_hover.png', 'click.ogg')

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(menu_background, (0, 0))

        font = pygame.font.Font('Silver.ttf', 100)
        text_surface = font.render("Выйти из игры?", True, (106, 90, 205))
        text_rect = text_surface.get_rect(center=(width / 2, 200))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            if event.type == pygame.USEREVENT and event.button == back:
                running = False

            if event.type == pygame.USEREVENT and event.button == logout:
                running = False
                pygame.quit()
                sys.exit()

            for button in [logout, back]:
                button.check_click(event)

        for button in [logout, back]:
            button.check_hover(pygame.mouse.get_pos())
            button.show(screen)

        pygame.display.flip()


def video_settings():
    sd = MenuButton(width / 2 - 200, height / 4, 400, height / 15, '960x544', 'yellow_button.png',
                    'yellow_button_hover.png', 'click.ogg')
    hd = MenuButton(width / 2 - 200, height / 4 + 72, 400, height / 15, '1280x720', 'yellow_button.png',
                    'yellow_button_hover.png', 'click.ogg')
    fullhd = MenuButton(width / 2 - 200, height / 4 + 144, 400, height / 15, '1920x1080', 'yellow_button.png',
                        'yellow_button_hover.png', 'click.ogg')
    fullscreen = MenuButton(width / 2 - 200, height / 4 + 216, 400, height / 15, 'Полный экран', 'yellow_button.png',
                            'yellow_button_hover.png', 'click.ogg')
    back = MenuButton(width / 2 - 200, height / 4 + 288, 400, height / 15, 'Назад', 'red_button.png',
                      'red_button_hover.png', 'click.ogg')

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(menu_background, (0, 0))

        font = pygame.font.Font('Silver.ttf', 100)
        text_surface = font.render("Выбор разрешения", True, (106, 90, 205))
        text_rect = text_surface.get_rect(center=(width / 2, 100))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    fade()
                    running = False

            if event.type == pygame.USEREVENT and event.button == back:
                fade()
                running = False

            if event.type == pygame.USEREVENT and event.button == sd:
                change_resolution(960, 544)
                running = False

            if event.type == pygame.USEREVENT and event.button == hd:
                change_resolution(1280, 720)
                running = False

            if event.type == pygame.USEREVENT and event.button == fullhd:
                change_resolution(1920, 1080)
                running = False

            if event.type == pygame.USEREVENT and event.button == fullscreen:
                switch_fullscreen()
                running = False

            for button in [sd, hd, fullhd, fullscreen, back]:
                button.check_click(event)

        for button in [sd, hd, fullhd, fullscreen, back]:
            button.check_hover(pygame.mouse.get_pos())
            button.show(screen)
        pygame.display.flip()


def change_volume():
    back = MenuButton(width / 2 - 200, height / 2, 400, height / 10, 'Ok', 'red_button.png',
                      'red_button_hover.png', 'click.ogg')
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(menu_background, (0, 0))

        font = pygame.font.Font('Silver.ttf', 100)
        text_surface = font.render("WIP", True, (106, 90, 205))
        text_rect = text_surface.get_rect(center=(width / 2, 300))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    fade()
                    running = False

            if event.type == pygame.USEREVENT and event.button == back:
                fade()
                running = False

            for button in [back]:
                button.check_click(event)

        for button in [back]:
            button.check_hover(pygame.mouse.get_pos())
            button.show(screen)

        pygame.display.flip()


def change_resolution(w, h):
    global width, height, screen, menu_background
    width, height = w, h
    screen = pygame.display.set_mode((w, h))
    menu_background = pygame.image.load(f'menu_background_{h}.jpg')
    fade()


def switch_fullscreen():
    global width, height, screen, menu_background
    width, height = monitor_size
    screen = pygame.display.set_mode(monitor_size, pygame.FULLSCREEN)
    menu_background = pygame.image.load('menu_background_1080.jpg')


def fade():
    running = True
    fade_alpha = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        fade_surface = pygame.Surface((width, height))
        fade_surface.fill((0, 0, 0))
        fade_surface.set_alpha(fade_alpha)
        screen.blit(fade_surface, (0, 0))

        fade_alpha += 5
        if fade_alpha >= 75:
            fade_alpha = 255
            running = False

        pygame.display.flip()
        clock.tick(max_fps)


if __name__ == '__main__':
    main_menu()
