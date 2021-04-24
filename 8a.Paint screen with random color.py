import pygame
import random



pygame.init()
win = pygame.display.set_mode((800,560))
pygame.display.set_caption('Paint screen with random colors')


w=20
h=20
run = True
while run:

    
    
    for event in pygame.event.get():
        #print (event)
        if event.type == pygame.QUIT:
            run = False

    for y in range(0,560,w):
        for x in range(0,800,h):
            pygame.time.delay(8)
            pygame.draw.rect(win, (random.randrange(226),random.randrange(226),random.randrange(226)), (x,y,w,h))
            pygame.display.update()

    win.fill((0,0,0))

pygame.quit()
