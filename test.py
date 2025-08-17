import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 255, 255), (320, 240), 50, width=2)
    pygame.display.flip()
    clock.tick(60)