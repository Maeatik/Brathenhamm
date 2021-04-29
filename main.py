import pygame
import math
import random


def generatePolygon(ctrX, ctrY, aveRadius, irregularity, spikeyness, numVerts):
    irregularity = clip(irregularity, 0, 1) * 2 * math.pi / numVerts
    spikeyness = clip(spikeyness, 0, 1) * aveRadius
    angleSteps = []
    lower = (2 * math.pi / numVerts) - irregularity
    upper = (2 * math.pi / numVerts) + irregularity
    sum = 0
    for i in range(numVerts):
        tmp = random.uniform(lower, upper)
        angleSteps.append(tmp)
        sum = sum + tmp

    k = sum / (2 * math.pi)
    for i in range(numVerts):
        angleSteps[i] = angleSteps[i] / k

    points = []
    angle = random.uniform(0, 2 * math.pi)
    for i in range(numVerts):
        r_i = clip(random.gauss(aveRadius, spikeyness), 0, 2 * aveRadius)
        x = ctrX + r_i * math.cos(angle)
        y = ctrY + r_i * math.sin(angle)
        points.append((int(x), int(y)))

        angle = angle + angleSteps[i]

    return points


def clip(x, min, max):
    if (min > max):
        return x
    elif (x < min):
        return min
    elif (x > max):
        return max
    else:
        return x


def paintingPoly():
    window.fill(white)
    pygame.display.update()
    irr = round(random.uniform(0, 1.0), 1)
    spikey = round(random.uniform(0, 0.4), 1)
    num = random.randint(3, 8)
    print("-----\n" + str(irr) + " " + str(spikey))
    pygame.draw.aalines(window, black, True, generatePolygon(300, 300, 100, irr, spikey, num))
    pygame.display.update()


def painting():
    text()
    for x in range(window.get_height()):
        check = False
        for y in range(window.get_width()):
            if (x < 470):
                color = window.get_at([y, x])
                if y > 1:
                    prePix = window.get_at([y - 1, x])
                else:
                    prePix = color

                if ((color != (255, 255, 255, 255)) & (color != (255, 0, 0, 255))) or (
                        (prePix != (255, 255, 255, 255)) & (prePix != (255, 0, 0, 255))):
                    if not check:
                        l = y
                        check = True
                    else:
                        pygame.draw.line(window, red, [l, x], [y, x])

                    pygame.display.update()
                    clock.tick(FPS)


def text():
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render('Пробел - создание нового многоугольника и закраска', True, black)
    text2 = font.render('LAlt - перезарядка пробела', True, black)
    textRect = text.get_rect()
    textRect2 = text2.get_rect()
    # set the center of the rectangular object.
    textRect.center = (300, 500)
    textRect2.center = (300, 525)
    window.blit(text, textRect)
    window.blit(text2, textRect2)
    pygame.display.update()


def func():
    paintingPoly()
    painting()


if __name__ == '__main__':

    flag = True
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0, 255)
    FPS = 288
    clock = pygame.time.Clock()
    RUN = True

    window = pygame.display.set_mode((600, 600))
    window.fill(white)
    pygame.display.set_caption('Закрашивание фигуры')
    pygame.init()

    func()

    while RUN:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] & flag:
            flag = False
            func()

        if keys[pygame.K_LALT]:
            flag = True

    pygame.quit()
