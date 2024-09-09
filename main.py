import pygame
pygame.init()

windows_size = 800, 600
screen = pygame.display.set_mode((windows_size))
pygame.display.set_caption("Тестовый проект")

image = pygame.image.load("star.png")
image_rect = image.get_rect()



run = True


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEMOTION:
            mouseX, mouseY = pygame.mouse.get_pos()
            image_rect.x = mouseX - 60
            image_rect.y = mouseY - 60





    screen.fill((0, 6, 0))
    screen.blit(image, image_rect)
    pygame.display.flip()

pygame.quit()

