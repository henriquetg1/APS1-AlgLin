import pygame, math, random 
from variaveis import *

class Nave(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original_image = pygame.image.load("assets/img/nave.png").convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, (100, 100))
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect(center=(75, HEIGHT - 75)) # Posição inicial da nave
        self.angle = 0

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        self.angle = math.atan2(mouse_pos[1] - self.rect.centery, mouse_pos[0] - self.rect.centerx)
        self.image = pygame.transform.rotate(self.original_image, math.degrees(-self.angle))
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

class Estrela(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((2, 2))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH)
        self.rect.y = random.randint(0, HEIGHT)
        
class CorpoCeleste(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.Surface((50, 50), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=position)
        pygame.draw.circle(self.image, WHITE, (25, 25), 25) 
        self.pos = pygame.math.Vector2(position)

    def calcular_forca_gravitacional(self, bala):
        # Constante de gravitação universal
        c = 7500  
        # Calcula os vetores da diferença entre a posição x e y dos vetores do corpo celeste e da bala
        direction = self.pos - bala.pos
        # Calcula a hipotenusa do triângulo formado pela diferença entre a posição x e y do corpo celeste e da bala
        distance_squared = direction.x ** 2 + direction.y ** 2
        # Calcula a força gravitacional
        forca = (c) / distance_squared
        # Calcula o vetor da força gravitacional
        gravidade = direction.normalize() * forca
        # Retorna o vetor 
        return gravidade    

class Alvo(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.Surface((50, 50), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=position)
        pygame.draw.circle(self.image, (50,50,50), (25, 25), 25)  # Desenha o círculo
