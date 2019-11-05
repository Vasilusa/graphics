import pygame
import sys
import math

size = width, height = 800, 600

black = 0, 0, 0


def main():
    pygame.init()
    screen = pygame.display.set_mode(size)
    dt = 0.3
    dx1, dy1 = 2, 1
    x1, y1 = 0, 0
    dx2, dy2 = -1, 5
    x2, y2 = 0, 0
    dx3, dy3 = 3, 4
    x3, y3 = 0, 0
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
        screen.fill(black)

        if x1 + width / 2 >= width or x1 + width / 2 < 0:
            dx1 = -dx1
        if y1 + height / 2 >= height or y1 + height / 2 < 0:
            dy1 = -dy1
        x1 += dx1 * dt
        y1 += dy1 * dt

        if x2 + width / 2 >= width or x2 + width / 2 < 0:
            dx2 = -dx2
        if y2 + height / 2 >= height or y2 + height / 2 < 0:
            dy2 = -dy2
        x2 += dx2 * dt
        y2 += dy2 * dt

        if x3 + width / 2 >= width or x3 + width / 2 < 0:
            dx3 = -dx3
        if y3 + height / 2 >= height or y3 + height / 2 < 0:
            dy3 = -dy3
        x3 += dx3 * dt
        y3 += dy3 * dt

        if (x2-x1) * (x3 - x1) + (y2-y1) * (y3 - y1) > 0:
            color1 = (155, 155, 0)
        else:
            color1 = (155, 0, 0)

        pygame.draw.circle(screen, (128, 128, 128), (int(width / 2 - x1), int(height / 2 + y1)), 5, 0)
        pygame.draw.circle(screen, color1, (int(width / 2 - x2), int(height / 2 + y2)), 5, 0)
        pygame.draw.circle(screen, (0, 0, 155), (int(width / 2 - x3), int(height / 2 + y3)), 5, 0)
        pygame.draw.line(screen, (128, 128, 128), (int(width / 2 - x1), int(height / 2 + y1)),
                         (int(width / 2 - x2), int(height / 2 + y2)))
        pygame.draw.line(screen, (128, 128, 128), (int(width / 2 - x1), int(height / 2 + y1)),
                         (int(width / 2 - x3), int(height / 2 + y3)))

        pygame.display.flip()
        pygame.time.wait(10)
    sys.exit(0)


if __name__ == '__main__':
    main()
