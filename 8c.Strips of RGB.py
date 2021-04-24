import pygame
import random



pygame.init()
win = pygame.display.set_mode((675,600))
pygame.display.set_caption('Strips of shades of RGB')



run = True
while run:

    
    
    for event in pygame.event.get():
        #print (event)
        if event.type == pygame.QUIT:
            run = False

    #red stirp
    for x in range(0,226):
        pygame.time.delay(5)
        pygame.draw.rect(win, (x,0,0),(3*x, 0, 3, 200))
        pygame.display.update()

    #green strip
    for x in range(225,-1,-1):
        pygame.time.delay(5)
        pygame.draw.rect(win, (0,x,0),(3*x, 200, 3, 200))
        pygame.display.update()

    #blue strip
    for x in range(0,226):
        pygame.time.delay(5)
        pygame.draw.rect(win, (0,0,x),(3*x, 400, 3, 200))
        pygame.display.update()
        
    win.fill((random.randrange(0,256),random.randrange(0,256),random.randrange(0,256)))

pygame.quit()
