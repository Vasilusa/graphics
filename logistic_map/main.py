import pygame
import sys

size = width, height = 1000, 600

black = 0, 0, 0


def main():
    pygame.init()
    screen = pygame.display.set_mode(size)

    k0, k1 = 2, 4
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
        screen.fill(black)
        y = 0
        x = 0.5
        k = k0
        while k <= k1:
            x1 = 1 - 1/k
            for _ in range(100):
                x = k * x * (1 - x)

                pygame.draw.rect(screen, (199, 0, 0), ((int(x * width),
                                                        int(y)), (int(1),
                                                                  1)), 1)
            pygame.draw.rect(screen, (0, 199, 0), ((int(x1*width), int(y)), (int(1), 1)), 1)
            y += 1

            k += (k1 - k0) / height
        pygame.display.flip()
        pygame.time.wait(10)
    sys.exit(0)


if __name__ == '__main__':
    main()
