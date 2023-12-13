import pygame
import sys
from Button import MenuButton
from Tutorial import start_tutorial

pygame.init()
pygame.mixer.init()
width, height, max_fps = 1280, 720, 30

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Magical Chaos")
menu_background = pygame.image.load('assets/menu_background_720.jpg')
clock = pygame.time.Clock()
monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
fullscreen_mode = False
current_volume = 0.2
pygame.mixer.music.load('assets/menu_music.mp3')
pygame.mixer.music.set_volume(current_volume)
pygame.mixer.music.play(-1)


def main_menu():
    choose_level = MenuButton(width / 2 - 200, height / 5, 400, height / 10, 'Выбрать уровень', 'assets/red_button.png',
                              'assets/red_button_hover.png', 'assets/click.ogg')
    gear = MenuButton(width / 2 - 200, height / 3, width / 3.2, 50, 'Снаряжение', 'assets/yellow_button.png',
                      'assets/yellow_button_hover.png', 'assets/click.ogg')
    introduction = MenuButton(width / 2 - 200, height / 3 + 80, width / 3.2, height / 14.4,
                              'Справка', 'assets/yellow_button.png', 'assets/yellow_button_hover.png',
                              'assets/click.ogg')
    settings = MenuButton(width / 2 - 200, height / 3 + 160, width / 3.2, height / 14.4,
                          'Настройки', 'assets/yellow_button.png', 'assets/yellow_button_hover.png', 'assets/click.ogg')
    log_out = MenuButton(width / 2 - 200, height / 3 + 240, width / 3.2, height / 14.4, 'Выйти',
                         'assets/yellow_button.png', 'assets/yellow_button_hover.png', 'assets/click.ogg')
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(menu_background, (0, 0))

        font = pygame.font.Font('assets/Silver.ttf', 150)
        text_surface = font.render("Magical Chaos", True, (255, 90, 205))
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
    tutorial = MenuButton(width / 2 - 200, height / 5, 400, height / 15, 'В пещерах...', 'assets/yellow_button.png',
                          'assets/yellow_button_hover.png', 'assets/click.ogg')
    level_one = MenuButton(width / 2 - 200, height / 5 + 72, 400, height / 15, 'Coming Soon...',
                           'assets/yellow_button.png',
                           'assets/yellow_button_hover.png', 'assets/click.ogg')
    back = MenuButton(width / 2 - 200, height / 5 + 216, 400, height / 15, 'Назад', 'assets/red_button.png',
                      'assets/red_button_hover.png', 'assets/click.ogg')

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(menu_background, (0, 0))

        font = pygame.font.Font('assets/Silver.ttf', 150)
        text_surface = font.render("Выбор уровня", True, (255, 90, 205))
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
                pass

            if event.type == pygame.USEREVENT and event.button == back:
                fade()
                running = False

            for button in [tutorial, level_one, back]:
                button.check_click(event)

        for button in [tutorial, level_one, back]:
            button.set_pos(width / 2 - 200)
            button.check_hover(pygame.mouse.get_pos())
            button.show(screen)
        pygame.display.flip()


