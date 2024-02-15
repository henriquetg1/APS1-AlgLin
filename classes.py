import pygame 

class Jogo:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('APS1 ALG LIN')
        self.window = pygame.display.set_mode((800,600))
        self.fundo = pygame.image.load('assets\img/ceu-estrelado.jpeg')
        self.passaro = pygame.image.load('assets\img/angry-birds-png.png')
        self.porco = pygame.image.load('assets\img/porco-angry-birds.png')
        imagem_canhao = pygame.image.load('assets\img/rocket-launcher.png')
        self.canhao = pygame.transform.scale(imagem_canhao, (200, 100))

    def roda(self):
        self.desenha()
        pygame.display.update()

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

class TelaJogo(Jogo):
    def __init__(self):
        super().__init__()
        self.window.fill((0,0,0))        

    def desenha(self):
        self.window.blit(self.fundo, (0,0))
        self.window.blit(self.canhao, (10,490))

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        return self 
    
tela_atual = TelaJogo()
while True:
    tela_atual.roda()
    tela_atual = tela_atual.update()
