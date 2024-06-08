import pygame
import math

GRID_SIZE_IN_PIXELS = 15

def snap(number, to):
    return math.floor(number / to + 0.5) * to

def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    direction = ""
    speed = 0

    delta = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(player_pos.x, player_pos.y, GRID_SIZE_IN_PIXELS, GRID_SIZE_IN_PIXELS))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            direction = "y"
            player_pos.x = snap(player_pos.x, GRID_SIZE_IN_PIXELS)
            speed = -GRID_SIZE_IN_PIXELS
        elif keys[pygame.K_s]:
            direction = "y"
            player_pos.x = snap(player_pos.x, GRID_SIZE_IN_PIXELS)
            speed = GRID_SIZE_IN_PIXELS
        elif keys[pygame.K_a]:
            direction = "x"
            player_pos.y = snap(player_pos.y, GRID_SIZE_IN_PIXELS)
            speed = -GRID_SIZE_IN_PIXELS
        elif keys[pygame.K_d]:
            direction = "x"
            player_pos.y = snap(player_pos.y, GRID_SIZE_IN_PIXELS)
            speed = GRID_SIZE_IN_PIXELS

        if direction == "x":
            player_pos.x += speed*delta/1000
        elif direction == "y":
            player_pos.y += speed*delta/1000

        pygame.display.flip()
        delta = clock.tick()

    pygame.quit()

if __name__ == "__main__":
    main()