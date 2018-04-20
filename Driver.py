import pygame
import Camera

pygame.init()

display_width = 800
display_height = 600

entities = []
camera = Camera(*blah*, display_width, display_height)


black = (0, 0, 0)
white = (255, 255, 255)

game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Flappy Bird')
clock = pygame.time.Clock()

box_image = pygame.image.load('BlackBox.jpg')
entities.append(box_image)

def box(x, y):
    game_display.blit(box_image, (x, y))

x = display_width * 0.01
y = display_height * 0.25

crashed = False
while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        # If space down, make the box jump
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_SPACE:
                box_image.jump()

    for e in entities:
        game_display.blit(e.image, camera.apply(e))

    pygame.display.update()
    clock.tick(30)

pygame.quit()
quit()