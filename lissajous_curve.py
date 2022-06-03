import pygame
import math

pygame.init()

screen = pygame.display.set_mode((1024, 720))
clock = pygame.time.Clock()
run = True

animate = True
a = 1
b = 1
theta = 0
A = 100
B = 100
points = []
center = (screen.get_width()/2, screen.get_height()/2)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_SPACE:
                animate = False
            if event.key == pygame.K_r or event.key == pygame.K_LEFT:
                a += 1
            if event.key == pygame.K_t or event.key == pygame.K_RIGHT and a > 0:
                a -= 1
            if event.key == pygame.K_d or event.key == pygame.K_UP:
                b += 1
            if event.key == pygame.K_f or event.key == pygame.K_DOWN and b > 0:
                b -= 1

    for t in range(2000):  # the more it has the more it's accurate
        points.append([round(A * math.sin(a * t + theta) + center[0]),
                       round(B * math.sin(b * t) + center[1])])

    if animate:
        theta += 0.01
        if theta >= math.pi:
            theta = 0.01
    screen.fill((0, 0, 0))
    for point in points:
        pygame.draw.rect(screen, (0, 125, 255), pygame.Rect(*point, 1, 1))
        points = []
    pygame.display.flip()
    clock.tick(60)
    print(f"{clock.get_fps():.0f} FPS")

pygame.quit()
