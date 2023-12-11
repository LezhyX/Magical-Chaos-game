import pygame
import random
import sys
import math

bullets = pygame.sprite.Group()
projectiles = pygame.sprite.Group()
mobs = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()


class Mob(pygame.sprite.Sprite):
    def __init__(self, spawn_x, spawn_y):
        width = spawn_x
        height = spawn_y
        self.hp = 30
        self.speed_x, self.speed_y = 5, 5
        pygame.sprite.Sprite.__init__(self)
        self.spritesheet = pygame.image.load('assets/bat.png')
        self.image = pygame.Surface((50, 50))
        self.rect = self.image.get_rect()
        self.frame = 0
        self.animation_speed = 100
        self.last_update = pygame.time.get_ticks()
        self.points = [[width / 4, height / 6], [width * (3 / 4), height / 6],
                       [width / 4, height / 2], [width * (3 / 4), height / 2]]
        self.rect.x, self.rect.y = random.choice(self.points)
        self.collide_damage = 10

    def get_image(self, x, y, width, height):
        image = pygame.Surface((width, height))
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))
        image = pygame.transform.scale(image, (50, 50))
        return image

    def update(self, width, height):
        if self.rect.x <= width * (3 / 4) and self.rect.y <= height / 6:
            self.rect.x += self.speed_x
        if self.rect.x >= width * (3 / 4) and self.rect.y <= height / 2:
            self.rect.y += self.speed_y
        if self.rect.x >= width / 4 and self.rect.y >= height / 2:
            self.rect.x -= self.speed_x
        if self.rect.x <= width / 4 and self.rect.y >= height / 6:
            self.rect.y -= self.speed_y
        now = pygame.time.get_ticks()
        if now - self.last_update > self.animation_speed:
            self.last_update = now
            self.frame = (self.frame + 1) % 4
            self.image = self.get_image(self.frame * 32, 0, 32, 32)
        self.image.set_colorkey((0, 0, 0))

    def hit(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.kill()

    def shoot(self, player_position):
        dx = player_position[0] - self.rect.centerx
        dy = player_position[1] - self.rect.centery
        angle_to_player = math.atan2(dy, dx)

        projectile_center = Projectile(self.rect.centerx, self.rect.bottom, int(math.degrees(angle_to_player)))
        projectile_left = Projectile(self.rect.centerx, self.rect.bottom,
                                     int(math.degrees(angle_to_player + math.pi / 8)))
        projectile_right = Projectile(self.rect.centerx, self.rect.bottom,
                                      int(math.degrees(angle_to_player - math.pi / 8)))

        projectiles.add(projectile_center, projectile_left, projectile_right)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load('assets/beam.png').convert_alpha(), (10, 20))
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10
        self.damage = 10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()


class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, angle=90):
        pygame.sprite.Sprite.__init__(self)
        self.images = [pygame.transform.scale(pygame.image.load('assets/Fireball1.png').convert_alpha(), (30, 30)),
                       pygame.transform.scale(pygame.image.load('assets/Fireball2.png').convert_alpha(), (30, 30))]
        self.index = 0
        self.image = self.images[self.index]
        self.original_image = self.image
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.centerx = x
        self.speed = 10
        self.angle = math.radians(angle)
        self.speed_x = self.speed * math.cos(self.angle)
        self.speed_y = self.speed * math.sin(self.angle)
        self.animation_speed = 150
        self.last_update = pygame.time.get_ticks()
        self.damage = 10

    def update(self, height):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.animation_speed:
            self.last_update = now
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
        if self.rect.top > height:
            self.kill()
        angle = math.degrees(math.atan2(-self.speed_y, self.speed_x))
        self.image = pygame.transform.rotate(self.original_image, angle)
        self.rect = self.image.get_rect(center=self.rect.center)


