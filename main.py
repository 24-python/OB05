import pygame
import time
pygame.init()

windows_size = 800, 600
screen = pygame.display.set_mode((windows_size))
pygame.display.set_caption("Тестовый проект")

image1 = pygame.image.load("star.png")
image_rect1 = image1.get_rect()

image2 = pygame.image.load("star.png")
image_rect2 = image2.get_rect()


run = True


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



        if event.type == pygame.MOUSEMOTION:
            mouseX, mouseY = pygame.mouse.get_pos()
            image_rect1.x = mouseX - 60
            image_rect1.y = mouseY - 60

    if image_rect1.colliderect(image_rect2):
        print("Б-о-о-о-о-о-о-о-о-М")
        time.sleep(1)



    screen.fill((0, 6, 0))
    screen.blit(image1, image_rect1)
    screen.blit(image2, image_rect2)
    pygame.display.flip()

pygame.quit()

