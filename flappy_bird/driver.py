import random

import pygame

from flappy_bird import box, game_constants

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()

game_display = pygame.display.set_mode(
    (game_constants.DISPLAY_WIDTH, game_constants.DISPLAY_HEIGHT)
)
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

flappy_box = box.Box(
    game_constants.DISPLAY_WIDTH * 0.25, game_constants.DISPLAY_HEIGHT * 0.25
)

delta_x = -15
wall_x_positions = [x for x in range(game_constants.DISPLAY_WIDTH, 0, delta_x)]
current_wall_position = 0
top_wall_lengths = [x for x in range(50, 260, 30)]
bottom_wall_lengths = [x for x in range(260, 50, -30)]
index = random.randint(0, len(top_wall_lengths) - 1)
top_wall_length, bottom_wall_length = (
    top_wall_lengths[index],
    bottom_wall_lengths[index],
)

score = 0
while True:
    for event in pygame.event.get():
        # If space down, make the box jump
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            flappy_box.jump()

    game_display.fill(WHITE)

    # Draw the floor
    floor = pygame.draw.rect(
        game_display,
        BLACK,
        pygame.Rect(
            (0, game_constants.DISPLAY_HEIGHT * 0.92),
            (game_constants.DISPLAY_WIDTH, 50),
        ),
    )

    # Draw the walls
    top_wall = pygame.Rect(
        (wall_x_positions[current_wall_position], 0), (20, top_wall_length)
    )
    top_wall = pygame.draw.rect(game_display, BLACK, top_wall)

    bottom_wall_start = (
        game_constants.DISPLAY_HEIGHT - floor.height - bottom_wall_length
    )  # Top of bottom wall
    bottom_wall = pygame.Rect(
        (wall_x_positions[current_wall_position], bottom_wall_start),
        (20, bottom_wall_length),
    )
    bottom_wall = pygame.draw.rect(game_display, BLACK, bottom_wall)

    # Update flappy box
    flappy_box.update_position(game_display)
    flappy_box.increment_time()

    # Check for collision with floor + walls
    if flappy_box.rect.colliderect(floor):
        pygame.quit()
        print("SCORE: ", score)
    elif flappy_box.rect.colliderect(top_wall) or flappy_box.rect.colliderect(
        bottom_wall
    ):
        pygame.quit()
        print("SCORE: ", score)

    # If walls at end of screen, create new walls
    current_wall_position += 1
    if current_wall_position > len(wall_x_positions) - 1:
        index = random.randint(0, len(top_wall_lengths) - 1)
        top_wall_length, bottom_wall_length = (
            top_wall_lengths[index],
            bottom_wall_lengths[index],
        )

    current_wall_position = current_wall_position % len(wall_x_positions)

    # Update graphics + advance 1 frame
    pygame.display.update()
    clock.tick(game_constants.FRAMES_PER_SECOND)
    score += 1

pygame.quit()
quit()
