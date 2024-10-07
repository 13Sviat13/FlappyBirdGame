import pygame, random
# Import the necessary modules: pygame for game development and random for generating random numbers

class Pipe:
    # Define a new class called Pipe
    def __init__(self, y_pos, gap_range):
        # Initialize a new Pipe object with a y-position and a gap range
        self.y_pos = y_pos  # Store the y-position of the pipe
        self.gap = gap_range[0]  # Store the gap distance from the top of the screen (assuming gap is the top pipe distance)
        self.surface = pygame.image.load('assets/pipe-green.png').convert_alpha()  # Load the pipe image
        self.surface = pygame.transform.scale2x(self.surface)  # Scale the pipe image to twice its size
        self.bottom_rect = self.surface.get_rect(midtop=(700, self.y_pos))  # Create a rectangle for the bottom pipe
        self.top_rect = self.surface.get_rect(midbottom=(700, self.y_pos - self.gap - 300))  # Create a rectangle for the top pipe (adjusted for pipe gap)
        self.centerx = self.bottom_rect.centerx  # Store the center x-coordinate of the pipe

    @property
    def bottom(self):
        # Define a property to get the bottom of the pipe
        return self.bottom_rect.bottom  # Return the bottom of the pipe

class PipeFactory:
    # Define a new class called PipeFactory
    def create_pipe(self, pipe_height_range, gap_range):
        # Create a new pipe with a random y-position within the given range
        random_pipe_pos = random.randrange(*pipe_height_range)  # Generate a random y-position
        return Pipe(random_pipe_pos, gap_range)  # Return a new Pipe object

class PipeComposite:
    # Define a new class called PipeComposite
    def __init__(self, pipe_surface):
        # Initialize a new PipeComposite object with a pipe surface
        self.pipes = []  # Initialize an empty list to store pipes
        self.pipe_surface = pipe_surface  # Store the pipe surface

    def add_pipe(self, pipe):
        # Add a new pipe to the list
        self.pipes.append(pipe)  # Append the pipe to the list

    def move_pipes(self):
        # Move all pipes in the list to the left
        for pipe in self.pipes:
            pipe.bottom_rect.move_ip(-5, 0)  # Move the bottom pipe rectangle to the left
            pipe.top_rect.move_ip(-5, 0)  # Move the top pipe rectangle to the left

    def draw_pipes(self, pipe_surface, screen):
        # Draw all pipes in the list on the screen
        for pipe in self.pipes:
            if pipe.top_rect.bottom >= 0:
                screen.blit(pipe_surface, pipe.top_rect)  # Draw the top pipe if it's visible
            if pipe.bottom_rect.bottom >= 1024:
                screen.blit(pipe_surface, pipe.bottom_rect)  # Draw the bottom pipe if it's visible

    def remove_pipes(self):
        """
        Removes pipes from the list that have moved off-screen (left edge).

        Args:
            pipes: A list of Pipe objects.

        Returns:
            A new list containing the remaining pipes.
        """
        self.pipes = [pipe for pipe in self.pipes if pipe.centerx > -600]  # Remove pipes that have moved off-screen
