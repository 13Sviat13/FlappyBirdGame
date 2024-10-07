import pygame
# Import the necessary module: pygame for game development

class BirdAnimator:
    # Define a new class called BirdAnimator
    def __init__(self, bird_frames, bird_index):
        # Initialize a new BirdAnimator object with bird frames and an index
        self.bird_frames = bird_frames  # Store the bird frames
        self.bird_index = bird_index  # Store the current bird index

    def bird_animation(self):
        # Animate the bird by cycling through the frames
        self.bird_index += 1  # Increment the bird index
        if self.bird_index >= len(self.bird_frames):
            self.bird_index = 0  # Reset the index if it reaches the end of the frames
        return self.bird_frames[self.bird_index]  # Return the current bird frame

    def rotate_bird(self, bird_surface, bird_movement):
        # Rotate the bird surface based on the bird movement
        return pygame.transform.rotozoom(bird_surface, -bird_movement * 3, 1)  # Rotate and zoom the bird surface

class ScoreManager:
    # Define a new class called ScoreManager
    def __init__(self, score, high_score, game_font, screen):
        # Initialize a new ScoreManager object with a score, high score, game font, and screen
        self.score = score  # Store the current score
        self.high_score = high_score  # Store the high score
        self.game_font = game_font  # Store the game font
        self.screen = screen  # Store the screen

    def display_score(self, game_state, screen):
        # Display the score on the screen based on the game state
        if game_state == 'main_game':
            score_surface = self.game_font.render(str(int(self.score)), True, (255, 255, 255))  # Render the score as a surface
            score_rect = score_surface.get_rect(center=(288, 100))  # Get the rectangle for the score surface
            screen.blit(score_surface, score_rect)  # Blit the score surface onto the screen
        if game_state == 'game_over':
            score_surface = self.game_font.render(f'Score: {int(self.score)}', True, (255, 255, 255))  # Render the score as a surface with a label
            score_rect = score_surface.get_rect(center=(288, 100))  # Get the rectangle for the score surface
            screen.blit(score_surface, score_rect)  # Blit the score surface onto the screen

            high_score_surface = self.game_font.render(f'High score: {int(self.high_score)}', True, (255, 255, 255))  # Render the high score as a surface with a label
            high_score_rect = high_score_surface.get_rect(center=(288, 850))  # Get the rectangle for the high score surface
            screen.blit(high_score_surface, high_score_rect)  # Blit the high score surface onto the screen

    def update_score(self, new_score):
        # Update the score and high score if necessary
        if new_score > self.high_score:
            self.high_score = new_score  # Update the high score if the new score is higher
        self.score = new_score  # Update the current score

    def reset_score(self):
        # Reset the score to 0
        self.score = 0