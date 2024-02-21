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
        self.tiros = 15

    def roda(self):
        self.desenha_telas()
        pygame.display.update()        

    def update(self):
        clock = pygame.time.Clock()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.tiros > 0:
                        bala = Bala(self.nave.rect.center, event.pos)
                        self.all_sprites.add(bala)
                        self.tiros -= 1

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
    
    def desenha_telas(self):
        self.screen.fill(self.BLACK) 
        self.all_sprites.draw(self.screen)
        fonte = pygame.font.Font(None, 36)
        texto_vidas = fonte.render(f'Tiros: {self.tiros}', True, self.WHITE)
        self.screen.blit(texto_vidas, (10, 10))

class TelaJogo1(Jogo):
    def __init__(self):
        super().__init__()
        self.alvo = Alvo((self.width // 2 + 150, self.height // 2 - 300))
        self.all_sprites.add(self.alvo)
        self.corpo_celeste = CorpoCeleste((self.width // 2 - 50 , self.height // 2), 1000)  
        self.all_sprites.add(self.corpo_celeste)

class TelaJogo2(Jogo):
    def __init__(self):
        super().__init__()
        self.alvo = Alvo((self.width // 2 + 150, self.height // 2 - 300))
        self.alvo2 = Alvo((self.width // 2 - 150, self.height // 2 - 300))
        self.corpo_celeste = CorpoCeleste((self.width // 2 - 50 , self.height // 2), 1000)  
        self.corpo_celeste2 = CorpoCeleste((self.width // 2 + 50 , self.height // 2), 1000)  
        self.all_sprites.add(self.corpo_celeste, self.corpo_celeste2, self.alvo, self.alvo2)

class TelaJogo3(Jogo):
    def __init__(self):
        super().__init__()
        self.alvo = Alvo((self.width // 2 + 150, self.height // 2 - 300))
        self.alvo2 = Alvo((self.width // 2 - 150, self.height // 2 - 300))
        self.alvo2 = Alvo((self.width // 2 - 250, self.height // 2 - 300))
        self.corpo_celeste = CorpoCeleste((self.width // 2 - 50 , self.height // 2), 1000)  
        self.corpo_celeste2 = CorpoCeleste((self.width // 2 + 50 , self.height // 2), 1000)  
        self.corpo_celeste2 = CorpoCeleste((self.width // 2 + 150 , self.height // 2), 1000)  
        self.all_sprites.add(self.corpo_celeste, self.corpo_celeste2, self.alvo, self.alvo2)
