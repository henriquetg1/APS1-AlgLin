import pygame, math

class Jogo:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('APS1 ALG LIN')
        self.window = pygame.display.set_mode((1200,800))
        img_fundo = pygame.image.load('assets\img/ceu-estrelado.jpeg')
        self.fundo = pygame.transform.scale(img_fundo, (1200,800))
        self.porco = pygame.image.load('assets\img/porco-angry-birds.png')
        
        img_passaro = pygame.image.load('assets\img/angry-birds-png.png')
        self.passaro = pygame.transform.scale(img_passaro, (50,50))
        self.rect_passaro = self.passaro.get_rect()
        self.condicao_passaro = False

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
        self.pos_canhao = (10,600)
        # self.eixo_rotacao ser não mais no centro da imagem e sim a borda esquerda
        self.eixo_rotacao = (self.pos_canhao[0], self.pos_canhao[1] + 100)
        self.canhao_rotacionado = self.canhao_original
        self.canhao_rect = self.canhao_rotacionado.get_rect(topleft=self.pos_canhao)



    def desenha_canhao(self, window):
        window.blit(self.canhao_rotacionado, self.pos_canhao)
        #desenha o retangulo para me ajudar a entender a posicao 
        pygame.draw.rect(window, (255, 0, 0), self.canhao_rect, 2)


    def rotaciona_canhao(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - self.eixo_rotacao[0], mouse_y - self.eixo_rotacao[1]
        angle = math.degrees(math.atan2(-rel_y, rel_x))
        self.canhao_rotacionado = pygame.transform.rotate(self.canhao_original, angle)
        # pega o rect que sempre muda com a rotacao
        self.canhao_rect = self.canhao_rotacionado.get_rect(topleft=self.pos_canhao)

        return math.radians(angle)

class TelaJogo(Jogo):
    def __init__(self):
        super().__init__()
        self.window.fill((0,0,0))      
        self.canhao = Canhao() 

    def desenha(self):
        self.window.blit(self.fundo, (0,0))
        self.canhao.desenha_canhao(self.window)
        if self.condicao_passaro:
            self.window.blit(self.passaro, self.rect_passaro)

    def update(self):
        angle = self.canhao.rotaciona_canhao()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and self.condicao_passaro == False:
                self.condicao_passaro = True
                # Ajusta a posição inicial do pássaro para a boca do canhão
                self.rect_passaro.x = 100
                self.rect_passaro.y = 600
                
                # Calcula o vetor de direção com base no ângulo de rotação do canhão
                self.dir_x = math.cos(angle)
                self.dir_y = -math.sin(angle)

        if self.condicao_passaro:
            # Move o pássaro na direção do vetor
            self.rect_passaro.x += self.dir_x 
            self.rect_passaro.y += self.dir_y 
            print(self.rect_passaro.x, self.rect_passaro.y)

            # Verifica se o pássaro saiu da tela
            if not self.window.get_rect().colliderect(self.rect_passaro):
                self.condicao_passaro = False
        return self 

# class Passaro_Projetil:
#     def __init__(self, origem_x, origem_y, destino_x, destino_y, velocidade):
#         self.x = origem_x
#         self.y = origem_y
#         self.destino_x = destino_x
#         self.destino_y = destino_y
#         self.velocidade = velocidade

#     def movimento(self):
#         distancia_x = self.destino_x - self.x
#         distancia_y = self.destino_y - self.y
#         modulo = math.sqrt(distancia_x**2 + distancia_y**2)
#         if modulo > self.velocidade:
#             self.x += distancia_x * self.velocidade / d
#             self.y += distancia_y * self.velocidade / d
#         else:
#             self.x = self.destino_x
#             self.y = self.destino_y
    
tela_atual = TelaJogo()
while True:
    tela_atual.roda()
    tela_atual = tela_atual.update()
