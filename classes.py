import pygame, random, math

class Jogo:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('APS1 ALG LIN')
        self.screen = pygame.display.set_mode((900,675))
        self.width = 900
        self.height = 675
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)

    def roda(self):
        self.desenha()
        pygame.display.update()

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

class Nave(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original_image = pygame.image.load("assets/img/nave.png").convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, (100, 100))
        self.image = self.original_image.copy()
        self.jogo = Jogo()
        self.rect = self.image.get_rect(center=(75, self.jogo.height - 75)) # Posição inicial da nave
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
        self.jogo = Jogo()
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
        if not pygame.Rect(0, 0, self.jogo.width, self.jogo.height).colliderect(self.rect):
            self.kill()

class Estrela(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.jogo = Jogo()
        self.image = pygame.Surface((2, 2))
        self.image.fill(self.jogo.WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, self.jogo.width)
        self.rect.y = random.randint(0, self.jogo.height)

class TelaJogo(Jogo):
    def __init__(self):
        super().__init__()
        self.all_sprites = pygame.sprite.Group()
        self.nave = Nave()
        self.all_sprites.add(self.nave)
        for i in range(50):
            estrela = Estrela()
            self.all_sprites.add(estrela)

    def desenha(self):
        self.screen.fill(self.BLACK)
        self.all_sprites.draw(self.screen)
            
    def update(self):
        clock = pygame.time.Clock()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    bala = Bala(self.nave.rect.center, event.pos)
                    self.all_sprites.add(bala)

        self.all_sprites.update()
        pygame.display.flip()
        clock.tick(60)
        return self

tela_atual = TelaJogo()
while True:
    tela_atual.roda()
    tela_atual = tela_atual.update()
