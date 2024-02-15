import pygame, math

class Jogo:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('APS1 ALG LIN')
        self.window = pygame.display.set_mode((1200,800))
        img_fundo = pygame.image.load('assets\img/ceu-estrelado.jpeg')
        self.fundo = pygame.transform.scale(img_fundo, (1200,800))
        self.porco = pygame.image.load('assets\img/porco-angry-birds.png')

    def roda(self):
        self.desenha()
        pygame.display.update()

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

class Canhao:
    def __init__(self):
        img_canhao = pygame.image.load('assets\img/rocket-launcher.png')
        self.canhao_original = pygame.transform.scale(img_canhao, (200,100))
        self.canhao_rotacionado = self.canhao_original
        self.pos_canhao = (10,600)

    def desenha_canhao(self,window):
        window.blit(self.canhao_rotacionado, self.pos_canhao)

    def rotaciona_canhao(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - self.pos_canhao[0], mouse_y - self.pos_canhao[1]
        angle = math.degrees(math.atan2(-rel_y, rel_x))
        self.canhao_rotacionado = pygame.transform.rotate(self.canhao_original, angle)

class Passaro: 
    def __init__(self):
        img_passaro = pygame.image.load('assets\img/angry-birds-png.png')
        self.passaro = pygame.transform.scale(img_passaro, (50,50))
        self.rect_passaro = self.passaro.get_rect()
        self.condicao_passaro = False

    def desenha_disparo(self,window):
        if self.condicao_passaro:
            window.blit(self.passaro, self.rect_passaro)

    def atira_disparo(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - self.pos_disparo[0], mouse_y - self.pos_disparo[1]
        angle = math.degrees(math.atan2(-rel_y, rel_x))
        self.disparo = pygame.transform.rotate(self.disparo, angle)

class TelaJogo(Jogo):
    def __init__(self):
        super().__init__()
        self.window.fill((0,0,0))      
        self.canhao = Canhao()  

    def desenha(self):
        self.window.blit(self.fundo, (0,0))
        self.canhao.desenha_canhao(self.window)

    def update(self):

        self.canhao.rotaciona_canhao()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        return self 
    
tela_atual = TelaJogo()
while True:
    tela_atual.roda()
    tela_atual = tela_atual.update()
