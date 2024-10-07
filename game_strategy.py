import pygame


class GameStrategy:
    # Define a new class called GameStrategy
    def __init__(self,  bird_rect, death_sound):
        # Initialize the GameStrategy object with a bird rectangle and a death sound
        self.game_active = True  # Set the game to be active by default
        self.bird_rect = bird_rect  # Store the bird rectangle
        self.death_sound = death_sound  # Store the death sound

    def check_collision(self, bird_rect, death_sound, pipes):
        # Check for collisions between the bird and the pipes
        for pipe in pipes:
            # Iterate over each pipe in the list
            if bird_rect.colliderect(pipe.bottom_rect) or bird_rect.colliderect(pipe.top_rect):
                # Check if the bird collides with the top or bottom of the pipe
                death_sound.play()  # Play the death sound
                self.game_active = False  # Set the game to be inactive
        if bird_rect.top <= -100 or bird_rect.bottom >= 900:
            # Check if the bird has moved outside the screen boundaries
            self.game_active = False  # Set the game to be inactive
        return self.game_active  # Return the game active status

class GraphicsManager:
    # Define a new class called GraphicsManager
    def __init__(self, screen):
        # Initialize the GraphicsManager object with a screen
        self.screen = screen  # Store the screen
        self.floor_surface = pygame.image.load('assets/base.png').convert()  # Load the floor image
        self.floor_surface = pygame.transform.scale2x(self.floor_surface)  # Scale the floor image to twice its size
        self.floor_x_pos = 0  # Initialize the floor x-position to 0

    def draw_floor(self):
        # Draw the floor on the screen
        self.screen.blit(self.floor_surface, (self.floor_x_pos, 900))  # Draw the floor at the current x-position
        self.screen.blit(self.floor_surface, (self.floor_x_pos + 576, 900))  # Draw another copy of the floor to create a seamless loop
        self.floor_x_pos -= 1  # Move the floor to the left
        if self.floor_x_pos <= -576:
            # Check if the floor has moved off the screen
            self.floor_x_pos = 0  # Reset the floor x-position to 0