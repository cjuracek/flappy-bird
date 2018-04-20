import GameConstants
import pygame

class Box(object):

    def __init__(self, x, y):
        self.x_pos = x
        self.initial_y_pos = y
        self.curr_y_pos = y

        self.time_since_last_jump = 0.0
        self.jump_velocity = 50

        # Collision/movement via this rectangle
        self.rect = pygame.Rect(50, 50, 50, 50)



    # Update y position according to 1/2gt^2 + vt + y
    def jump(self):
        self.curr_y_pos = (0.5 * GameConstants.GRAVITY * (self.time_since_last_jump) ** 2) \
                        + (self.jump_velocity * self.time_since_last_jump) \
                        + self.initial_y_pos