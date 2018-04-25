import pygame
import Camera
import GameConstants
import BoxClass

pygame.init()

entities = []
#camera = Camera(*blah*, display_width, display_height)

game_display = pygame.display.set_mode((GameConstants.DISPLAY_WIDTH, GameConstants.DISPLAY_HEIGHT))
pygame.display.set_caption('Flappy Bird')
clock = pygame.time.Clock()

box = BoxClass.Box(GameConstants.DISPLAY_WIDTH * 0.25, GameConstants.DISPLAY_HEIGHT * 0.25)
#entities.append(box_image)

crashed = False
while not crashed:

    for event in pygame.event.get():

        # If space down, make the box jump
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            box.jump()

    game_display.fill(GameConstants.WHITE)
    box.update_position(game_display)

    box.increment_time()
    pygame.display.update()
    clock.tick(GameConstants.FRAMES_PER_SECOND)

    # for e in entities:
        # game_display.blit(e.image, camera.apply(e))

pygame.quit()
quit()