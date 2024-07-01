import pygame
import random

from settings import *

class Vine(pygame.sprite.Sprite):

    def __init__(self, game, image, loc):
        super().__init__()

        self.game = game
        self.image = image
        self.mask = pygame.mask.from_surface(self.game.vine_hitbox_img)
        self.rect = self.image.get_rect()
        self.rect.midbottom = loc
        
        self.vine_position = 0
        self.movement_distance = 160 * SCALE
        self.score = 0
        self.score_multiplier = 1
        self.powerup_timer = 0
        self.has_a_score_multiplier = False
        self.a_few_frames = 3
        self.frame_countdown = self.a_few_frames
        self.must_animate = False

    def move_left(self):
        if self.vine_position > -2:
            self.vine_position -= 1

    def move_right(self):
        if self.vine_position < 2:
            self.vine_position += 1

    def check_position(self):
        if self.vine_position == -2:
            self.rect.centerx = WIDTH // 2 - self.movement_distance - self.movement_distance
        elif self.vine_position == -1:
            self.rect.centerx = WIDTH // 2 - self.movement_distance
        elif self.vine_position == 0:
            self.rect.centerx = WIDTH // 2
        elif self.vine_position == 1:
            self.rect.centerx = WIDTH // 2 + self.movement_distance
        elif self.vine_position == 2:
            self.rect.centerx = WIDTH // 2 + self.movement_distance + self.movement_distance

    def check_bugs(self):
        hit_bugs = pygame.sprite.spritecollide(self, self.game.buggies, True, pygame.sprite.collide_mask)

        for bug in hit_bugs:
            if self.game.bug.bug_type > 6:
                self.score += 2 * self.score_multiplier # IDK why 2 equals 4 score points ¯\_(ツ)_/¯
            if self.game.bug.bug_type > 4 and self.game.bug.bug_type < 17:
                self.score += 2 * self.score_multiplier
            else:
                self.score += 1 * self.score_multiplier
            
            if self.game.game_mode == 1:
                self.game.load_buggies()
            elif self.game.game_mode == 2:
                self.game.load_buggies()
            self.must_animate = True
                
    def check_second_bugs(self):
        hit_second_bugs = pygame.sprite.spritecollide(self, self.game.second_buggies, True, pygame.sprite.collide_mask)

        for bug in hit_second_bugs:
            if self.game.bug.bug_type > 6:
                self.score += 2 * self.score_multiplier # IDK why 2 equals 4 score points ¯\_(ツ)_/¯
            if self.game.bug.bug_type > 4 and self.game.bug.bug_type < 17:
                self.score += 2 * self.score_multiplier
            else:
                self.score += 1 * self.score_multiplier
            
            if self.game.game_mode == 2:
                self.game.load_second_buggies()
            self.must_animate = True

    def animate(self):
        if self.must_animate == True:
            if self.frame_countdown > 0:
                self.frame_countdown -= 1
            else:
                if self.image == self.game.vine_four_img:
                    self.image = self.game.vine_three_img
                    
                elif self.image == self.game.vine_three_img:
                    self.image = self.game.vine_two_img
                    
                elif self.image == self.game.vine_two_img:
                    self.image = self.game.vine_one_img

                elif self.image == self.game.vine_one_img:
                    self.image = self.game.vine_one_again_img
                    
                elif self.image == self.game.vine_one_again_img:
                    self.image = self.game.vine_two_again_img
                    
                elif self.image == self.game.vine_two_again_img:
                    self.image = self.game.vine_three_again_img
                    
                elif self.image == self.game.vine_three_again_img:
                    self.image = self.game.vine_four_img
                    self.must_animate = False
                self.frame_countdown = self.a_few_frames

    def check_powerups(self):
        hit_powerups = pygame.sprite.spritecollide(self, self.game.powerups, True, pygame.sprite.collide_mask)

        for powerup in hit_powerups:
            if self.game.powerup.powerup_type == 1:
                self.has_a_score_multiplier = True
                self.powerup_timer = TWENTY_SECONDS
            self.game.load_powerups()

    def apply_honey(self):
        if self.has_a_score_multiplier == True:
            self.score_multiplier = 2
            if self.powerup_timer > 0:
                self.powerup_timer -= 1
            else:
                self.has_a_score_multiplier = False
        else:
            self.score_multiplier = 1

    def update(self):
        self.check_bugs()
        self.check_second_bugs()
        self.check_powerups()
        self.check_position()
        self.apply_honey()
        self.animate()


