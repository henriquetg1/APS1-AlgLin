from sprites import Nave, Bala, Estrela, CorpoCeleste, Alvo
import pygame


class Jogo:
    def __init__(self, num_alvos):
        pygame.init()
        pygame.display.set_caption('APS1 ALG LIN')
        self.width = 900
        self.height = 675
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.all_sprites = pygame.sprite.Group()
        self.nave = Nave()
        self.all_sprites.add(self.nave)
        self.num_alvos = num_alvos

        for i in range(50):
            estrela = Estrela()
            self.all_sprites.add(estrela)

        self.width = 900
        self.height = 675
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.tiros = 5

    def roda(self):
        self.desenha_tela_inicial_gameover()
        self.desenha_telas()
        pygame.display.update()        

    def update(self):
        clock = pygame.time.Clock()
        if self.tiros == 0:
            return TelaGameOver()
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

        self.alvos = pygame.sprite.Group()
        for sprite in self.all_sprites:
            if isinstance(sprite, Alvo):
                self.alvos.add(sprite)

        for bala in self.all_sprites:
            if isinstance(bala, Bala):
                gravidade = self.corpo_celeste.calcular_forca_gravitacional(bala)
                bala.vel += gravidade 
                colisoes = pygame.sprite.spritecollide(bala, self.alvos, True)
                for alvo in colisoes:
                    self.num_alvos -= 1

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
        super().__init__(1)
        self.alvo = Alvo((self.width // 2 + 150, self.height // 2 - 300))
        self.corpo_celeste = CorpoCeleste((self.width // 2 - 50 , self.height // 2), 1000)  
        self.all_sprites.add(self.alvo, self.corpo_celeste)

    def desenha_tela_inicial_gameover(self):    
        pass

    def update(self):
        if self.num_alvos == 0:
            return TelaJogo2()
        return super().update() 

class TelaJogo2(Jogo):
    def __init__(self):
        super().__init__(2)
        self.alvo = Alvo((self.width // 2 + 150, self.height // 2 - 300))
        self.alvo2 = Alvo((self.width // 2 - 150, self.height // 2 - 300))
        self.corpo_celeste = CorpoCeleste((self.width // 2 - 50 , self.height // 2), 1000)  
        self.corpo_celeste2 = CorpoCeleste((self.width // 2 + 50 , self.height // 2), 1000)  
        self.all_sprites.add(self.corpo_celeste, self.corpo_celeste2, self.alvo, self.alvo2)
    
    def desenha_tela_inicial_gameover(self):
        pass

    def update(self):
        if self.num_alvos == 0:
            return TelaJogo3()
        return super().update() 

class TelaJogo3(Jogo):
    def __init__(self):
        super().__init__(3)
        self.alvo = Alvo((self.width // 2 + 150, self.height // 2 - 300))
        self.alvo2 = Alvo((self.width // 2 - 150, self.height // 2 - 300))
        self.alvo3 = Alvo((self.width // 2 - 250, self.height // 2 - 300))
        self.corpo_celeste = CorpoCeleste((self.width // 2 - 50 , self.height // 2), 1000)  
        self.corpo_celeste2 = CorpoCeleste((self.width // 2 + 50 , self.height // 2), 1000)  
        self.corpo_celeste3 = CorpoCeleste((self.width // 2 + 150 , self.height // 2), 1000)  
        self.all_sprites.add(self.corpo_celeste, self.corpo_celeste2, self.corpo_celeste3, self.alvo, self.alvo2, self.alvo3)

    def desenha_tela_inicial_gameover(self):
        pass

    def update(self):
        if self.num_alvos == 0:
            return TelaInicial()
        return super().update() 

class TelaInicial(Jogo):
    def __init__(self):
        super().__init__(0)
        self.font = pygame.font.Font(None, 60)
        self.text = self.font.render("Iniciar", True, self.BLACK)
        self.text_rect = self.text.get_rect(center=(self.width // 2, self.height // 2))
        self.text2 = self.font.render("Sair", True, self.BLACK)
        self.text2_rect = self.text2.get_rect(center=(self.width // 2, self.height // 2 + 100))

    def desenha_tela_inicial_gameover(self):
        self.screen.fill(self.BLACK)
        pygame.draw.rect(self.screen, self.WHITE, self.text_rect)
        self.screen.blit(self.text, self.text_rect)
        pygame.draw.rect(self.screen, self.WHITE, self.text2_rect)
        self.screen.blit(self.text2, self.text2_rect)

    def desenha_telas(self):
        pass

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
        super().__init__(0)
        self.font = pygame.font.Font(None, 60)
        self.text = self.font.render("Game Over", True, self.WHITE)
        self.text_rect = self.text.get_rect(center=(self.width // 2, self.height // 2))

    def desenha_tela_inicial_gameover(self):
        self.screen.fill(self.BLACK)
        pygame.draw.rect(self.screen, self.RED, self.text_rect)

    def desenha_telas(self):
        pass

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                return TelaInicial()
        return self