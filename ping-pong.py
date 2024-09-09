import pygame
import sys

# Инициализация Pygame
pygame.init()

# Определяем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Настройки окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Пинг-понг")

# Настройки ракеток
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
paddle_speed = 5

# Настройки мяча
BALL_SIZE = 20

# Начальные позиции
left_paddle = pygame.Rect(10, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - 20, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)


# Функция для выбора скорости
def choose_speed():
    screen.fill(BLACK)
    font = pygame.font.Font(None, 74)
    text = font.render("Выберите скорость мяча", True, WHITE)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 4))

    font = pygame.font.Font(None, 36)
    text1 = font.render("1 - Медленная", True, WHITE)
    text2 = font.render("2 - Средняя", True, WHITE)
    text3 = font.render("3 - Быстрая", True, WHITE)
    screen.blit(text1, (WIDTH // 2 - text1.get_width() // 2, HEIGHT // 2))
    screen.blit(text2, (WIDTH // 2 - text2.get_width() // 2, HEIGHT // 2 + 40))
    screen.blit(text3, (WIDTH // 2 - text3.get_width() // 2, HEIGHT // 2 + 80))

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return 3
                elif event.key == pygame.K_2:
                    return 5
                elif event.key == pygame.K_3:
                    return 8


# Функция для отрисовки начального экрана
def draw_start_screen():
    screen.fill(BLACK)
    font = pygame.font.Font(None, 74)
    text = font.render("Выберите режим игры", True, WHITE)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 4))

    font = pygame.font.Font(None, 36)
    text1 = font.render("1 - Человек против Человека", True, WHITE)
    text2 = font.render("2 - Человек против Компьютера", True, WHITE)
    screen.blit(text1, (WIDTH // 2 - text1.get_width() // 2, HEIGHT // 2))
    screen.blit(text2, (WIDTH // 2 - text2.get_width() // 2, HEIGHT // 2 + 40))

    pygame.display.flip()


# Основной игровой цикл
def main():
    ball_speed_x = choose_speed()
    ball_speed_y = ball_speed_x
    game_mode = None

    # Ждем выбора режима
    while game_mode is None:
        draw_start_screen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    game_mode = '1'
                elif event.key == pygame.K_2:
                    game_mode = '2'

    # Игровой цикл
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Управление ракетками
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and left_paddle.top > 0:
            left_paddle.y -= paddle_speed
        if keys[pygame.K_DOWN] and left_paddle.bottom < HEIGHT:
            left_paddle.y += paddle_speed

        if game_mode == '1':  # Человек против Человека
            if keys[pygame.K_w] and right_paddle.top > 0:
                right_paddle.y -= paddle_speed
            if keys[pygame.K_s] and right_paddle.bottom < HEIGHT:
                right_paddle.y += paddle_speed
        else:  # Человек против Компьютера
            if ball.centery < right_paddle.centery and right_paddle.top > 0:
                right_paddle.y -= paddle_speed
            if ball.centery > right_paddle.centery and right_paddle.bottom < HEIGHT:
                right_paddle.y += paddle_speed

        # Движение мяча
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        # Отскок от верхнего и нижнего края
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_speed_y = -ball_speed_y

        # Отскок от ракеток
        if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
            ball_speed_x = -ball_speed_x

        # Проверка выхода мяча за пределы экрана
        if ball.left <= 0 or ball.right >= WIDTH:
            ball.x, ball.y = WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2
            ball_speed_x = -ball_speed_x

        # Отрисовка
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, left_paddle)
        pygame.draw.rect(screen, WHITE, right_paddle)
        pygame.draw.ellipse(screen, WHITE, ball)
        pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

        pygame.display.flip()
        pygame.time.Clock().tick(60)


if __name__ == "__main__":
    main()