class Bug(pygame.sprite.Sprite):

    def __init__(self, game, image, loc):
        super().__init__()

        self.game = game
        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.midbottom = loc

        self.bug_type = 1
        self.bug_position = 0
        self.movement_distance = 160 * SCALE
        self.falling_speed = 4 * SCALE

    def randomize_bug(self):
        self.bug_position = random.randint(1, 5)

        if self.game.vine.score > 5:
            self.bug_type = random.randint(1, 7)
        elif self.game.vine.score > 3:
            self.bug_type = random.randint(1, 6)
        else:
            self.bug_type = random.randint(1, 4)

    def create_bug(self):
        self.randomize_bug()

        #Position
        if self.bug_position == 1:
            self.rect.centerx = WIDTH // 2 - self.movement_distance - self.movement_distance
        elif self.bug_position == 2:
            self.rect.centerx = WIDTH // 2 - self.movement_distance
        elif self.bug_position == 3:
            self.rect.centerx = WIDTH // 2
        elif self.bug_position == 4:
            self.rect.centerx = WIDTH // 2 + self.movement_distance
        elif self.bug_position == 5:
            self.rect.centerx = WIDTH // 2 + self.movement_distance + self.movement_distance

        #Bug Type
        if self.bug_type <= 4:
            self.image = self.game.caterpie_img
        elif self.bug_type == 5 or self.bug_type == 6:
            self.image = self.game.metapod_img
        elif self.bug_type == 7:
            self.image = self.game.butterfree_img
        
        self.mask = pygame.mask.from_surface(self.image)

    def gradually_increase_difficulty(self):        
        if self.game.vine.score > self.game.first_difficulty_spike:
            self.falling_speed = 5 * SCALE
        if self.game.vine.score > self.game.second_difficulty_spike:
            self.falling_speed = 6 * SCALE
        if self.game.vine.score > self.game.third_difficulty_spike:
            self.falling_speed = 7 * SCALE
        if self.game.vine.score > self.game.fourth_difficulty_spike:
            self.falling_speed = 8 * SCALE
        if self.game.vine.score > self.game.fifth_difficulty_spike:
            self.falling_speed = 9 * SCALE
        if self.game.vine.score > self.game.sixth_difficulty_spike:
            self.falling_speed = 10 * SCALE
        if self.game.vine.score > self.game.seventh_difficulty_spike:
            self.falling_speed = 11 * SCALE
        if self.game.vine.score > self.game.eighth_difficulty_spike:
            self.falling_speed = 12 * SCALE
        if self.game.vine.score > self.game.ninth_difficulty_spike:
            self.falling_speed = 13 * SCALE
        if self.game.vine.score > self.game.tenth_difficulty_spike:
            self.falling_speed = 14 * SCALE

    def fall_down(self):
        self.rect.y += self.falling_speed

    def reach_the_bottom(self):
        if self.rect.bottom >= HEIGHT:
            self.game.lose()
        
    def update(self):
        self.fall_down()
        self.gradually_increase_difficulty()
        self.reach_the_bottom()


class SecondBug(pygame.sprite.Sprite):

    def __init__(self, game, image, loc):
        super().__init__()

        self.game = game
        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.midbottom = loc

        self.bug_type = 1
        self.bug_position = 0
        self.movement_distance = 160 * SCALE
        self.falling_speed = 4 * SCALE

    def randomize_bug(self):
        self.bug_position = random.randint(1, 5)

        if self.game.vine.score > 5:
            self.bug_type = random.randint(1, 7)
        elif self.game.vine.score > 3:
            self.bug_type = random.randint(1, 6)
        else:
            self.bug_type = random.randint(1, 4)

    def create_bug(self):
        self.randomize_bug()

        #Position
        if self.bug_position == 1:
            self.rect.centerx = WIDTH // 2 - self.movement_distance - self.movement_distance
        elif self.bug_position == 2:
            self.rect.centerx = WIDTH // 2 - self.movement_distance
        elif self.bug_position == 3:
            self.rect.centerx = WIDTH // 2
        elif self.bug_position == 4:
            self.rect.centerx = WIDTH // 2 + self.movement_distance
        elif self.bug_position == 5:
            self.rect.centerx = WIDTH // 2 + self.movement_distance + self.movement_distance

        #Bug Type
        if self.bug_type <= 4:
            self.image = self.game.weedle_img
        elif self.bug_type == 5 or self.bug_type == 6:
            self.image = self.game.kakuna_img
        elif self.bug_type == 7:
            self.image = self.game.beedrill_img
        
        self.mask = pygame.mask.from_surface(self.image)

    def gradually_increase_difficulty(self):        
        if self.game.vine.score > self.game.first_difficulty_spike:
            self.falling_speed = 5 * SCALE
        if self.game.vine.score > self.game.second_difficulty_spike:
            self.falling_speed = 6 * SCALE
        if self.game.vine.score > self.game.third_difficulty_spike:
            self.falling_speed = 7 * SCALE
        if self.game.vine.score > self.game.fourth_difficulty_spike:
            self.falling_speed = 8 * SCALE
        if self.game.vine.score > self.game.fifth_difficulty_spike:
            self.falling_speed = 9 * SCALE
        if self.game.vine.score > self.game.sixth_difficulty_spike:
            self.falling_speed = 10 * SCALE
        if self.game.vine.score > self.game.seventh_difficulty_spike:
            self.falling_speed = 11 * SCALE
        if self.game.vine.score > self.game.eighth_difficulty_spike:
            self.falling_speed = 12 * SCALE
        if self.game.vine.score > self.game.ninth_difficulty_spike:
            self.falling_speed = 13 * SCALE
        if self.game.vine.score > self.game.tenth_difficulty_spike:
            self.falling_speed = 14 * SCALE

    def fall_down(self):
        self.rect.y += self.falling_speed

    def reach_the_bottom(self):
        if self.rect.bottom >= HEIGHT:
            self.game.lose()
        
    def update(self):
        self.fall_down()
        self.gradually_increase_difficulty()
        self.reach_the_bottom()


