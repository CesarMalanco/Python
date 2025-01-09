# Author: reDragonCoder

import pygame
import sys

pygame.init()

width, height=800, 600
screen=pygame.display.set_mode((width, height))
pygame.display.set_caption("Spinning Banana")

new_icon=pygame.image.load('banana.png')
pygame.display.set_icon(new_icon)

banana_image=pygame.image.load('banana.png')
banana_image=pygame.transform.scale(banana_image, (500, 500)) 
banana_rect=banana_image.get_rect(center=(width // 2, height // 2))

angle=0
rotation_speed=1
max_rotation_speed=20

font=pygame.font.Font('funnyCat.ttf', 36)
text_color=(255, 255, 255)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.MOUSEBUTTONDOWN:
            if banana_rect.collidepoint(event.pos):
                rotation_speed+=1
                if rotation_speed>max_rotation_speed:
                    rotation_speed=1
    
    angle+=rotation_speed
    if angle>=360:
        angle=0
    
    rotated_banana=pygame.transform.rotate(banana_image, angle)
    rotated_rect=rotated_banana.get_rect(center=banana_rect.center)
    
    screen.fill((0, 0, 0))
    screen.blit(rotated_banana, rotated_rect.topleft)

    text=font.render("Click to increase speed", True, text_color)
    screen.blit(text, (200, 20))

    pygame.display.flip() 

    pygame.time.Clock().tick(60)
