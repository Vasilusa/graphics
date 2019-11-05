import pygame
import sys
import math

size = width, height = 800, 600

black = 0, 0, 0


def main():
    pygame.init()
    screen = pygame.display.set_mode(size)
    game_over = False

    t = 0
    w11 = 3
    w12 = 5
    w21 = 4
    w22 = 7
    w31 = 2
    w32 = 11
    w41 = 1
    w42 = 3
    r = 100

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
        screen.fill(black)

        t += 0.001
        x1 = math.sin(w11 * t + 6) * r
        y1 = math.sin(w12 * t + 6) * r
        y2 = math.sin(w21 * t + 2) * r
        x2 = math.sin(w22 * t + 2) * r
        y3 = math.sin(w31 * t + 3) * r
        x3 = math.sin(w32 * t + 3) * r
        x4 = math.sin(w41 * t + 4) * r
        y4 = math.sin(w42 * t + 4) * r
        k1 = (y1 - y2) / (x1 - x2)
        c1 = (x1 * y2 - x2 * y1) / (x1 - x2)
        k2 = (y3 - y4) / (x3 - x4)
        c2 = (x3 * y4 - x4 * y3) / (x3 - x4)
        a = (c2 - c1) / (k1 - k2)
        b = (k1 * c2 - k2 * c1) / (k1 - k2)
        x_min = -width/2
        x_max = width/2
        y1_left = k1*x_min + c1
        y1_right = k1*x_max + c1
        y2_left = k2 * x_min + c2
        y2_right = k2 * x_max + c2
        pygame.draw.circle(screen, (0, 155, 0), (int(width / 2 + x1), int(height / 2 - y1)), 5, 0)
        pygame.draw.circle(screen, (0, 155, 0), (int(width / 2 + x2), int(height / 2 - y2)), 5, 0)
        pygame.draw.circle(screen, (0, 155, 0), (int(width / 2 + x3), int(height / 2 - y3)), 5, 0)
        pygame.draw.circle(screen, (0, 155, 0), (int(width / 2 + x4), int(height / 2 - y4)), 5, 0)
        pygame.draw.circle(screen, (155, 155, 0), (int(width / 2 + a), int(height / 2 - b)), 5, 0)
        pygame.draw.line(screen, (128, 128, 128), (0, int(height / 2 - y1_left)),
                         (width, height / 2 - y1_right), 1)
        pygame.draw.line(screen, (128, 128, 128), (0, int(height / 2 - y2_left)),
                         (width, height / 2 - y2_right), 1)
        pygame.draw.line(screen, (0, 228, 228), (int(width / 2 + x1), int(height / 2 - y1)),
                         (int(width / 2 + x2), int(height / 2 - y2)), 1)
        pygame.draw.line(screen, (228, 0, 228), (int(width / 2 + x3), int(height / 2 - y3)),
                         (int(width / 2 + x4), int(height / 2 - y4)), 1)
        pygame.display.flip()
        pygame.time.wait(10)
    sys.exit(0)


if __name__ == '__main__':
    main()
