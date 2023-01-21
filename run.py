from game import blk
import pygame    

pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("ぬるぬるシミュレーター")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                blk.wPress = True
            if event.key == pygame.K_a:
                blk.aPress = True
            if event.key == pygame.K_s:
                blk.sPress = True
            if event.key == pygame.K_d:
                blk.dPress = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                blk.wPress = False
            if event.key == pygame.K_a:
                blk.aPress = False
            if event.key == pygame.K_s:
                blk.sPress = False
            if event.key == pygame.K_d:
                blk.dPress = False
    screen.fill((173, 216, 230))
    blk.update(screen)
    pygame.display.update()
    

pygame.quit()
