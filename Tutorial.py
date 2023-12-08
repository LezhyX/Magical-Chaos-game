import pygame
import sys
import random

bullets = pygame.sprite.Group()
mobs = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()


class Mob(pygame.sprite.Sprite):
    def __init__(self, spawn_x, spawn_y):
        width = spawn_x
        height = spawn_y
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.points = [[width / 4, height / 6], [width / 2, height * (1 / 3)], [width * (3 / 4), height / 2],
                       [width / 4, height * (1 / 3)], [width / 2, height / 6], [width * (3 / 4), height / 6],
                       [width / 4, height / 2], [width / 2, height / 2], [width * (3 / 4), height * (1 / 3)]]
        self.rect.x, self.rect.y = random.choice(self.points)

    def update(self, width, height):
        self.rect.x, self.rect.y = random.choice(self.points)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()


class Player(pygame.sprite.Sprite):
    def __init__(self, spawn_x, spawn_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.centerx = spawn_x / 2
        self.rect.bottom = spawn_y - 50
        self.speed_x = 0
        self.speed_y = 0

    def update(self, range_x, range_y):
        self.speed_x = 0
        self.speed_y = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.speed_x = -7.5
        if keystate[pygame.K_d]:
            self.speed_x = 7.5
        if keystate[pygame.K_w]:
            self.speed_y = -7.5
        if keystate[pygame.K_s]:
            self.speed_y = 7.5
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.right >= range_x:
            self.rect.right = range_x
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.bottom >= range_y:
            self.rect.bottom = range_y
        if self.rect.top <= 0:
            self.rect.top = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        bullets.add(bullet)


def start_tutorial(width, height, screen):
    clock = pygame.time.Clock()
    mobs_spawn_timer, mobs_move_timer = 5000, 1000
    player = Player(width, height)
    all_sprites.add(player)
    mobs.empty()
    start_time = pygame.time.get_ticks()
    last_move = 0

    running = True
    last_spawn, last_fly = pygame.time.get_ticks(), pygame.time.get_ticks()
    while running:
        screen.fill((255, 255, 255))
        clock.tick(60)
        current_time = pygame.time.get_ticks()
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot()

        if 10000 < current_time - start_time < 60000 and current_time - last_spawn > mobs_spawn_timer:
            mob = Mob(width, height)
            mobs.add(mob)
            last_spawn = current_time

        if current_time - last_move > mobs_move_timer and current_time - start_time < 60000:
            mobs.update(width, height)
            last_move = current_time
        bullets.update()

        all_sprites.update(width, height)
        hits = pygame.sprite.spritecollide(player, mobs, False)
        if hits:
            bullets.empty()
            mobs.empty()
            all_sprites.empty()
            running = False
        hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
        for hit in hits:
            mobs.update(width, height)
        all_sprites.draw(screen)
        bullets.draw(screen)
        mobs.draw(screen)
        pygame.display.flip()
