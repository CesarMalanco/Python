# Author: reDragonCoder

import pygame
import sys

pygame.init()
pygame.mixer.init()

width, height=800, 600
screen=pygame.display.set_mode((width, height))
pygame.display.set_caption("Spinning Spongebob")

new_icon=pygame.image.load('pinapple.png')
pygame.display.set_icon(new_icon)

background=pygame.image.load('background.jpg')
background=pygame.transform.scale(background, (width, height))

spongebob_image1=pygame.image.load('spongebob1.png')
spongebob_image1=pygame.transform.scale(spongebob_image1, (370, 300))
spongebob_image2=pygame.image.load('spongebob2.png') 
spongebob_image2=pygame.transform.scale(spongebob_image2, (350, 350))

spongebob_rect1=spongebob_image1.get_rect(center=(width // 2, height // 2))
spongebob_rect2=spongebob_image2.get_rect(center=(width // 2, height // 2))


angle=0
rotation_speed=1
max_rotation_speed=20

font=pygame.font.Font('bikiniBottom.ttf', 50)
text_color=(0, 0, 0)

pygame.mixer.music.load('bikiniBottomMP3.mp3')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

change_image_sound=pygame.mixer.Sound('cryingMP3.mp3')
change_image_sound.set_volume(1.0)
image_changed=False

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.MOUSEBUTTONDOWN:
            if spongebob_rect1.collidepoint(event.pos) or spongebob_rect2.collidepoint(event.pos):
                rotation_speed+=1
                if rotation_speed>max_rotation_speed:
                    rotation_speed=1
    
    angle+=rotation_speed
    if angle>=360:
        angle=0

    if 10<=rotation_speed<=20:
        rotated_spongebob=pygame.transform.rotate(spongebob_image2, angle)
        rotated_rect=rotated_spongebob.get_rect(center=spongebob_rect2.center)
        if not image_changed:
            change_image_sound.play()
            image_changed=True
    else:
        rotated_spongebob=pygame.transform.rotate(spongebob_image1, angle)
        rotated_rect=rotated_spongebob.get_rect(center=spongebob_rect1.center)
        image_changed=False

    screen.blit(background, (0, 0))
    screen.blit(rotated_spongebob, rotated_rect.topleft)

    text=font.render("Click to increase speed", True, text_color)
    screen.blit(text, (120, 20))

    pygame.display.flip() 

    pygame.time.Clock().tick(60)
