import pygame
import random



pygame.init()
win = pygame.display.set_mode((800,550))
pygame.display.set_caption('Paint with random colors')


run = True
while run:

    
    
    for event in pygame.event.get():
        #print (event)
        if event.type == pygame.QUIT:
            run = False

    if pygame.mouse.get_pressed()[0]:
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]
        
        
        pygame.draw.circle(win,(random.randrange(226),random.randrange(226),random.randrange(226)),(x,y),8)



        pygame.display.update()


pygame.quit()