class PowerUp(pygame.sprite.Sprite):

    def __init__(self, game, image, loc):
        super().__init__()

        self.game = game
        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.topleft = loc

        self.powerup_type = 0
        self.powerup_position = 0
        self.movement_distance = 160 * SCALE
        self.falling_speed = 4 * SCALE

    def randomize_powerup_type(self):
        if self.game.vine.has_a_score_multiplier == False:
            self.powerup_type = random.randint(1, 15)
        else:
            self.powerup_type = random.randint(2, 15)
        self.powerup_position = random.randint(1, 5)

    def create_powerup(self):
        self.randomize_powerup_type()
        self.mask = pygame.mask.from_surface(self.image)

        #Position
        if self.powerup_position == 1:
            self.rect.centerx = WIDTH // 2 - self.movement_distance - self.movement_distance
        elif self.powerup_position == 2:
            self.rect.centerx = WIDTH // 2 - self.movement_distance
        elif self.powerup_position == 3:
            self.rect.centerx = WIDTH // 2
        elif self.powerup_position == 4:
            self.rect.centerx = WIDTH // 2 + self.movement_distance
        elif self.powerup_position == 5:
            self.rect.centerx = WIDTH // 2 + self.movement_distance + self.movement_distance

        self.mask = pygame.mask.from_surface(self.image)

        #PowerUp Type
        if self.powerup_type == 1:
            self.image = self.game.honey_img
            self.game.vine.score += 0
        else:
            self.image = self.game.blank_img
            self.game.vine.score += 0

    def gradually_increase_difficulty(self):        
        if self.game.vine.score > self.game.first_difficulty_spike:
            self.falling_speed = 5 * SCALE
        if self.game.vine.score > self.game.second_difficulty_spike:
            self.falling_speed = 6 * SCALE
        if self.game.vine.score > self.game.third_difficulty_spike:
            self.falling_speed = 7 * SCALE
        if self.game.vine.score > self.game.fourth_difficulty_spike:
            self.falling_speed = 8 * SCALE
        if self.game.vine.score > self.game.fifth_difficulty_spike:
            self.falling_speed = 9 * SCALE
        if self.game.vine.score > self.game.sixth_difficulty_spike:
            self.falling_speed = 10 * SCALE
        if self.game.vine.score > self.game.seventh_difficulty_spike:
            self.falling_speed = 11 * SCALE
        if self.game.vine.score > self.game.eighth_difficulty_spike:
            self.falling_speed = 12 * SCALE
        if self.game.vine.score > self.game.ninth_difficulty_spike:
            self.falling_speed = 13 * SCALE
        if self.game.vine.score > self.game.tenth_difficulty_spike:
            self.falling_speed = 14 * SCALE

    def fall_down(self):
        self.rect.y += self.falling_speed

    def reach_the_bottom(self):
        if self.rect.top >= HEIGHT:
            self.game.load_powerups()
            
    def update(self):
        self.fall_down()
        self.gradually_increase_difficulty()
        self.reach_the_bottom()


class HoneyBar(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        super().__init__()

        self.game = game
        self.x = x
        self.y = y
        self.w = 198
        self.h = 27
        self.ratio = 1
        self.falling_speed = 4 * SCALE
        self.ascending_speed = self.falling_speed * 2.25
        self.offscreen_y_value = -70 * SCALE
        self.onscreen_y_value = 73 * SCALE 

    def draw_me(self, surface):
        self.game.screen.blit(self.game.honey_bar_outline_img, [self.x, self.y])

        pygame.draw.rect(surface, "brown", (self.x + 61 * SCALE, self.y + 20 * SCALE, self.w * SCALE, self.h * SCALE))
        pygame.draw.rect(surface, "orange", (self.x + 61 * SCALE, self.y + 20 * SCALE, self.w * SCALE * self.ratio, self.h * SCALE))

        self.game.screen.blit(self.game.honey_icon_img, [self.x, self.y])

        if self.game.vine.has_a_score_multiplier == True:
            self.ratio -= 1 / TWENTY_SECONDS
            if self.y <= self.onscreen_y_value:
                self.y += self.falling_speed
        else:
            self.ratio = 1
            if self.y >= self.offscreen_y_value:
                self.y -= self.ascending_speed


class A_BLAAAAANK_CLASS(pygame.sprite.Sprite):

    def __init__(self, game, image, loc):
        super().__init__()

        self.game = game
        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.topleft = loc

    def update(self):
        pass
