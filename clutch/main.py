import pygame
import sys
import math

size = width, height = 800, 600

black = 0, 0, 0


def main():
    pygame.init()
    screen = pygame.display.set_mode(size)
    t = 0
    dt = 0.8
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
        screen.fill(black)
        t += dt
        n1 = 30
        n2 = 80
        r1 = 50
        r2 = 30 + 60*math.sin(2*math.pi/1000 * t)
        r3 = r1 + r2
        w1 = 0.01
        w2 = w1 * r3 / r2
        w3 = w1
        phi1 = w1 * t * 0
        phi2 = w2 * t
        phi3 = w3 * t

        phi1 -= phi3
        phi2 -= phi3
        phi3 -= phi3

        pygame.draw.circle(screen, (199, 199, 199), (width // 2 + int(r1 * math.cos(phi1)),
                                                     height // 2 - int(r1 * math.sin(phi1))), 10, 0)
        for i in range(n1):
            pygame.draw.circle(screen, (0, 255, 0), (width // 2 + int(r1 * math.cos(phi1))
                                                     + int(r2 * math.cos(((2 * math.pi) / n1) * i + phi2)),
                                                     height // 2 - int(r1 * math.sin(phi1))
                                                     - int(r2 * math.sin(((2 * math.pi) / n1) * i + phi2))), 2, 0)
        for i in range(n2):
            pygame.draw.circle(screen, (199, 0, 0), (width // 2 + int(r3 * math.cos(((2 * math.pi) / n2) *
                                                                                    i + phi3)),
                                                     height // 2 - int(r3 * math.sin(((2 * math.pi) / n2) *
                                                                                     i + phi3))),
                               2, 0)
        pygame.display.flip()
        pygame.time.wait(10)
    sys.exit(0)


if __name__ == '__main__':
    main()
