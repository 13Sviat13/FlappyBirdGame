import pygame, sys
from bird_and_score import BirdAnimator, ScoreManager
from game_strategy import GraphicsManager, GameStrategy
from pipe import Pipe, PipeFactory, PipeComposite

pygame.mixer.pre_init(frequency=44100, size=16, channels=1, buffer=512)
pygame.init()
screen = pygame.display.set_mode((576, 1024))
clock = pygame.time.Clock()
game_font = pygame.font.Font('04B_19.ttf', 40)

# Game Variables
gravity = 0.25
bird_movement = 0
game_active = True
score = 0
high_score = 0

bg_surface = pygame.image.load('assets/background-day.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)

floor_surface = pygame.image.load('assets/base.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0

bird_downflap = pygame.transform.scale2x(pygame.image.load('assets/bluebird-downflap.png').convert_alpha())
bird_midflap = pygame.transform.scale2x(pygame.image.load('assets/bluebird-midflap.png').convert_alpha())
bird_upflap = pygame.transform.scale2x(pygame.image.load('assets/bluebird-upflap.png').convert_alpha())
bird_frames = [bird_downflap, bird_midflap, bird_upflap]
bird_index = 0
bird_surface = bird_frames[bird_index]
bird_rect = bird_surface.get_rect(center=(100, 512))




BIRDFLAP = pygame.USEREVENT + 1
pygame.time.set_timer(BIRDFLAP, 200)


pipe_surface = pygame.image.load('assets/pipe-green.png')
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)
pipe_height = [400, 600, 800]

game_over_surface = pygame.transform.scale2x(pygame.image.load('assets/message.png').convert_alpha())
game_over_rect = game_over_surface.get_rect(center=(288, 512))

flap_sound = pygame.mixer.Sound('sound/sfx_wing.wav')
death_sound = pygame.mixer.Sound('sound/sfx_hit.wav')
score_sound = pygame.mixer.Sound('sound/sfx_point.wav')
score_sound_countdown = 100



bird_animator = BirdAnimator(bird_frames, bird_index)
pipe_factory = PipeFactory()
pipe_composite = PipeComposite(pipe_surface)
game_strategy = GameStrategy(bird_rect, death_sound)
graphics_manager = GraphicsManager(screen)
score_manager = ScoreManager(0, 0, game_font, screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement -= 12
                flap_sound.play()
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                pipe_composite.pipes.clear()
                bird_rect.center = (100, 512)
                bird_movement = 0
                score = 0
                score_manager.reset_score()
                game_strategy.game_active = True  # Reset game_active in GameStrategy

        if event.type == SPAWNPIPE:
            new_pipe = pipe_factory.create_pipe((400, 800), (50, 100))  # Assuming gap range is for top pipe position
            pipe_composite.add_pipe(new_pipe)

        if event.type == BIRDFLAP:
            bird_surface = bird_animator.bird_animation()
            bird_rect = bird_surface.get_rect(center=(100, bird_rect.centery))
            rotated_bird = bird_animator.rotate_bird(bird_surface, bird_movement)
            screen.blit(rotated_bird, bird_rect)

    screen.blit(bg_surface, (0, 0))

    if game_active:
        # Bird
        bird_movement += gravity
        bird_surface = bird_animator.bird_animation()
        bird_rect = bird_surface.get_rect(center=(100, bird_rect.centery))
        rotated_bird = bird_animator.rotate_bird(bird_surface, bird_movement)
        bird_rect.centery += bird_movement
        screen.blit(rotated_bird, bird_rect)

        # Pipes
        pipe_composite.move_pipes()
        pipe_composite.remove_pipes()
        pipe_composite.draw_pipes(pipe_surface, screen)

        #Collosion
        game_active = game_strategy.check_collision(bird_rect, death_sound, pipe_composite.pipes)
        print("Game active:", game_active)

        score += 0.01
        score_manager.update_score(score)
        score_manager.display_score('main_game', screen)
        score_sound_countdown -= 1
        if score_sound_countdown <= 0:
            score_sound.play()
            score_sound_countdown = 100
    else:
        screen.blit(game_over_surface, game_over_rect)
        score_manager.display_score('game_over', screen)

    # Floor
    floor_x_pos -= 1
    graphics_manager.draw_floor()
    if floor_x_pos <= -576:
        floor_x_pos = 0

    pygame.display.update()
    clock.tick(120)