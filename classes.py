import pygame 

class Jogo:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('APS1 ALG LIN')
        self.window = pygame.display.set_mode((800,600))
        self.fundo = pygame.image.load('assets\img/ceu-estrelado.jpeg')
        self.passaro = pygame.image.load('assets\img/angry-birds-png.png')
        self.porco = pygame.image.load('assets\img/porco-angry-birds.png')
        self.tiros_passaros = []

    def roda(self):
        self.desenha()
        pygame.display.update()

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                self.atira(mouse_x, mouse_y)

    def atira(self, x, y):
        distancia_x = x - 100
        distancia_y = y - 100
        d = math.sqrt(distancia_x**2 + distancia_y**2)
        # Velocidade com base na distância do mouse
        velocidade = min(10, d/10)

class TelaJogo(Jogo):
    def __init__(self):
        super().__init__()
        self.window.fill((0,0,0))

    def desenha(self):
        self.window.blit(self.fundo, (0,0))
        self.window.blit(self.passaro, (100,100))
        self.window.blit(self.porco, (600,100))

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        return self 

class Passaro_Projetil:
    def __init__(self, origem_x, origem_y, destino_x, destino_y, velocidade):
        self.x = origem_x
        self.y = origem_y
        self.destino_x = destino_x
        self.destino_y = destino_y
        self.velocidade = velocidade

    def movimento(self):
        distancia_x = self.destino_x - self.x
        distancia_y = self.destino_y - self.y
        modulo = math.sqrt(distancia_x**2 + distancia_y**2)
        if modulo > self.velocidade:
            self.x += distancia_x * self.velocidade / d
            self.y += distancia_y * self.velocidade / d
        else:
            self.x = self.destino_x
            self.y = self.destino_y
    
tela_atual = TelaJogo()
while True:
    tela_atual.roda()
    tela_atual = tela_atual.update()
