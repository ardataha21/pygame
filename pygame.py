import pygame
import sys

# Pygame'ı başlat
pygame.init()

# Ekran boyutları
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Parkur Oyunu")

# Renkler
black = (0, 0, 0)
white = (255, 255, 255)

# Oyuncu özellikleri
player_size = 50
player_x = width // 2 - player_size // 2
player_y = height - 2 * player_size
player_speed = 5

# Engeller
obstacle_size = 50
obstacle_speed = 5
obstacle_y = 0
obstacle_x = width // 2 - obstacle_size // 2

# Skor
score = 0
font = pygame.font.Font(None, 36)

# Ana oyun döngüsü
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Oyuncu hareketi
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < width - player_size:
        player_x += player_speed

    # Engelleri hareket ettir
    obstacle_y += obstacle_speed
    if obstacle_y > height:
        obstacle_y = 0
        obstacle_x = pygame.randint(0, width - obstacle_size)
        score += 1

    # Çarpışma kontrolü
    if (
        player_x < obstacle_x + obstacle_size
        and player_x + player_size > obstacle_x
        and player_y < obstacle_y + obstacle_size
        and player_y + player_size > obstacle_y
    ):
        print("Oyun Bitti! Skor:", score)
        pygame.quit()
        sys.exit()

    # Ekranı temizle
    screen.fill(black)

    # Engelleri çiz
    pygame.draw.rect(screen, white, (obstacle_x, obstacle_y, obstacle_size, obstacle_size))

    # Oyuncuyu çiz
    pygame.draw.rect(screen, white, (player_x, player_y, player_size, player_size))

    # Skoru ekrana yazdır
    score_text = font.render("Skor: {}".format(score), True, white)
    screen.blit(score_text, (10, 10))

    # Ekranı güncelle
    pygame.display.flip()

    # FPS ayarı
    clock.tick(60)
