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
        
class CorpoCeleste(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.image.load("assets\img\planeta verde fase 1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect(center=position)
        self.pos = pygame.math.Vector2(position)

    def calcular_forca_gravitacional(self, bala):
        # Constante de gravitação universal
        c = 7500  
        # Calcula os vetores da diferença entre a posição x e y do corpo celeste e da bala
        direction = self.pos - bala.pos
        # Calcula a hipotenusa do triângulo formado pela diferença entre a posição x e y do corpo celeste e da bala
        distance_squared = direction.x ** 2 + direction.y ** 2
        # Calcula a força gravitacional
        force_magnitude = (c) / distance_squared
        print(force_magnitude)
        # Calcula o vetor da força gravitacional
        force = direction.normalize() * force_magnitude
        return force
    
class CorpoCeleste2(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.image.load("assets\img\Planeta-Fase2e3.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect(center=position)
        self.pos = pygame.math.Vector2(position)

    def calcular_forca_gravitacional(self, bala):
        # Constante de gravitação universal
        c = 7500  
        # Calcula os vetores da diferença entre a posição x e y do corpo celeste e da bala
        direction = self.pos - bala.pos
        # Calcula a hipotenusa do triângulo formado pela diferença entre a posição x e y do corpo celeste e da bala
        distance_squared = direction.x ** 2 + direction.y ** 2
        # Calcula a força gravitacional
        force_magnitude = (c) / distance_squared
        print(force_magnitude)
        # Calcula o vetor da força gravitacional
        force = direction.normalize() * force_magnitude
        return force
    
class CorpoCeleste3(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.image.load("assets\img\saturno fase 3.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (120, 120))
        self.rect = self.image.get_rect(center=position)
        self.pos = pygame.math.Vector2(position)

    def calcular_forca_gravitacional(self, bala):
        # Constante de gravitação universal
        c = 7500  
        # Calcula os vetores da diferença entre a posição x e y do corpo celeste e da bala
        direction = self.pos - bala.pos
        # Calcula a hipotenusa do triângulo formado pela diferença entre a posição x e y do corpo celeste e da bala
        distance_squared = direction.x ** 2 + direction.y ** 2
        # Calcula a força gravitacional
        force_magnitude = (c) / distance_squared
        print(force_magnitude)
        # Calcula o vetor da força gravitacional
        force = direction.normalize() * force_magnitude
        # Retorna o vetor 
        return force    

class Alvo(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        # Carrega a imagem do arquivo
        self.image = pygame.image.load("assets/img/ufo.png").convert_alpha()
        # Redimensiona a imagem para o tamanho desejado
        self.image = pygame.transform.scale(self.image, (75, 50))
        self.rect = self.image.get_rect(center=position)
