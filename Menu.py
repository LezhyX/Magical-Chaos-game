import pygame
import sys
from Button import MenuButton

pygame.init()
width, height = 1280, 720

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Magical Chaos")
menu_background = pygame.image.load('menu_background.jpg')


def main_menu():
    choose_level = MenuButton(width / 2 - 200, 230, 400, 75, 'Выбрать уровень', 'red_button.png',
                              'red_button_hover.png',
                              'click.ogg')
    gear = MenuButton(width / 2 - 200, 350, 400, 50, 'Снаряжение', 'yellow_button.png', 'yellow_button_hover.png',
                      'click.ogg')
    introduction = MenuButton(width / 2 - 200, 425, 400, 50, 'Справка', 'yellow_button.png', 'yellow_button_hover.png',
                              'click.ogg')
    settings = MenuButton(width / 2 - 200, 500, 400, 50, 'Настройки', 'yellow_button.png', 'yellow_button_hover.png',
                          'click.ogg')
    log_out = MenuButton(width / 2 - 200, 575, 400, 50, 'Выйти', 'yellow_button.png', 'yellow_button_hover.png',
                         'click.ogg')
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(menu_background, (0, 0))

        font = pygame.font.Font('Silver.ttf', 150)
        text_surface = font.render("Magical Chaos", True, (106, 90, 205))
        text_rect = text_surface.get_rect(center=(width / 2, 100))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            for button in [choose_level, gear, introduction, settings, log_out]:
                button.check_click(event)

        for button in [choose_level, gear, introduction, settings, log_out]:
            button.check_hover(pygame.mouse.get_pos())
            button.show(screen)
        pygame.display.flip()


if __name__ == '__main__':
    main_menu()
