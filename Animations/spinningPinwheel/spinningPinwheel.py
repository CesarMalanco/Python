# Author: reDragonCoder

import pygame
import sys
import itertools

def rainbow_colors():
    colors=[
        (255, 0, 0), # red
        (255, 165, 0), # orange
        (255, 255, 0), # yellow
        (0, 255, 0), # green
        (0, 0, 255), # blue
        (75, 0, 130), # purple
        (238, 130, 238), # pink
    ]
    return itertools.cycle(colors)

def render_rainbow_text(surface, text, font, start_pos):
    x, y=start_pos
    colors=rainbow_colors()

    for char in text:
        char_surface=font.render(char, True, next(colors))
        surface.blit(char_surface, (x, y))
        x+=char_surface.get_width()

pygame.init()

width, height=800, 600
screen=pygame.display.set_mode((width, height))
pygame.display.set_caption("Spinning Pinwheel")

new_icon=pygame.image.load('pinwheel.png')
pygame.display.set_icon(new_icon)


pinwheel_image=pygame.image.load('pinwheel.png')
pinwheel_image=pygame.transform.scale(pinwheel_image, (350, 350)) 
pinwheel_rect=pinwheel_image.get_rect(center=(width // 2, height // 2))

angle=0
rotation_speed=1
max_rotation_speed=20

font=pygame.font.Font('corinto.ttf', 36)
text_color=(255, 255, 255)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.MOUSEBUTTONDOWN:
            if pinwheel_rect.collidepoint(event.pos):
                rotation_speed+=1
                if rotation_speed>max_rotation_speed:
                    rotation_speed=1
    
    angle+=rotation_speed
    if angle>=360:
        angle=0
    
    rotated_pinwheel=pygame.transform.rotate(pinwheel_image, angle)
    rotated_rect=rotated_pinwheel.get_rect(center=pinwheel_rect.center)
    
    screen.fill((0, 0, 0))
    screen.blit(rotated_pinwheel, rotated_rect.topleft)

    render_rainbow_text(screen, "Click to increase speed", font, (200, 30))

    pygame.display.flip() 

    pygame.time.Clock().tick(60)