class Player(pygame.sprite.Sprite):
    def __init__(self, spawn_x, spawn_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("assets/player.png"), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.centerx = spawn_x / 2
        self.rect.bottom = spawn_y - 50
        self.speed_x = 0
        self.speed_y = 0
        self.hp = 100
        self.invincible = False
        self.invincible_duration = 1000
        self.invincible_timer = pygame.time.get_ticks()
        self.last_flash = 0

    def update(self, range_x, range_y):
        current_time = pygame.time.get_ticks()
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
        if self.invincible:
            if current_time - self.invincible_timer > self.invincible_duration:
                self.invincible = False
                self.image.set_alpha(255)
            elif current_time - self.last_flash > 100:
                self.image.set_alpha(80 if self.image.get_alpha() == 255 else 255)
                self.last_flash = current_time

    def hit(self, damage):
        if not self.invincible:
            self.hp -= damage
            self.invincible = True
            self.invincible_timer = pygame.time.get_ticks()

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        bullets.add(bullet)


def start_tutorial(width, height, screen):
    score, combo, last_mob_spawn, last_mob_shoot, pause_start_time, pause_duration = 0, 0, 0, 0, 0, 0
    mobs_music = pygame.mixer.Sound('assets/cave_mobs.mp3')
    mobs_music_channel = mobs_music.play()
    mobs_music_channel.set_volume(0.2)
    paused = False
    clock = pygame.time.Clock()
    player = Player(width, height)
    all_sprites.add(player)
    font = pygame.font.Font('assets/Silver.ttf', 50)
    background = pygame.transform.scale(pygame.image.load('assets/cave.png').convert(), (width, height))
    pause_surface = pygame.Surface((width, height))
    pause_surface.set_alpha(128)
    start_time = pygame.time.get_ticks()
    running = True
    while running:
        clock.tick(60)
        if not paused:
            game_time = pygame.time.get_ticks() - pause_duration
            screen.blit(background, (0, 0))

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        player.shoot()
                    elif event.key == pygame.K_ESCAPE:
                        paused = not paused

            if 7000 <= game_time - start_time <= 55000:
                if game_time - last_mob_spawn >= 2500:
                    mob = Mob(width, height)
                    mobs.add(mob)
                    last_mob_spawn = game_time

            if game_time - last_mob_shoot >= 2000:
                for mob in mobs:
                    mob.shoot((player.rect.centerx, player.rect.centery))
                last_mob_shoot = game_time

            mobs.update(width, height)
            projectiles.update(height)
            bullets.update()
            all_sprites.update(width, height)

            hits = pygame.sprite.spritecollide(player, mobs, False)
            for hit in hits:
                combo = 0
                player.hit(10)

            for mob in mobs:
                hits = pygame.sprite.spritecollide(mob, bullets, True)
                for bullet in hits:
                    combo += 10
                    score += combo
                    mob.hit(bullet.damage)

            hits = pygame.sprite.groupcollide(all_sprites, projectiles, False, True)
            if hits:
                player.hit(10)
            if player.hp == 0:
                mobs_music_channel.stop()
                bullets.empty()
                mobs.empty()
                projectiles.empty()
                all_sprites.empty()
                pause_time = 0
                running = False

        if paused:
            if pause_start_time == 0:
                pause_start_time = pygame.time.get_ticks()
                mobs_music_channel.pause()
            screen.blit(background, (0, 0))
            screen.blit(pause_surface, (0, 0))
            text_surface = font.render("Пауза", True, (106, 90, 205))
            text_rect = text_surface.get_rect(center=(width / 2, height / 2))
            screen.blit(text_surface, text_rect)
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pause_end_time = pygame.time.get_ticks()
                        pause_duration += pause_end_time - pause_start_time
                        pause_start_time = 0
                        mobs_music_channel.unpause()
                        paused = not paused

        game_time -= pause_duration
        all_sprites.draw(screen)
        projectiles.draw(screen)
        bullets.draw(screen)
        mobs.draw(screen)
        score_text = font.render("Счет:" + str(score), True, (255, 255, 255))
        hp_text = font.render('HP:' + str(player.hp), True, (255, 255, 255))
        screen.blit(score_text, (width - 150, 10))
        screen.blit(hp_text, (width - 150, 50))
        pygame.display.flip()
