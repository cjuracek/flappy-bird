import GameConstants
import pygame


class Box(object):
    def __init__(self, x, y):
        self.box_image = pygame.image.load("BlackBox.jpg")
        self.box_image = pygame.transform.scale(self.box_image, (50, 50))
        self.x_pos, self.y_pos = x, y

        # Jump options
        self.time_since_last_jump = 0.0
        self.jump_velocity = -700
        self.jump_start_y_pos = self.y_pos

        # Collision/movement via this rectangle
        self.rect = pygame.Rect(50, 50, 50, 50)

    def draw(self, surface):
        pygame.draw.rect(surface, GameConstants.BLACK, self.rect)

    # Update y position according to 1/2gt^2 + vt + y
    def jump(self):
        self.time_since_last_jump = 0.0
        self.jump_start_y_pos = self.y_pos

        self.y_pos = (
            (-0.5 * GameConstants.GRAVITY * self.time_since_last_jump**2)
            + (self.jump_velocity * self.time_since_last_jump)
            + self.jump_start_y_pos
        )

        # self.rect.move_ip(self.x_pos, self.y_pos)

    def increment_time(self):
        self.time_since_last_jump += 1 / GameConstants.FRAMES_PER_SECOND

    def update_position(self, surface):
        self.y_pos = (
            (-0.5 * GameConstants.GRAVITY * self.time_since_last_jump**2)
            + (self.jump_velocity * self.time_since_last_jump)
            + self.jump_start_y_pos
        )

        surface.blit(self.box_image, (self.x_pos, self.y_pos))
        self.rect.x, self.rect.y = self.x_pos, self.y_pos
