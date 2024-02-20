import pygame
import math
import random

pygame.init()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

WIDTH, HEIGHT = 900, 675
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("APS1")

BARRA_LENGTH = 20 # Tamanho barra

class Barra(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original_image = pygame.Surface((BARRA_LENGTH, 5))
        self.original_image.fill(RED)
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect(center=(75, HEIGHT - 45)) # Posição inicial da barra
        self.angle = 0

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        self.angle = math.atan2(mouse_pos[1] - self.rect.centery, mouse_pos[0] - self.rect.centerx)
        self.rect = self.image.get_rect(center=self.rect.center)

class Bala(pygame.sprite.Sprite):
    def __init__(self, position, target):
        super().__init__()
        self.original_image = pygame.image.load("assets/img/bala.png").convert_alpha()
        self.rect = self.original_image.get_rect(center=position)
        self.pos = pygame.math.Vector2(position)
        direction = pygame.math.Vector2(target) - self.pos
        self.vel = direction.normalize() * min(direction.length() * 0.02, 10) # Velocidade conforme a distância para o mouse
        self.angle = 0

    def update(self):
        self.pos += self.vel
        self.rect.center = self.pos
        self.angle = math.degrees(math.atan2(self.vel.y, self.vel.x))
        rotated_image = pygame.transform.rotate(self.original_image, -self.angle)
        self.image = pygame.transform.scale(rotated_image, (35, 35))
        self.rect = self.image.get_rect(center=self.rect.center)
        if not pygame.Rect(0, 0, WIDTH, HEIGHT).colliderect(self.rect):
            self.kill()

# Classe para criar estrelas no fundo
class Estrela(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((2, 2))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH)
        self.rect.y = random.randint(0, HEIGHT)

all_sprites = pygame.sprite.Group()
barra = Barra()
all_sprites.add(barra)

for i in range(50):
    estrela = Estrela()
    all_sprites.add(estrela)

running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                bala = Bala(barra.rect.center, event.pos)
                all_sprites.add(bala)

    all_sprites.update()
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
