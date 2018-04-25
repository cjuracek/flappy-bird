import pygame
import Camera
import GameConstants
import BoxClass
# import Box

pygame.init()

entities = []
#camera = Camera(*blah*, display_width, display_height)

game_display = pygame.display.set_mode((GameConstants.DISPLAY_WIDTH, GameConstants.DISPLAY_HEIGHT))
pygame.display.set_caption('Flappy Bird')
clock = pygame.time.Clock()

# box_image = pygame.image.load('BlackBox.jpg')
box = BoxClass.Box(GameConstants.DISPLAY_WIDTH * 0.25, GameConstants.DISPLAY_HEIGHT * 0.25)
#entities.append(box_image)

# game_display.blit(box.rect, (box.x_pos, box.y_pos))
# box.draw(game_display)
# pygame.display.update()

crashed = False
while not crashed:

    for event in pygame.event.get():

        # If space down, make the box jump
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            print('SPACE WAS PRESSED')
            box.jump()

    game_display.fill(GameConstants.WHITE)
    box.update_position(game_display)
    game_display.blit(box.box_image, (box.x_pos, box.y_pos))

    #for e in entities:
        #game_display.blit(e.image, camera.apply(e))

    box.increment_time()
    # game_display.blit(box.rect, (box.x_pos, box.curr_y_pos))
    pygame.display.update()
    clock.tick(GameConstants.FRAMES_PER_SECOND)

pygame.quit()
quit()