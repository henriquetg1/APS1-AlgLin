from sprites import Nave, Bala, Estrela, CorpoCeleste, Alvo
import pygame


class Jogo:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('APS1 ALG LIN')
        self.width = 900
        self.height = 675
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.all_sprites = pygame.sprite.Group()
        self.nave = Nave()
        self.all_sprites.add(self.nave)

        for i in range(50):
            estrela = Estrela()
            self.all_sprites.add(estrela)

        self.width = 900
        self.height = 675
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.tiros = 15

    def roda(self):
        self.desenha()
        pygame.display.update()

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

        for bala in self.all_sprites:
            if isinstance(bala, Bala):
                gravidade = self.corpo_celeste.calcular_forca_gravitacional(bala)
                bala.vel += gravidade 
                if pygame.sprite.spritecollide(self.alvo, self.all_sprites, False):
                    self.alvo.verificar_colisao(bala)

        self.all_sprites.update()
        pygame.display.flip()
        clock.tick(60)
        return self

class TelaJogo1(Jogo):
    def __init__(self):
        super().__init__()
        self.alvo = Alvo((self.width // 2 + 50, self.height // 2 + 100))
        self.all_sprites.add(self.alvo)
        self.corpo_celeste = CorpoCeleste((self.width // 2, self.height // 2), 1000)  
        self.all_sprites.add(self.corpo_celeste)
    
    def desenha(self):
        self.screen.fill(self.BLACK) 
        self.all_sprites.draw(self.screen)

class TelaInicial(Jogo):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.Font(None, 60)
        self.text = self.font.render("Iniciar", True, self.BLACK)
        self.text_rect = self.text.get_rect(center=(self.width // 2, self.height // 2))
        self.text2 = self.font.render("Sair", True, self.BLACK)
        self.text2_rect = self.text2.get_rect(center=(self.width // 2, self.height // 2 + 100))

    def desenha(self):
        self.screen.fill(self.BLACK)
        pygame.draw.rect(self.screen, self.WHITE, self.text_rect)
        self.screen.blit(self.text, self.text_rect)
        pygame.draw.rect(self.screen, self.WHITE, self.text2_rect)
        self.screen.blit(self.text2, self.text2_rect)

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.text_rect.collidepoint(event.pos):
                    return TelaJogo1()
                elif self.text2_rect.collidepoint(event.pos):
                    pygame.quit()
                    quit()
        return self

class TelaGameOver(Jogo):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.Font(None, 60)
        self.text = self.font.render("Game Over", True, self.WHITE)
        self.text_rect = self.text.get_rect(center=(self.width // 2, self.height // 2))

    def desenha(self):
        self.screen.fill(self.BLACK)
        pygame.draw.rect(self.screen, self.RED, self.text_rect)

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                return TelaInicial()
        return self