def tutorial_selection():
    with open('assets/info.txt', 'r') as file:
        data = file.read().split(',')
        weapon_selected = int(data[2])
    start = MenuButton(width / 8, height / 1.5, 300, height / 15, 'Начать', 'assets/yellow_button.png',
                       'assets/yellow_button_hover.png', 'assets/click.ogg')
    back = MenuButton(width * 7 / 8 - 300, height / 1.5, 300, height / 15, 'Назад', 'assets/red_button.png',
                      'assets/red_button_hover.png', 'assets/click.ogg')

    running = True
    while running:
        with open('assets/info.txt', 'r') as file:
            data = file.read().split(',')
            score = int(data[0])
        screen.fill((0, 0, 0))
        screen.blit(menu_background, (0, 0))

        font = pygame.font.Font('assets/Silver.ttf', 50)
        text_surface = font.render("Первый уровень", True, (255, 0, 0))
        text_surface1 = font.render(f'Максимум очков: {score}', True, (255, 0, 0))
        text_rect = text_surface.get_rect(center=(width / 2, 300))
        text_rect1 = text_surface1.get_rect(center=(width / 2, 350))
        screen.blit(text_surface, text_rect)
        screen.blit(text_surface1, text_rect1)

        font = pygame.font.Font('assets/Silver.ttf', 150)
        text_surface = font.render("Уровень 1: Пещеры", True, (255, 90, 205))
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

            if event.type == pygame.USEREVENT and event.button == start:
                fade()
                pygame.mixer.music.stop()
                start_tutorial(width, height, screen, weapon_selected, current_volume)
                pygame.mixer.music.play(-1)

            for button in [start, back]:
                button.check_click(event)

        for button in [start, back]:
            button.check_hover(pygame.mouse.get_pos())
            button.show(screen)
        pygame.display.flip()


def settings_menu():
    global screen
    video = MenuButton(width / 2 - 200, height / 5, 400, height / 15, 'Видео', 'assets/yellow_button.png',
                       'assets/yellow_button_hover.png', 'assets/click.ogg')
    audio = MenuButton(width / 2 - 200, height / 5 + 72, 400, height / 15, 'Аудио', 'assets/yellow_button.png',
                       'assets/yellow_button_hover.png', 'assets/click.ogg')
    back = MenuButton(width / 2 - 200, height / 5 + 144, 400, height / 15, 'Назад', 'assets/red_button.png',
                      'assets/red_button_hover.png', 'assets/click.ogg')
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(menu_background, (0, 0))

        font = pygame.font.Font('assets/Silver.ttf', 100)
        text_surface = font.render("Настройки", True, (255, 90, 205))
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
    default = pygame.transform.scale(pygame.image.load('assets/default_weapon.png').convert_alpha(),
                                     (width / 8, width / 8))
    shotgun = pygame.transform.scale(pygame.image.load('assets/shotgun.png').convert_alpha(), (width / 8, width / 8))
    with open('assets/info.txt', 'r') as file:
        data = file.read().split(',')
        weapon_selected = int(data[2])
        score = int(data[0])
    if weapon_selected == 0:
        text_1 = 'Выбрано'
        if score < 50000:
            text_2 = 'Набрать 50000 очков в пещерах'
        else:
            text_2 = 'Выбрать'
    elif weapon_selected == 1:
        text_1 = 'Выбрать'
        text_2 = 'Выбрано'
    select_1 = MenuButton((width / 3) - (width / 5), height / 1.5, width / 5, height / 12, f'{text_1}',
                          'assets/yellow_button.png',
                          'assets/yellow_button_hover.png', 'assets/click.ogg')
    select_2 = MenuButton(width * (2 / 3), height / 1.5, width / 5, height / 12, f'{text_2}',
                          'assets/yellow_button.png', 'assets/yellow_button_hover.png', 'assets/click.ogg')
    back = MenuButton(width * 0.01, (height * 0.98) - (height / 14), width / 6, height / 14, 'Назад',
                      'assets/red_button.png', 'assets/red_button_hover.png', 'assets/click.ogg')
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(menu_background, (0, 0))

        font = pygame.font.Font('assets/Silver.ttf', 100)
        text_surface = font.render("Снаряжение", True, (255, 90, 205))
        text_rect = text_surface.get_rect(center=(width / 2, height / 7.2))
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

            if event.type == pygame.USEREVENT and event.button == select_1:
                if weapon_selected == 0:
                    pass
                else:
                    with open('assets/info.txt', 'r') as file:
                        data = file.read().split(',')
                        score = int(data[0])
                        gold = int(data[1])
                        weapon_to_rewrite = 0
                        with open('assets/info.txt', 'w') as file:
                            file.write(f"{score},{gold},{weapon_to_rewrite}")
                    fade()
                    running = False

            if event.type == pygame.USEREVENT and event.button == select_2:
                if weapon_selected == 1:
                    pass
                with open('assets/info.txt', 'r') as file:
                    data = file.read().split(',')
                    score = int(data[0])
                    gold = int(data[1])
                if score < 50000:
                    pass
                else:
                    weapon_to_rewrite = 1
                    with open('assets/info.txt', 'w') as file:
                        file.write(f"{score},{gold},{weapon_to_rewrite}")
                    fade()
                    running = False

            if event.type == pygame.USEREVENT and event.button == back:
                fade()
                running = False

            for button in [select_1, select_2, back]:
                button.check_click(event)

        screen.blit(default, (width / 2.7 - (width / 5), height / 3))
        screen.blit(shotgun, (width * (2 / 3) + (height / 12), height / 3))
        for button in [select_1, select_2, back]:
            button.check_hover(pygame.mouse.get_pos())
            button.show(screen)

        pygame.display.flip()


