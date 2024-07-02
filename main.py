import pygame
from random import randint
from collections import deque
from enum import Enum
from math import floor


class Direction(Enum):
    X = 1
    Y = 2


DEBUG = True

GRID_SIZE = 10

SNAKE_SPEED = 5


def snap(square, to):
    return (square // to) * to


def clamp_into_grid(square):
    return min(max(square, 0), GRID_SIZE - 1)


def random_square():
    return randint(0, GRID_SIZE - 1)


def main():
    pygame.init()

    screen = pygame.display.set_mode((15 * GRID_SIZE, 15 * GRID_SIZE), pygame.RESIZABLE)
    square_pixel_size = min(screen.get_size()) / GRID_SIZE

    def snap_to_grid(number):
        return snap(number, square_pixel_size)

    player_position = {Direction.X: GRID_SIZE / 2, Direction.Y: GRID_SIZE / 2}
    direction = None
    speed = 0

    snake_squares = deque()
    snake_length = 1

    apple_position = (
        random_square(),
        random_square(),
    )

    def draw_back_ground():
        background = pygame.Surface(screen.get_size())
        background.fill((0, 0, 70))
        pygame.draw.rect(
            background,
            (20, 20, 20),
            pygame.Rect(
                0,
                0,
                GRID_SIZE * square_pixel_size,
                GRID_SIZE * square_pixel_size,
            ),
        )
        return background

    background = draw_back_ground()

    clock = pygame.time.Clock()
    delta = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                square_pixel_size = min(screen.get_size()) / GRID_SIZE
                background = draw_back_ground()

        if (
            floor(player_position[Direction.X]) == apple_position[0]
            and floor(player_position[Direction.Y]) == apple_position[1]
        ):
            apple_position = (
                random_square(),
                random_square(),
            )
            snake_length += 1

        if len(snake_squares) > snake_length:
            snake_squares.popleft()

        if (
            len(snake_squares) == 0
            or snake_squares[-1][0] != floor(player_position[Direction.X])
            or snake_squares[-1][1] != floor(player_position[Direction.Y])
        ):
            snake_squares.append(
                (
                    floor(player_position[Direction.X]),
                    floor(player_position[Direction.Y]),
                )
            )

        screen.blit(background, background.get_rect())

        for i, (x, y) in enumerate(snake_squares):
            pygame.draw.rect(
                screen,
                (0, 100 + (i + 1) / len(snake_squares) * 155, 0),
                pygame.Rect(
                    x * square_pixel_size,
                    y * square_pixel_size,
                    square_pixel_size,
                    square_pixel_size,
                ),
            )

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

        if DEBUG:
            pygame.draw.rect(
                screen,
                (20, 90, 50),
                pygame.Rect(
                    (player_position[Direction.X] * square_pixel_size),
                    (player_position[Direction.Y] * square_pixel_size),
                    square_pixel_size,
                    square_pixel_size,
                ),
            )

        keys = pygame.key.get_pressed()
        # TODO: prioritise latest key press
        if keys[pygame.K_w]:
            if direction != Direction.Y:
                direction = Direction.Y
                speed = -SNAKE_SPEED
        elif keys[pygame.K_s]:
            if direction != Direction.Y:
                direction = Direction.Y
                speed = SNAKE_SPEED
        elif keys[pygame.K_a]:
            if direction != Direction.X:
                direction = Direction.X
                speed = -SNAKE_SPEED
        elif keys[pygame.K_d]:
            if direction != Direction.X:
                direction = Direction.X
                speed = SNAKE_SPEED

        if direction == Direction.X:
            player_position[Direction.X] = clamp_into_grid(
                player_position[Direction.X] + (speed * delta / 1000)
            )
        elif direction == Direction.Y:
            player_position[Direction.Y] = clamp_into_grid(
                player_position[Direction.Y] + (speed * delta / 1000)
            )

        pygame.display.flip()
        delta = clock.tick()

    pygame.quit()


if __name__ == "__main__":
    main()
