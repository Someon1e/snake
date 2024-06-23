import pygame
import math
from random import randint

DEBUG = True

GRID_SIZE = 10


def snap(number, to):
    return math.floor(number / to) * to


def random_square():
    return randint(0, GRID_SIZE)


def main():
    pygame.init()
    screen = pygame.display.set_mode((15 * GRID_SIZE, 15 * GRID_SIZE), pygame.RESIZABLE)
    square_pixel_size = min(screen.get_height(), screen.get_width()) / GRID_SIZE

    def snap_to_grid(number):
        return snap(number, square_pixel_size)

    clock = pygame.time.Clock()
    running = True
    player_position = {"x": GRID_SIZE / 2, "y": GRID_SIZE / 2}

    direction = ""
    speed = 0

    delta = 0

    snake_length = 1
    snake_position = []

    apple_position = (
        random_square(),
        random_square(),
    )

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                # There's some code to add back window content here.
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                square_pixel_size = (
                    min(screen.get_height(), screen.get_width()) / GRID_SIZE
                )

        screen.fill((20, 20, 20))

        pygame.draw.rect(
            screen,
            (240, 0, 0),
            pygame.Rect(
                apple_position[0] * square_pixel_size,
                apple_position[1] * square_pixel_size,
                square_pixel_size,
                square_pixel_size,
            ),
        )

        if (
            math.floor(player_position["x"]) == apple_position[0]
            and math.floor(player_position["y"]) == apple_position[1]
        ):
            apple_position = (
                random_square(),
                random_square(),
            )
            snake_length += 1

        if len(snake_position) > snake_length:
            snake_position.remove(snake_position[0])

        if (
            len(snake_position) == 0
            or snake_position[len(snake_position) - 1][0]
            != math.floor(player_position["x"])
            or snake_position[len(snake_position) - 1][1]
            != math.floor(player_position["y"])
        ):
            snake_position.append(
                (
                    math.floor(player_position["x"]),
                    math.floor(player_position["y"]),
                )
            )

        for i, (x, y) in enumerate(snake_position):
            pygame.draw.rect(
                screen,
                (0, 100 + (i + 1) / len(snake_position) * 155, 0),
                pygame.Rect(
                    x * square_pixel_size,
                    y * square_pixel_size,
                    square_pixel_size,
                    square_pixel_size,
                ),
            )
        if DEBUG:
            pygame.draw.rect(
                screen,
                (20, 90, 50),
                pygame.Rect(
                    (player_position["x"] * square_pixel_size),
                    (player_position["y"] * square_pixel_size),
                    square_pixel_size,
                    square_pixel_size,
                ),
            )

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            direction = "y"
            speed = -1
        elif keys[pygame.K_s]:
            direction = "y"
            speed = 1
        elif keys[pygame.K_a]:
            direction = "x"
            speed = -1
        elif keys[pygame.K_d]:
            direction = "x"
            speed = 1

        if direction == "x":
            player_position["x"] += speed * delta / 1000
        elif direction == "y":
            player_position["y"] += speed * delta / 1000

        pygame.display.flip()
        delta = clock.tick()

    pygame.quit()


if __name__ == "__main__":
    main()
