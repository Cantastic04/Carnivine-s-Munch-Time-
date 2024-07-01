# Imports
import pygame

from entities import *
from settings import *


# Main game class 
class Game:
    
    # Scenes
    START_ONE = -1
    START_TWO = -2
    START_THREE_A = -3
    START_THREE_B = 0
    PLAYING = 1
    PAUSE = 2
    LOSE = 3
    
    def __init__(self):
        # Initialize pygame
        pygame.mixer.pre_init()
        pygame.init()

        # Make window
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True

        # Set up game
        self.start_option = 1
        self.how_to_play_option = 1
        self.pause_option = 1
        self.lose_option = 1
        self.high_score_A = 0
        self.high_score_B = 0
        self.game_mode = 1

        self.load_assets()
        self.new_game()

    def load_assets(self):
        self.title_font = pygame.font.Font('assets/fonts/Dinofans.ttf', 48)# * SCALE)
        self.bigger_title_font = pygame.font.Font('assets/fonts/Dinofans.ttf', 54)# * SCALE)

        self.blank_img = pygame.image.load('assets/images/blank.png').convert_alpha()
        self.blank_img = pygame.transform.scale_by(self.blank_img, [SCALE, SCALE])

        # Title/Lose Screens
        self.title_screen_img = pygame.image.load('assets/images/title screen.png').convert_alpha()
        self.title_screen_img = pygame.transform.scale_by(self.title_screen_img, [SCALE, SCALE])

        self.press_start_game_screen_img = pygame.image.load('assets/images/press start game screen.png').convert_alpha()
        self.press_start_game_screen_img = pygame.transform.scale_by(self.press_start_game_screen_img, [SCALE, SCALE])
        self.press_how_to_play_screen_img = pygame.image.load('assets/images/press how to play screen.png').convert_alpha()
        self.press_how_to_play_screen_img = pygame.transform.scale_by(self.press_how_to_play_screen_img, [SCALE, SCALE])

        self.game_A_screen_img = pygame.image.load('assets/images/game a screen.png').convert_alpha()
        self.game_A_screen_img = pygame.transform.scale_by(self.game_A_screen_img, [SCALE, SCALE])
        self.game_B_screen_img = pygame.image.load('assets/images/game b screen.png').convert_alpha()
        self.game_B_screen_img = pygame.transform.scale_by(self.game_B_screen_img, [SCALE, SCALE])
        self.how_to_play_screen_A_img = pygame.image.load('assets/images/how to play screen a.png').convert_alpha()
        self.how_to_play_screen_A_img = pygame.transform.scale_by(self.how_to_play_screen_A_img, [SCALE, SCALE])
        self.how_to_play_screen_B_img = pygame.image.load('assets/images/how to play screen b.png').convert_alpha()
        self.how_to_play_screen_B_img = pygame.transform.scale_by(self.how_to_play_screen_B_img, [SCALE, SCALE])

        self.lose_screen_a_img = pygame.image.load('assets/images/lose screen a.png').convert_alpha()
        self.lose_screen_a_img = pygame.transform.scale_by(self.lose_screen_a_img, [SCALE, SCALE])
        self.lose_screen_b_img = pygame.image.load('assets/images/lose screen b.png').convert_alpha()
        self.lose_screen_b_img = pygame.transform.scale_by(self.lose_screen_b_img, [SCALE, SCALE])
        
        """
        self.title_screen_oneA_img = pygame.image.load('assets/images/title screen a.png').convert_alpha()
        self.title_screen_oneA_img = pygame.transform.scale_by(self.title_screen_oneA_img, [SCALE, SCALE])
        self.title_screen_oneB_img = pygame.image.load('assets/images/title screen b.png').convert_alpha()
        self.title_screen_oneB_img = pygame.transform.scale_by(self.title_screen_oneB_img, [SCALE, SCALE])
        self.title_screen_twoA_img = pygame.image.load('assets/images/title screen a.png').convert_alpha()
        self.title_screen_twoA_img = pygame.transform.scale_by(self.title_screen_twoA_img, [SCALE, SCALE])
        self.title_screen_twoB_img = pygame.image.load('assets/images/title screen b.png').convert_alpha()
        self.title_screen_twoB_img = pygame.transform.scale_by(self.title_screen_twoB_img, [SCALE, SCALE])
        """

        self.background_img = pygame.image.load('assets/images/background.png').convert_alpha()
        self.background_img = pygame.transform.scale_by(self.background_img, [SCALE, SCALE])

        # Carnivine
        self.vine_one_img = pygame.image.load('assets/images/carnivine 1.png').convert_alpha()
        self.vine_one_img = pygame.transform.scale_by(self.vine_one_img, [SCALE, SCALE])
        self.vine_two_img = pygame.image.load('assets/images/carnivine 2.png').convert_alpha()
        self.vine_two_img = pygame.transform.scale_by(self.vine_two_img, [SCALE, SCALE])
        self.vine_three_img = pygame.image.load('assets/images/carnivine 3.png').convert_alpha()
        self.vine_three_img = pygame.transform.scale_by(self.vine_three_img, [SCALE, SCALE])
        self.vine_four_img = pygame.image.load('assets/images/carnivine 4.png').convert_alpha()
        self.vine_four_img = pygame.transform.scale_by(self.vine_four_img, [SCALE, SCALE])

        self.vine_one_again_img = pygame.image.load('assets/images/carnivine 1.png').convert_alpha()
        self.vine_one_again_img = pygame.transform.scale_by(self.vine_one_again_img, [SCALE, SCALE])
        self.vine_two_again_img = pygame.image.load('assets/images/carnivine 2.png').convert_alpha()
        self.vine_two_again_img = pygame.transform.scale_by(self.vine_two_again_img, [SCALE, SCALE])
        self.vine_three_again_img = pygame.image.load('assets/images/carnivine 3.png').convert_alpha()
        self.vine_three_again_img = pygame.transform.scale_by(self.vine_three_again_img, [SCALE, SCALE])
        
        self.vine_hitbox_img = pygame.image.load('assets/images/carnivine hitbox.png').convert_alpha()
        self.vine_hitbox_img = pygame.transform.scale_by(self.vine_hitbox_img, [SCALE, SCALE])

        # Bugs
        self.caterpie_img = pygame.image.load('assets/images/Caterpie.png').convert_alpha()
        self.caterpie_img = pygame.transform.scale_by(self.caterpie_img, [SCALE, SCALE])
        self.metapod_img = pygame.image.load('assets/images/Metapod.png').convert_alpha()
        self.metapod_img = pygame.transform.scale_by(self.metapod_img, [SCALE, SCALE])
        self.butterfree_img = pygame.image.load('assets/images/Butterfree.png').convert_alpha()
        self.butterfree_img = pygame.transform.scale_by(self.butterfree_img, [SCALE, SCALE])

        self.weedle_img = pygame.image.load('assets/images/Weedle.png').convert_alpha()
        self.weedle_img = pygame.transform.scale_by(self.weedle_img, [SCALE, SCALE])
        self.kakuna_img = pygame.image.load('assets/images/Kakuna.png').convert_alpha()
        self.kakuna_img = pygame.transform.scale_by(self.kakuna_img, [SCALE, SCALE])
        self.beedrill_img = pygame.image.load('assets/images/Beedrill.png').convert_alpha()
        self.beedrill_img = pygame.transform.scale_by(self.beedrill_img, [SCALE, SCALE])

        # Power Ups and Pause
        self.honey_img = pygame.image.load('assets/images/honey.png').convert_alpha()
        self.honey_img = pygame.transform.scale_by(self.honey_img, [SCALE, SCALE])
        self.honey_icon_img = pygame.image.load('assets/images/honey icon.png').convert_alpha()
        self.honey_icon_img = pygame.transform.scale_by(self.honey_icon_img, [SCALE, SCALE])
        self.honey_bar_outline_img = pygame.image.load('assets/images/honey bar outline.png').convert_alpha()
        self.honey_bar_outline_img = pygame.transform.scale_by(self.honey_bar_outline_img, [SCALE, SCALE])

        self.pause_option_1_img = pygame.image.load('assets/images/pause option 1.png').convert_alpha()
        self.pause_option_1_img = pygame.transform.scale_by(self.pause_option_1_img, [SCALE, SCALE])
        self.pause_option_2_img = pygame.image.load('assets/images/pause option 2.png').convert_alpha()
        self.pause_option_2_img = pygame.transform.scale_by(self.pause_option_2_img, [SCALE, SCALE])
        self.pause_option_3_img = pygame.image.load('assets/images/pause option 3.png').convert_alpha()
        self.pause_option_3_img = pygame.transform.scale_by(self.pause_option_3_img, [SCALE, SCALE])
    
    def randomize_difficulty_spike(self):
        self.first_difficulty_spike = random.randint(10, 15)
        self.second_difficulty_spike = random.randint(25, 30)
        self.third_difficulty_spike = random.randint(40, 45)
        self.fourth_difficulty_spike = random.randint(55, 60)
        self.fifth_difficulty_spike = random.randint(70, 75)
        self.sixth_difficulty_spike = random.randint(85, 90)     
        self.seventh_difficulty_spike = random.randint(100, 105)     
        self.eighth_difficulty_spike = random.randint(115, 120)     
        self.ninth_difficulty_spike = random.randint(130, 135)     
        self.tenth_difficulty_spike = random.randint(145, 150)

    def update_high_score(self):
        if self.game_mode == 1:
            if self.vine.score > self.high_score_A:
                self.high_score_A = self.vine.score
        elif self.game_mode == 2:
            if self.vine.score > self.high_score_B:
                self.high_score_B = self.vine.score
        
    def new_game(self):        
        self.player = pygame.sprite.Group()
        self.vine = Vine(self, self.vine_four_img, [WIDTH // 2, HEIGHT + 50 * SCALE])
        self.player.add(self.vine)

        self.orange_bar = HoneyBar(self, WIDTH // 3, -60 * SCALE)

        self.buggies = pygame.sprite.Group()
        
        self.second_buggies = pygame.sprite.Group()

        self.randomize_difficulty_spike()
        self.load_buggies()
        self.load_second_buggies()
        self.load_powerups()

    def load_buggies(self):
        self.bug = Bug(self, self.caterpie_img, [100, -60])
        self.buggies.add(self.bug)
        self.bug.create_bug()

    def load_second_buggies(self):
        self.second_bug = SecondBug(self, self.weedle_img, [300, -160])
        self.second_buggies.add(self.second_bug)
        self.second_bug.create_bug()

    def load_powerups(self):
        self.powerups = pygame.sprite.Group()
        self.powerup = PowerUp(self, self.honey_img, [WIDTH // 2, -60])
        self.powerups.add(self.powerup)
        self.powerup.create_powerup()

    def press_start(self):
        self.scene = Game.START_TWO

    def press_play(self):
        self.scene = Game.START_THREE_A

    def press_how_to_play(self):
        self.scene = Game.START_THREE_B
        
    def play(self):
        self.scene = Game.PLAYING

    def lose(self):
        self.lose_option = 1
        self.scene = Game.LOSE

    def pause(self):
        self.pause_option = 1
        self.scene = Game.PAUSE
        
    def show_title_screen(self):
        self.screen.blit(self.title_screen_img, [0, 0])

    def show_start_two_screen(self):
        if self.start_option == 1:
            self.screen.blit(self.press_start_game_screen_img, [0, 0])
        elif self.start_option == 2:
            self.screen.blit(self.press_how_to_play_screen_img, [0, 0])

    def show_start_three_A_screen(self):
        if self.game_mode == 1:
            self.screen.blit(self.game_A_screen_img, [0, 0])
        elif self.game_mode == 2:
            self.screen.blit(self.game_B_screen_img, [0, 0])
        
        text = self.title_font.render(f"{self.high_score_A}", True, DARK_BROWN)
        rect = text.get_rect()
        rect.midbottom = WIDTH // 3.85, 250 * SCALE
        self.screen.blit(text, rect)

        text = self.title_font.render(f"{self.high_score_B}", True, DARK_BROWN)
        rect = text.get_rect()
        rect.midtop = WIDTH // 3.85, 465 * SCALE
        self.screen.blit(text, rect)

    def show_start_three_B_screen(self):
        if self.how_to_play_option == 1:
            self.screen.blit(self.how_to_play_screen_A_img, [0, 0])
        elif self.how_to_play_option == 2:
            self.screen.blit(self.how_to_play_screen_B_img, [0, 0])

    def show_lose_screen(self):
        if self.lose_option == 1:
            self.screen.blit(self.lose_screen_a_img, [0, 0])
        elif self.lose_option == 2:
            self.screen.blit(self.lose_screen_b_img, [0, 0])

        if self.game_mode == 1:
            text = self.bigger_title_font.render(f"High Score: {self.high_score_A}", True, DARK_BROWN)
            rect = text.get_rect()
            rect.midbottom = WIDTH // 2, 280 * SCALE
            self.screen.blit(text, rect)

            text = self.bigger_title_font.render(f"Score: {self.vine.score}", True, DARK_BROWN)
            rect = text.get_rect()
            rect.midtop = WIDTH // 2, 280 * SCALE
            self.screen.blit(text, rect)
                
        elif self.game_mode == 2:
            text = self.bigger_title_font.render(f"High Score: {self.high_score_B}", True, DARK_BROWN)
            rect = text.get_rect()
            rect.midbottom = WIDTH // 2, 280 * SCALE
            self.screen.blit(text, rect)

            text = self.bigger_title_font.render(f"Score: {self.vine.score}", True, DARK_BROWN)
            rect = text.get_rect()
            rect.midtop = WIDTH // 2, 280 * SCALE
            self.screen.blit(text, rect)
                
    def show_pause_screen(self):
        if self.pause_option == 1:
            self.screen.blit(self.pause_option_1_img, [0, 0])
        elif self.pause_option == 2:
            self.screen.blit(self.pause_option_2_img, [0, 0])
        elif self.pause_option == 3:
            self.screen.blit(self.pause_option_3_img, [0, 0])

        if self.game_mode == 1:
            text = self.bigger_title_font.render(f"High Score: {self.high_score_A}", True, DARK_BROWN)
            rect = text.get_rect()
            rect.midbottom = WIDTH // 2, 265 * SCALE
            self.screen.blit(text, rect)
        else:
            text = self.bigger_title_font.render(f"High Score: {self.high_score_B}", True, DARK_BROWN)
            rect = text.get_rect()
            rect.midbottom = WIDTH // 2, 265 * SCALE
            self.screen.blit(text, rect)

    def show_hud(self):
        text = self.title_font.render(f"SCORE: {self.vine.score}", True, DARKER_BROWN)
        rect = text.get_rect()
        rect.midtop = WIDTH // 2, HEIGHT // 18
        self.screen.blit(text, rect)

        #text = self.title_font.render(f" {self.vine.score}", True, DARKER_BROWN)
        rect = text.get_rect()
        rect.topleft = WIDTH // 1.775, HEIGHT // 18
        #self.screen.blit(text, rect)

    def show_debug_hud(self):
        text = self.title_font.render(f"{self.high_score_A}", True, BLACK)
        rect = text.get_rect()
        rect.topright = 500, 200
        self.screen.blit(text, rect)

        text = self.title_font.render(f"{self.high_score_B}", True, BLACK)
        rect = text.get_rect()
        rect.topleft = 500, 250
        self.screen.blit(text, rect)
        
    def process_input(self):        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:
                #START_ONE
                if self.scene == Game.START_ONE:
                    if event.key == pygame.K_SPACE:
                        self.press_start()
                #START_TWO
                elif self.scene == Game.START_TWO:
                    if event.key == pygame.K_SPACE:
                        if self.start_option == 1:
                            self.press_play()
                        else:
                            self.press_how_to_play()
                    elif event.key == pygame.K_UP or event.key == pygame.K_w:
                        if self.start_option < 2:
                            self.start_option = 2
                        else:
                            self.start_option -= 1
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        if self.start_option > 1:
                            self.start_option = 1
                        else:
                            self.start_option += 1
                #START_THREE_A
                elif self.scene == Game.START_THREE_A:
                    if event.key == pygame.K_SPACE:
                        self.play()
                    elif event.key == pygame.K_UP or event.key == pygame.K_w:
                        if self.game_mode < 2:
                            self.game_mode = 2
                        else:
                            self.game_mode -= 1
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        if self.game_mode > 1:
                            self.game_mode = 1
                        else:
                            self.game_mode += 1
                    elif event.key == pygame.K_b:
                        self.press_start()
                #START_THREE_B
                elif self.scene == Game.START_THREE_B:
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.how_to_play_option = 2
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self.how_to_play_option = 1
                    elif event.key == pygame.K_b:
                        self.press_start()
                #PLAYING
                elif self.scene == Game.PLAYING:
                    if event.key == pygame.K_SPACE:
                        self.pause()
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.vine.move_right()
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self.vine.move_left()
                #PAUSE
                elif self.scene == Game.PAUSE:
                    if event.key == pygame.K_SPACE:
                        if self.pause_option == 1:
                            self.scene = Game.PLAYING
                        elif self.pause_option == 2:
                            if self.game_mode == 1:
                                self.new_game()
                                self.play()
                                self.game_mode == 1
                            else:
                                self.new_game()
                                self.play()
                                self.game_mode == 2
                        elif self.pause_option == 3:
                            self.new_game()
                            self.press_play()
                    elif event.key == pygame.K_UP or event.key == pygame.K_w:
                        if self.pause_option < 2:
                            self.pause_option = 3
                        else:
                            self.pause_option -= 1
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        if self.pause_option > 2:
                            self.pause_option = 1
                        else:
                            self.pause_option += 1
                #LOSE
                elif self.scene == Game.LOSE:
                    if event.key == pygame.K_SPACE:
                        self.new_game()
                        if self.lose_option == 1:
                            self.play()
                        else:
                            self.press_play()
                    elif event.key == pygame.K_UP or event.key == pygame.K_w:
                        if self.lose_option < 2:
                            self.lose_option = 2
                        else:
                            self.lose_option -= 1
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        if self.lose_option > 1:
                            self.lose_option = 1
                        else:
                            self.lose_option += 1

        pressed = pygame.key.get_pressed()

    def update(self):
        if self.scene == Game.PLAYING:
            if self.game_mode == 1:
                self.buggies.update()
            elif self.game_mode == 2:
                self.buggies.update()
                self.second_buggies.update()
            self.update_high_score()
            self.powerups.update()
            self.player.update()

    def render(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.background_img, [0, 0])
        if self.scene == Game.PLAYING or self.scene == Game.PAUSE:
            self.player.draw(self.screen)
            if self.game_mode == 1:
                self.buggies.draw(self.screen)
            elif self.game_mode == 2:
                self.buggies.draw(self.screen)
                self.second_buggies.draw(self.screen)
            self.powerups.draw(self.screen)
            self.orange_bar.draw_me(self.screen)
            self.show_hud()

        if self.scene == Game.START_ONE:
            self.show_title_screen()

        if self.scene == Game.START_TWO:
            self.show_start_two_screen()

        if self.scene == Game.START_THREE_A:
            self.show_start_three_A_screen()

        if self.scene == Game.START_THREE_B:
            self.show_start_three_B_screen()

        if self.scene == Game.LOSE:
            self.show_lose_screen()

        if self.scene == Game.PAUSE:
            self.show_pause_screen()
        #self.show_debug_hud()
        
    def run(self):
        self.scene = Game.START_ONE
        while self.running:
            self.process_input()     
            self.update()     
            self.render()
            #print(f"{self.game_mode}")
            
            pygame.display.update()
            self.clock.tick(FPS)

        pygame.quit()


# Let's do this!
if __name__ == "__main__":
   g = Game()
   g.run()
