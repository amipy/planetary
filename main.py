import random

import pygame as pygame

from planet import Planet as planet

screen = (500, 500)
disp = pygame.display.set_mode(screen)
disp.fill((0, 0, 0))
pygame.display.update()

#initialie planets
#planet format is as follows: [postion, inital velocity, mass]
planets=[
    planet([screen[0] // 2, screen[1] // 2], [0, 0], 1000),
    planet([screen[0] // 2 - 100, screen[1] // 2], [0, -3], 10),
    planet([screen[0] // 2 + 100, screen[1] // 2], [0, 3], 10),
    planet([screen[0] // 2 - 150, screen[1] // 2], [0, -2], 10),
    planet([screen[0] // 2 + 250, screen[1] // 2], [0, 2], 10),
]
#sun = planet([screen[0] // 2, screen[1] // 2], [0, 0], 10)
#earth = planet([screen[0] // 2 - 10, screen[1] // 2 + 100], [0, -1], 10)
clock = pygame.time.Clock()
#planets=[planet([random.randint(0,screen[0]), random.randint(0,screen[1])], [0,0], random.randint(1,100)) for i in range(20)]


dt = 0
timeScale=25
running = True
#main loop
while running:
    disp.fill((0, 0, 0))
    #calculate planets
    for i in planets:
        a = [0, 0]
        for j in planets:
            if i != j:
                if planet.distance2(i, j) < ((i.mass ** (1 / 3)) + (j.mass ** (1 / 3)))**2:
                    sum_mass = i.mass + j.mass
                    i.velocity[0] = i.velocity[0]*i.mass/sum_mass + j.velocity[0]*j.mass/sum_mass
                    i.velocity[1] = i.velocity[1]*i.mass/sum_mass + j.velocity[1]*j.mass/sum_mass
                    i.position[0] = (i.position[0]+j.position[0])/2
                    i.position[1] = (i.position[1]+j.position[1])/2
                    i.mass = sum_mass
                    planets.remove(j)
                    continue
                x,y=planet.calcGravityForce(i,j)
                a[0]+=x
                a[1]+=y
        i.proccessVel(a, dt/timeScale)
        i.proccessMove(dt/timeScale)
        pygame.draw.circle(disp, (255, 255, 255), i.position, i.mass ** (1 / 3))

    #a = planet.calcGravityForce(earth, sun)
    #earth.proccessVel(a, dt/50)
    #earth.proccessMove(dt/50)

    #a = planet.calcGravityForce(sun, earth)
    #sun.proccessVel(a, dt/50)
    #sun.proccessMove(dt/50)

    #pygame.draw.circle(disp, (255, 255, 255), sun.position, sun.mass ** (1 / 3))
    #pygame.draw.circle(disp, (255, 255, 255), earth.position, earth.mass ** (1 / 3))
    pygame.display.update()
    #no event supprt yet; will add later.
    pygame.event.pump()

    dt = clock.tick(60)