def introduction_menu():
    back = MenuButton(width / 2 - 200, height / 2, 400, height / 10, 'Ok', 'assets/red_button.png',
                      'assets/red_button_hover.png', 'assets/click.ogg')
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(menu_background, (0, 0))

        font = pygame.font.Font('assets/Silver.ttf', 50)
        text_surface = font.render("Меню: Esc-назад", True, (255, 100, 150))
        text_surface1 = font.render("Игра: WASD-движение, Пробел-стрельба, Esc-пауза", True, (255, 100, 150))
        text_rect = text_surface.get_rect(center=(width / 2, 200))
        text_rect1 = text_surface.get_rect(center=(width / 2 - text_surface1.get_width() / 4, 300))
        screen.blit(text_surface, text_rect)
        screen.blit(text_surface1, text_rect1)

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
    logout = MenuButton((width / 3) - (width / 6.4), height / 1.8, width / 3.2, height / 9.6, 'Да',
                        'assets/red_button.png',
                        'assets/red_button_hover.png', 'assets/click.ogg')
    back = MenuButton(width * 2 / 3 - (width / 6.4), height / 1.8, width / 3.2, height / 9.6, 'Нет',
                      'assets/yellow_button.png', 'assets/yellow_button_hover.png', 'assets/click.ogg')

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(menu_background, (0, 0))

        font = pygame.font.Font('assets/Silver.ttf', 100)
        text_surface = font.render("Выйти из игры?", True, (255, 90, 205))
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
    sd = MenuButton(width / 2 - 200, height / 4, 400, height / 15, '960x544', 'assets/yellow_button.png',
                    'assets/yellow_button_hover.png', 'assets/click.ogg')
    hd = MenuButton(width / 2 - 200, height / 4 + 72, 400, height / 15, '1280x720', 'assets/yellow_button.png',
                    'assets/yellow_button_hover.png', 'assets/click.ogg')
    fullhd = MenuButton(width / 2 - 200, height / 4 + 144, 400, height / 15, '1920x1080', 'assets/yellow_button.png',
                        'assets/yellow_button_hover.png', 'assets/click.ogg')
    fullscreen = MenuButton(width / 2 - 200, height / 4 + 216, 400, height / 15, 'Полный экран',
                            'assets/yellow_button.png',
                            'assets/yellow_button_hover.png', 'assets/click.ogg')
    back = MenuButton(width / 2 - 200, height / 4 + 288, 400, height / 15, 'Назад', 'assets/red_button.png',
                      'assets/red_button_hover.png', 'assets/click.ogg')

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(menu_background, (0, 0))

        font = pygame.font.Font('assets/Silver.ttf', 100)
        text_surface = font.render("Выбор разрешения", True, (255, 90, 205))
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
    global current_volume
    main_font = pygame.font.Font('assets/Silver.ttf', 100)
    second_font = pygame.font.Font('assets/Silver.ttf', 70)
    if current_volume == 0:
        display_volume = 0
    else:
        display_volume = int(current_volume * 250)
    back = MenuButton(width * 0.01, (height * 0.98) - (height / 14), width / 6, height / 14, 'Назад',
                      'assets/red_button.png', 'assets/red_button_hover.png', 'assets/click.ogg')
    level_0 = MenuButton(width / 8, height / 2, width / 10, height / 10, '0', 'assets/yellow_button.png',
                         'assets/yellow_button_hover.png', 'assets/click.ogg')
    level_1 = MenuButton(width / 8 * 2, height / 2, width / 10, height / 10, '20%', 'assets/yellow_button.png',
                         'assets/yellow_button_hover.png', 'assets/click.ogg')
    level_2 = MenuButton(width / 8 * 3, height / 2, width / 10, height / 10, '40%', 'assets/yellow_button.png',
                         'assets/yellow_button_hover.png', 'assets/click.ogg')
    level_3 = MenuButton(width / 8 * 4, height / 2, width / 10, height / 10, '60%', 'assets/yellow_button.png',
                         'assets/yellow_button_hover.png', 'assets/click.ogg')
    level_4 = MenuButton(width / 8 * 5, height / 2, width / 10, height / 10, '80%', 'assets/yellow_button.png',
                         'assets/yellow_button_hover.png', 'assets/click.ogg')
    level_5 = MenuButton(width / 8 * 6, height / 2, width / 10, height / 10, '100%', 'assets/yellow_button.png',
                         'assets/yellow_button_hover.png', 'assets/click.ogg')
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(menu_background, (0, 0))
        volume_text = second_font.render(f'Текущий уровень громкости: {display_volume}%', True, (255, 0, 0))
        screen.blit(volume_text,
                    (width / 2 - volume_text.get_width() / 2, height / 2.5 - volume_text.get_height() / 2.5))
        text_surface = main_font.render("Изменить громкость", True, (255, 90, 205))
        text_rect = text_surface.get_rect(center=(width / 2, height / 7.2))
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

            if event.type == pygame.USEREVENT and event.button == level_0:
                current_volume = 0
                pygame.mixer.music.set_volume(current_volume)
                fade()
                running = False

            if event.type == pygame.USEREVENT and event.button == level_1:
                current_volume = 0.08
                pygame.mixer.music.set_volume(current_volume)
                fade()
                running = False

            if event.type == pygame.USEREVENT and event.button == level_2:
                current_volume = 0.16
                pygame.mixer.music.set_volume(current_volume)
                fade()
                running = False

            if event.type == pygame.USEREVENT and event.button == level_3:
                current_volume = 0.24
                pygame.mixer.music.set_volume(current_volume)
                fade()
                running = False

            if event.type == pygame.USEREVENT and event.button == level_4:
                current_volume = 0.32
                pygame.mixer.music.set_volume(current_volume)
                fade()
                running = False

            if event.type == pygame.USEREVENT and event.button == level_5:
                current_volume = 0.4
                pygame.mixer.music.set_volume(current_volume)
                fade()
                running = False

            for button in [back, level_0, level_1, level_2, level_3, level_4, level_5]:
                button.check_click(event)

        for button in [back, level_0, level_1, level_2, level_3, level_4, level_5]:
            button.check_hover(pygame.mouse.get_pos())
            button.show(screen)

        pygame.display.flip()


def change_resolution(w, h):
    global width, height, screen, menu_background
    width, height = w, h
    screen = pygame.display.set_mode((w, h))
    menu_background = pygame.image.load(f'assets/menu_background_{h}.jpg')
    fade()


def switch_fullscreen():
    global width, height, screen, menu_background
    width, height = monitor_size
    screen = pygame.display.set_mode(monitor_size, pygame.FULLSCREEN)
    menu_background = pygame.image.load('assets/menu_background_1080.jpg')


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
