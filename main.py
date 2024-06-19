import pygame
import math
from random import randint

GRID_SIZE_IN_PIXELS = 15


def snap(number, to):
    return math.floor(number / to + 0.5) * to


def main():
    pygame.init()
    screen = pygame.display.set_mode(
        (GRID_SIZE_IN_PIXELS * 50, GRID_SIZE_IN_PIXELS * 50)
    )
    clock = pygame.time.Clock()
    running = True
    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    direction = ""
    speed = 0

    delta = 0

    snake_position = []

    apple_position = (
        snap(randint(0, screen.get_width()), GRID_SIZE_IN_PIXELS),
        snap(randint(0, screen.get_height()), GRID_SIZE_IN_PIXELS),
    )

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        pygame.draw.rect(
            screen,
            (240, 0, 0),
            pygame.Rect(
                apple_position[0],
                apple_position[1],
                GRID_SIZE_IN_PIXELS,
                GRID_SIZE_IN_PIXELS,
            ),
        )
        pygame.draw.rect(
            screen,
            (0, 125, 0),
            pygame.Rect(
                player_pos.x, player_pos.y, GRID_SIZE_IN_PIXELS, GRID_SIZE_IN_PIXELS
            ),
        )
        snake_position.append(
            (
                snap(player_pos.x, GRID_SIZE_IN_PIXELS),
                snap(player_pos.y, GRID_SIZE_IN_PIXELS),
            )
        )
        for x, y in snake_position:
            pygame.draw.rect(
                screen,
                (0, 255, 0),
                pygame.Rect(x, y, GRID_SIZE_IN_PIXELS, GRID_SIZE_IN_PIXELS),
            )

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
            player_pos.x += speed * delta / 1000
        elif direction == "y":
            player_pos.y += speed * delta / 1000

        pygame.display.flip()
        delta = clock.tick()

    pygame.quit()


if __name__ == "__main__":
    main()
